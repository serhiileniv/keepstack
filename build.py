#!/usr/bin/env python3
"""Build the hub: README.md + a static, SEO-friendly site from entries/*.md

Stdlib only, on purpose — no install step, nothing to rot in six months.

    python3 build.py            build README.md + site/
    python3 build.py --stale    what's overdue for a re-check
    python3 build.py --check    validate entries, exit 1 on problems
    python3 build.py --sync     pull link + short description from upstream into entries
    python3 build.py --drift    upstreams that moved since last_checked (exit 1 if any)
    python3 build.py --serve    build, then serve site/ on :8000
"""
import sys, re, html, datetime, pathlib, shutil

ROOT = pathlib.Path(__file__).parent
ENTRIES, LIBRARY, SITE = ROOT / "entries", ROOT / "library", ROOT / "site"

# Set this before the first deploy — it drives canonical URLs and sitemap.xml.
SITE_URL = "https://ai-hub-dg0.pages.dev"
SITE_NAME = "AI Hub"
REPO_URL = "https://github.com/serhiileniv/ai-hub"
AUTHOR = "Serhii Leniv"
TAGLINE = ("Agent skills, configs and tools I run on real work. Nothing ranked, "
           "nothing filler — every entry carries the day I last confirmed it works.")

STALE_AFTER_DAYS = 90
KINDS = ("skill", "mcp", "config", "workflow", "tool", "model", "prompt")
REQUIRED = ("name", "what", "kind", "group", "last_checked")

# Grouped by the moment you'd reach for the thing, not by what it is and not by
# how good it is. Nothing here is ranked — if it's in the hub, it's in use. See
# D10 in notes/DECISIONS.md.
GROUPS = [
    ("planning", "Planning"),
    ("writing", "Writing & review"),
    ("codebase", "Working in a codebase"),
    ("terminal", "Terminal"),
    ("services", "Connected services"),
]
GROUP_KEYS = tuple(g for g, _ in GROUPS)


# ---------------------------------------------------------------- frontmatter
def parse_scalar(v):
    v = v.strip()
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        return [p.strip().strip('"').strip("'") for p in inner.split(",") if p.strip()]
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    if v.lower() in ("true", "false"):
        return v.lower() == "true"
    return v


def load(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"{path.name}: no frontmatter")
    _, fm, body = text.split("---", 2)
    data = {}
    for line in fm.splitlines():
        if line.strip().startswith("#"):
            continue
        line = line.split(" #")[0]
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        if re.match(r"^[a-z_]+$", k.strip()):
            data[k.strip()] = parse_scalar(v)
    data.update(_file=path.name, _slug=path.stem, _body=body.strip())
    return data


def entries():
    return [load(p) for p in sorted(ENTRIES.glob("*.md")) if not p.name.startswith("_")]


def as_date(v):
    try:
        return datetime.date.fromisoformat(str(v))
    except (ValueError, TypeError):
        return None


def age_days(e):
    d = as_date(e.get("last_checked"))
    return None if d is None else (datetime.date.today() - d).days


def is_stale(e):
    a = age_days(e)
    return True if a is None else a >= STALE_AFTER_DAYS


def fmt_date(v):
    d = as_date(v)
    return d.strftime("%-d %b %Y") if d else "—"


# ------------------------------------------------------------------- markdown
def inline(s):
    s = html.escape(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", s)
    return s


def render_md(text, shift=1):
    """A deliberately small Markdown subset: headings, paragraphs, fenced code,
    lists, tables, blockquotes, rules. Enough for entries, and nothing to update."""
    lines, out, i = text.split("\n"), [], 0
    while i < len(lines):
        line = lines[i]

        if line.startswith("```"):
            lang, buf, i = line[3:].strip(), [], i + 1
            while i < len(lines) and not lines[i].startswith("```"):
                buf.append(lines[i]); i += 1
            i += 1
            cls = f' class="lang-{html.escape(lang)}"' if lang else ""
            out.append(f"<pre><code{cls}>{html.escape(chr(10).join(buf))}</code></pre>")
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            lvl = min(len(m.group(1)) + shift, 6)
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>"); i += 1; continue

        if re.match(r"^\s*([-*_])\1{2,}\s*$", line):
            out.append("<hr>"); i += 1; continue

        # table
        if line.strip().startswith("|") and i + 1 < len(lines) \
                and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            def cells(r):
                return [c.strip() for c in r.strip().strip("|").split("|")]
            head = cells(line); i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(cells(lines[i])); i += 1
            th = "".join(f"<th>{inline(c)}</th>" for c in head)
            tb = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
                         for r in rows)
            out.append(f'<div class="tablewrap"><table><thead><tr>{th}</tr></thead>'
                       f"<tbody>{tb}</tbody></table></div>")
            continue

        if line.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i].lstrip(">").strip()); i += 1
            out.append(f"<blockquote>{inline(' '.join(buf))}</blockquote>")
            continue

        m = re.match(r"^\s*([-*+]|\d+\.)\s+", line)
        if m:
            ordered = m.group(1).endswith(".")
            items, cur = [], None
            while i < len(lines):
                mm = re.match(r"^\s*(?:[-*+]|\d+\.)\s+(.*)$", lines[i])
                if mm:
                    if cur is not None:
                        items.append(cur)
                    cur = mm.group(1)
                elif lines[i].strip() and lines[i].startswith(("  ", "\t")) and cur is not None:
                    cur += " " + lines[i].strip()
                else:
                    break
                i += 1
            if cur is not None:
                items.append(cur)
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
            continue

        if not line.strip():
            i += 1; continue

        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(
                r"^\s*(#{1,6}\s|```|\||>|[-*+]\s|\d+\.\s|([-*_])\2{2,}\s*$)", lines[i]):
            buf.append(lines[i].strip()); i += 1
        out.append(f"<p>{inline(' '.join(buf))}</p>")
    return "\n".join(out)


# ---------------------------------------------------------------- validation
def cmd_check(items, quiet=False):
    problems = []
    seen = {}
    for e in items:
        for f in REQUIRED:
            if not e.get(f):
                problems.append(f"{e['_file']}: missing '{f}'")
        if e.get("group") not in GROUP_KEYS:
            problems.append(f"{e['_file']}: group '{e.get('group')}' not in {GROUP_KEYS}")
        if e.get("kind") not in KINDS:
            problems.append(f"{e['_file']}: kind '{e.get('kind')}' not in {KINDS}")
        if as_date(e.get("last_checked")) is None:
            problems.append(f"{e['_file']}: last_checked must be YYYY-MM-DD")
        if not e.get("checked_against"):
            problems.append(f"{e['_file']}: checked_against is empty — an undated claim is the "
                            "one thing this project exists not to publish")
        if len(e.get("_body", "").strip()) < 120:
            problems.append(f"{e['_file']}: too thin. An entry earns its place by saying why "
                            "it's worth someone's afternoon")
        if e.get("source"):
            if not (ROOT / e["source"]).exists():
                problems.append(f"{e['_file']}: source '{e['source']}' does not exist")
        elif not e.get("url"):
            problems.append(f"{e['_file']}: needs either 'url' (external) or 'source' (in library/)")
        n = str(e.get("name", "")).lower()
        if n in seen:
            problems.append(f"{e['_file']}: duplicate name, also in {seen[n]}")
        seen[n] = e["_file"]
    if not quiet:
        for p in problems:
            print("✗", p)
        print(f"\n{len(items)} {'entry' if len(items) == 1 else 'entries'}, "
              f"{len(problems)} problem{'' if len(problems) == 1 else 's'}")
    return 1 if problems else 0


def cmd_stale(items, days):
    rows = sorted(((age_days(e), e) for e in items
                   if age_days(e) is None or age_days(e) >= days),
                  key=lambda r: -(r[0] if r[0] is not None else 10 ** 6))
    if not rows:
        print(f"Nothing older than {days} days. All {len(items)} entries current.")
        return 0
    print(f"{len(rows)} of {len(items)} not checked in {days}+ days:\n")
    for a, e in rows:
        print(f"  {('never' if a is None else str(a) + 'd'):>6}  "
              f"{e['_slug']:<34}{e.get('name','')}")
    print("\nRe-check, then bump last_checked and checked_against.")
    return 0


# ------------------------------------------------------------------ rendering

# --- sync --------------------------------------------------------------------
# The facts about an upstream go stale on their own; my note about it does not. So this
# refreshes only the two machine-knowable fields — `what` (the repo's own one-line
# description) and `upstream_pushed` — and never touches the group, the body,
# last_checked or checked_against. Opt an entry out with `sync: false`.

SYNCED = ("what", "upstream_pushed")


def _set_fm(path, updates):
    """Rewrite frontmatter keys in place. Line-based, to match the parser above."""
    text = path.read_text(encoding="utf-8")
    head, fm, body = text.split("---", 2)
    lines = fm.splitlines()
    for key, val in updates.items():
        val = '"%s"' % str(val).replace('"', "'") if key == "what" else str(val)
        for i, line in enumerate(lines):
            if line.split(":", 1)[0].strip() == key:
                lines[i] = "%s: %s" % (key, val)
                break
        else:
            anchor = next((i for i, l in enumerate(lines)
                           if l.split(":", 1)[0].strip() == "last_checked"), len(lines) - 1)
            lines.insert(anchor + 1, "%s: %s" % (key, val))
    path.write_text("---".join([head, "\n".join(lines) + "\n", body]), encoding="utf-8")


def cmd_sync(items):
    import urllib.error
    changed = skipped = 0
    for e in items:
        repo = _gh_repo(e.get("url", ""))
        if not repo or e.get("sync") is False:
            skipped += 1
            continue
        try:
            data = _api("https://api.github.com/repos/%s/%s" % repo[:2])
        except (urllib.error.URLError, urllib.error.HTTPError, OSError) as ex:
            print("✗ %-28s %s" % (e["_slug"], str(ex)[:60]))
            continue
        updates = {}
        desc = (data.get("description") or "").strip()
        if repo[2] and desc and desc != e.get("what"):
            updates["what"] = desc
        pushed = (data.get("pushed_at") or "")[:10]
        if pushed and pushed != str(e.get("upstream_pushed", "")):
            updates["upstream_pushed"] = pushed
        if updates:
            _set_fm(ENTRIES / e["_file"], updates)
            changed += 1
            for k, v in updates.items():
                print("→ %-28s %s: %s" % (e["_slug"], k, v))
    print("\n%d entr%s updated, %d not syncable (no GitHub URL, or sync: false)."
          % (changed, "y" if changed == 1 else "ies", skipped))
    if changed:
        print("Descriptions and upstream dates only — no words and no date of mine "
              "was touched. Re-run `python3 build.py` to publish.")
    return 0


# --- drift -------------------------------------------------------------------
# Has an upstream moved since I last checked it?
#
# This NEVER writes last_checked. That date means *I* looked at the thing; a machine
# bumping it would make every date on the site a lie, which is the one failure this
# project cannot survive. Drift only ever reports — the re-check stays manual.

def _gh_repo(url):
    """(owner, repo, is_root). is_root is False for a URL pointing inside the repo —
    a single skill in a monorepo, whose description is not the repo's description."""
    m = re.match(r"https?://github\.com/([^/]+)/([^/#?]+)(/[^#?]*)?", url or "")
    if not m:
        return None
    name = m.group(2)
    rest = (m.group(3) or "").strip("/")
    return (m.group(1), name[:-4] if name.endswith(".git") else name, not rest)


def _api(url):
    import urllib.request, json, os
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json",
                                               "User-Agent": "ai-hub-drift"})
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:
        req.add_header("Authorization", "Bearer " + tok)
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def cmd_drift(items):
    import urllib.error
    moved, broken, opaque = [], [], []
    for e in items:
        repo = _gh_repo(e.get("url", ""))
        checked = as_date(e.get("last_checked"))
        if not repo:
            opaque.append(e)
            continue
        try:
            data = _api("https://api.github.com/repos/%s/%s" % repo[:2])
        except urllib.error.HTTPError as ex:
            broken.append((e, "HTTP %s" % ex.code))
            continue
        except Exception as ex:
            broken.append((e, str(ex)[:70]))
            continue
        pushed = as_date((data.get("pushed_at") or "")[:10])
        if pushed and checked and pushed > checked:
            moved.append((e, pushed, (pushed - checked).days))

    out = []
    if moved:
        out.append("### Upstream moved since I last checked\n")
        out.append("| Entry | Last checked | Upstream pushed | Gap |")
        out.append("|---|---|---|---|")
        for e, pushed, gap in sorted(moved, key=lambda r: -r[2]):
            out.append("| [%s](entries/%s.md) | %s | %s | %d days |"
                       % (e.get("name"), e["_slug"], fmt_date(e.get("last_checked")),
                          fmt_date(pushed), gap))
        out.append("")
    if broken:
        out.append("### Link no longer resolves\n")
        for e, why in broken:
            out.append("- **%s** — `%s` (%s)" % (e.get("name"), e.get("url"), why))
        out.append("")
    if opaque:
        out.append("<sub>Not checkable automatically (no GitHub URL): %s</sub>"
                   % ", ".join(e.get("name", "?") for e in opaque))

    if not moved and not broken:
        print("No upstream has moved since its last_checked. %d entries, "
              "%d not auto-checkable." % (len(items), len(opaque)))
        return 0

    print("\n".join(out))
    print("\nRe-check these by hand, then bump `last_checked` and `checked_against` "
          "yourself. Nothing here has been dated for you.")
    return 1


def page(title, desc, body, path, extra_head="", groups=()):
    """path is the site-relative directory, '' for the root."""
    canonical = f"{SITE_URL}/{path}".rstrip("/") + ("/" if path else "")
    depth = "../" * (len(pathlib.PurePath(path).parts)) if path else ""
    shown = groups or GROUPS
    nav = "".join(f'<a href="{depth or "/"}#{k}">{html.escape(t)}</a>' for k, t in shown)
    nav += f'<a href="{depth or "/"}#dates">The dates</a>' 
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="{html.escape(SITE_NAME)}">
<meta name="twitter:card" content="summary">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<meta name="theme-color" content="#0a0a0a">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{depth}style.css">
{extra_head}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site">
  <div class="wrap">
    <a class="logo" href="{depth or '/'}">
      <span class="mark">&#9650;</span><span class="name">{html.escape(SITE_NAME)}</span>
    </a>
    <nav>{nav}</nav>
    <a class="ghost" href="{REPO_URL}" rel="noopener">GitHub &#8599;</a>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site">
  <div class="wrap">
    <p><strong>Nothing here is ranked.</strong> If it's on this site I use it. The only claim an
       entry makes is the day I last confirmed it still works.</p>
    <p><strong>No schedule.</strong> I re-check in bursts. A date older than {STALE_AFTER_DAYS}
       days may still be right — I just haven't confirmed it lately, and I'd rather say so.</p>
    <p class="fine">{html.escape(AUTHOR)} · built {datetime.date.today().strftime('%-d %B %Y')}</p>
  </div>
</footer>
</body>
</html>
"""


def card(e, depth=""):
    pill = ('<span class="pill mine">mine</span>' if e.get("mine")
            else f'<span class="pill">{html.escape(e.get("kind",""))}</span>')
    src = e.get("url") or e.get("source") or ""
    src = src.replace("https://github.com/", "").split("/tree/")[0]
    when = fmt_date(e.get("last_checked")).rsplit(" ", 1)[0]
    return f"""      <a class="card" href="{depth}e/{e['_slug']}/">
        <div class="top">
          <h3>{html.escape(e.get('name',''))}</h3>
          {pill}
        </div>
        <p class="what">{html.escape(e.get('what',''))}</p>
        <div class="foot">
          <span>{html.escape(src)}</span>
          <span class="d{' stale' if is_stale(e) else ''}">{html.escape(when)}</span>
        </div>
      </a>"""


def build_index(items):
    stale_n = sum(1 for e in items if is_stale(e))
    mine_n = sum(1 for e in items if e.get("mine"))
    newest = max((as_date(e.get("last_checked")) for e in items
                  if as_date(e.get("last_checked"))), default=None)
    against = sorted({v for e in items for v in (e.get("checked_against") or [])})
    tool = next((v for v in against if not v.startswith(("opus", "sonnet", "haiku"))), "—")

    present = [(k, t) for k, t in GROUPS if any(e.get("group") == k for e in items)]

    hero = f"""<section class="hero">
  <div class="wrap">
    <div class="inner">
      <span class="eyebrow"><i></i>Last checked {html.escape(fmt_date(newest))} &middot; {html.escape(', '.join(v for v in against if v.startswith(('opus','sonnet','haiku'))) or '—')}</span>
      <h1>Agent tooling that earned<span>a permanent place.</span></h1>
      <p class="tag">Skills, configs and small tools I run on real work. Nothing ranked,
         nothing filler &mdash; every entry carries <b>the day I last confirmed it works</b>.</p>
      <div class="cta">
        <a class="btn p" href="#{present[0][0] if present else 'dates'}">Browse the hub</a>
        <a class="btn s" href="#dates">Why the dates &darr;</a>
      </div>
      <div class="strip">
        <div><div class="k">In the hub</div><div class="v">{len(items)} {'tool' if len(items)==1 else 'tools'}</div></div>
        <div><div class="k">Built by me</div><div class="v">{mine_n}</div></div>
        <div><div class="k">Checked against</div><div class="v">{html.escape(tool)}</div></div>
        <div><div class="k">Overdue</div><div class="v{' warn' if stale_n else ''}">{'<em>none</em>' if not stale_n else stale_n}</div></div>
      </div>
    </div>
  </div>
</section>"""

    secs = []
    for key, title in present:
        b = sorted([e for e in items if e.get("group") == key],
                   key=lambda x: str(x.get("name", "")).lower())
        cards = "\n".join(card(e) for e in b)
        secs.append(f"""<section id="{key}" class="group">
  <div class="wrap">
    <div class="head">
      <h2>{html.escape(title)}</h2>
      <span class="count">{len(b)} {'tool' if len(b)==1 else 'tools'}</span>
    </div>
    <div class="grid">
{cards}
    </div>
  </div>
</section>""")

    secs.append(f"""<section class="wrap"><div class="band" id="dates">
    <h2>Why every entry has a date</h2>
    <dl>
      <div class="r"><dt>Last checked</dt><dd>The day <b>I</b> confirmed it still works, against
        the versions named on the entry. Never written by a bot.</dd></div>
      <div class="r"><dt>Upstream</dt><dd>The day the project itself last changed. Newer than my
        check means I'm slightly behind &mdash; the repo will tell you what moved.</dd></div>
      <div class="r"><dt>No schedule</dt><dd>I re-check in bursts. The date is here so you never
        have to take my word for how current this is.</dd></div>
    </dl>
  </div></section>""")

    return page(f"{SITE_NAME} — agent skills, configs and tools, dated and checked",
                TAGLINE, hero + "\n" + "\n".join(secs), "", groups=present)


def build_entry(e):
    a = age_days(e)
    cls = "stale" if is_stale(e) else "fresh"
    against = ", ".join(e.get("checked_against") or []) or "—"
    upstream = (f"\n      <div><dt>Upstream pushed</dt>"
                f"<dd>{html.escape(fmt_date(e.get('upstream_pushed')))}</dd></div>"
                if e.get("upstream_pushed") else "")
    link = (f'<a class="ext" href="{html.escape(e["url"])}" rel="noopener">'
            f'{html.escape(e["url"])}</a>' if e.get("url") else "")
    note = (f'<p class="notice">I have not re-checked this in over {STALE_AFTER_DAYS} days. It '
            'may well still be right — I just haven\'t confirmed it lately.</p>'
            if is_stale(e) else "")

    src = ""
    if e.get("source"):
        p = ROOT / e["source"]
        files = sorted(p.rglob("*")) if p.is_dir() else [p]
        blocks = []
        for f in files:
            if f.is_dir() or f.suffix not in (".md", ".json", ".yaml", ".yml", ".toml", ".sh", ".py"):
                continue
            rel = f.relative_to(ROOT)
            body = f.read_text(encoding="utf-8", errors="replace")
            blocks.append(f'<h3 class="srcname">{html.escape(str(rel))}</h3>'
                          f"<pre><code>{html.escape(body)}</code></pre>")
        if blocks:
            src = ('<section class="source"><h2>The files</h2>'
                   '<p class="blurb">Copy these straight into your setup.</p>'
                   + "\n".join(blocks) + "</section>")

    gtitle = dict(GROUPS).get(e.get("group"), "")
    body = f"""<article class="entry">
  <div class="wrap narrow">
    <p class="crumb"><a href="../../">{html.escape(SITE_NAME)}</a> &rsaquo;
       <a href="../../#{e.get('group')}">{html.escape(gtitle)}</a></p>
    <h1>{html.escape(e.get('name',''))}{' <span class="pill mine">mine</span>' if e.get('mine') else ''}</h1>
    <p class="lede">{html.escape(e.get('what',''))}</p>
    <dl class="facts">
      <div><dt>Kind</dt><dd>{html.escape(str(e.get('kind','')))}</dd></div>
      <div><dt>Last checked</dt><dd class="{cls}">{html.escape(fmt_date(e.get('last_checked')))}</dd></div>
      <div><dt>Checked against</dt><dd>{html.escape(against)}</dd></div>{upstream}
    </dl>
    {link}
    {note}
    <div class="prose">
{render_md(e.get('_body',''), shift=1)}
    </div>
  </div>
  {f'<div class="wrap narrow">{src}</div>' if src else ''}
</article>"""
    jsonld = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"TechArticle",
"headline":{_j(e.get('name',''))},"description":{_j(e.get('what',''))},
"dateModified":{_j(str(e.get('last_checked','')))},
"author":{{"@type":"Person","name":{_j(AUTHOR)}}}}}
</script>
"""
    return page(f"{e.get('name','')} — {SITE_NAME}",
                f"{e.get('what','')} Last checked {fmt_date(e.get('last_checked'))} "
                f"against {against}.",
                body, f"e/{e['_slug']}", jsonld)


def _j(s):
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def build_readme(items):
    intro = ROOT / "_intro.md"
    parts = [intro.read_text(encoding="utf-8").rstrip() if intro.exists() else f"# {SITE_NAME}", ""]
    for key, title in GROUPS:
        b = sorted([e for e in items if e.get("group") == key],
                   key=lambda x: str(x.get("name", "")).lower())
        if not b:
            continue
        parts += [f"## {title}", ""]
        parts += ["| | What | Last checked |", "|---|---|---|"]
        for e in b:
            name = e.get("name", "")
            target = e.get("url") or (e.get("source") or "")
            link = f"[{name}]({target})" if target else name
            parts.append(f"| **{link}**{' &middot; mine' if e.get('mine') else ''} | "
                         f"{e.get('what','')} | {fmt_date(e.get('last_checked'))}"
                         f"{' &#9888;' if is_stale(e) else ''}"
                         f"<br><sub>{', '.join(e.get('checked_against') or []) or '—'}</sub> |")
        parts.append("")
    stale_n = sum(1 for e in items if is_stale(e))
    parts += ["---", "",
              "**How to read the dates.** `Last checked` is the day I personally confirmed the "
              "entry still works, against the versions beneath it — a machine never writes that "
              f"date. &#9888; means it's more than {STALE_AFTER_DAYS} days old: the entry may "
              "still be right, I just haven't confirmed it lately. I re-check in bursts and "
              "promise no schedule, which is exactly why the date is shown.", "",
              f"<sub>{len(items)} {'entry' if len(items)==1 else 'entries'}, {stale_n} overdue. "
              f"Generated by `build.py` on {datetime.date.today().isoformat()}. "
              "Don't edit this file by hand.</sub>", ""]
    return "\n".join(parts)


def build_site(items):
    SITE.mkdir(exist_ok=True)
    for old in SITE.glob("e/*"):
        shutil.rmtree(old, ignore_errors=True)
    (SITE / "index.html").write_text(build_index(items), encoding="utf-8")
    urls = [f"{SITE_URL}/"]
    for e in items:
        d = SITE / "e" / e["_slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(build_entry(e), encoding="utf-8")
        urls.append(f"{SITE_URL}/e/{e['_slug']}/")
    today = datetime.date.today().isoformat()
    (SITE / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls)
        + "</urlset>\n", encoding="utf-8")
    (SITE / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")


def main():
    args = sys.argv[1:]
    if not ENTRIES.exists():
        print("no entries/ directory"); return 1
    items = entries()
    if args and args[0] == "--check":
        return cmd_check(items)
    if args and args[0] == "--sync":
        return cmd_sync(items)
    if args and args[0] == "--drift":
        return cmd_drift(items)
    if args and args[0] == "--stale":
        return cmd_stale(items, int(args[1]) if len(args) > 1 else STALE_AFTER_DAYS)

    cmd_check(items)
    (ROOT / "README.md").write_text(build_readme(items), encoding="utf-8")
    build_site(items)
    print(f"→ README.md · site/index.html · {len(items)} entry pages · sitemap.xml")
    if args and args[0] == "--serve":
        import http.server, socketserver, functools, os
        os.chdir(SITE)
        h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(SITE))
        print("http://localhost:8000  (ctrl-c to stop)")
        socketserver.TCPServer(("", 8000), h).serve_forever()
    return 0


if __name__ == "__main__":
    sys.exit(main())

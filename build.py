#!/usr/bin/env python3
"""Build the hub: README.md + a static, SEO-friendly site from entries/*.md

Stdlib only, on purpose — no install step, nothing to rot in six months.

    python3 build.py            build README.md + site/
    python3 build.py --stale    what's overdue for a re-check
    python3 build.py --check    validate entries, exit 1 on problems
    python3 build.py --serve    build, then serve site/ on :8000
"""
import sys, re, html, datetime, pathlib, shutil

ROOT = pathlib.Path(__file__).parent
ENTRIES, LIBRARY, SITE = ROOT / "entries", ROOT / "library", ROOT / "site"

# Set this before the first deploy — it drives canonical URLs and sitemap.xml.
SITE_URL = "https://ai-hub.pages.dev"
SITE_NAME = "AI Hub"
AUTHOR = "Serhii Leniv"
TAGLINE = ("The AI tooling I actually run — plus what I tried and dropped. "
           "Every entry says when I last checked it, and against which versions.")

STALE_AFTER_DAYS = 90
VERDICTS = ("using", "dropped", "watching")
KINDS = ("skill", "mcp", "config", "workflow", "tool", "model", "prompt")
REQUIRED = ("name", "what", "kind", "verdict", "last_checked")

BUCKETS = [
    ("using", "Using", "Tools and configs I actually run day to day."),
    ("dropped", "Dropped", "Tried these and stopped. Everyone publishes recommendations; "
                           "almost nobody publishes what they abandoned — so this is usually "
                           "the most useful section here."),
    ("watching", "Watching", "Looks promising, not properly tried yet. No verdict."),
]


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
        if e.get("verdict") not in VERDICTS:
            problems.append(f"{e['_file']}: verdict '{e.get('verdict')}' not in {VERDICTS}")
        if e.get("kind") not in KINDS:
            problems.append(f"{e['_file']}: kind '{e.get('kind')}' not in {KINDS}")
        if as_date(e.get("last_checked")) is None:
            problems.append(f"{e['_file']}: last_checked must be YYYY-MM-DD")
        if not e.get("checked_against"):
            problems.append(f"{e['_file']}: checked_against is empty — an undated claim is the "
                            "one thing this project exists not to publish")
        if e.get("verdict") == "dropped" and len(e.get("_body", "")) < 200:
            problems.append(f"{e['_file']}: 'dropped' with a thin explanation — that paragraph "
                            "is the entire value of the entry")
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
def page(title, desc, body, path, extra_head=""):
    """path is the site-relative directory, '' for the root."""
    canonical = f"{SITE_URL}/{path}".rstrip("/") + ("/" if path else "")
    depth = "../" * (len(pathlib.PurePath(path).parts)) if path else ""
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
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{depth}style.css">
{extra_head}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site">
  <div class="wrap">
    <a class="brand" href="{depth or '/'}">{html.escape(SITE_NAME)}</a>
    <nav><a href="{depth or '/'}#using">Using</a><a href="{depth or '/'}#dropped">Dropped</a><a href="{depth or '/'}#watching">Watching</a></nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site">
  <div class="wrap">
    <p><strong>Why the dates.</strong> Every <em>awesome-</em> list is undated, so within months
       you can't tell what still works. A date you can weigh beats a recommendation you can't.</p>
    <p><strong>No schedule.</strong> I re-check in bursts. An entry marked overdue may still be
       right — I just haven't confirmed it lately, and I'd rather say so than hide it.</p>
    <p class="fine">{html.escape(AUTHOR)} · built {datetime.date.today().strftime('%-d %B %Y')}</p>
  </div>
</footer>
</body>
</html>
"""


def card(e, depth=""):
    a = age_days(e)
    cls = "stale" if is_stale(e) else "fresh"
    mine = '<span class="mine" title="I built this">★</span>' if e.get("mine") else ""
    against = html.escape(", ".join(e.get("checked_against") or []) or "—")
    return f"""      <a class="card" href="{depth}e/{e['_slug']}/">
        <h3>{html.escape(e.get('name',''))} {mine}</h3>
        <p class="what">{html.escape(e.get('what',''))}</p>
        <p class="meta"><span class="kind">{html.escape(e.get('kind',''))}</span>
          <span class="date {cls}">checked {html.escape(fmt_date(e.get('last_checked')))}</span></p>
        <p class="against">{against}</p>
      </a>"""


def build_index(items):
    stale_n = sum(1 for e in items if is_stale(e))
    mine_n = sum(1 for e in items if e.get("mine"))
    hero = f"""<section class="hero">
  <div class="wrap">
    <h1>The AI tooling I actually run<br><span>— and what I dropped.</span></h1>
    <p class="tag">Skills, agent configs, MCP servers and workflows, each one dated and checked
       against named tool and model versions. Nothing here that I haven't personally used.</p>
    <p class="stats"><span class="pill">{len(items)} {'entry' if len(items)==1 else 'entries'}</span>
       <span class="pill">{mine_n} built by me</span>
       <span class="pill{' warn' if stale_n else ''}">{stale_n} overdue</span></p>
  </div>
</section>"""
    secs = []
    for verdict, title, blurb in BUCKETS:
        b = sorted([e for e in items if e.get("verdict") == verdict],
                   key=lambda x: str(x.get("name", "")).lower())
        cards = "\n".join(card(e) for e in b) or '      <p class="empty">Nothing here yet.</p>'
        secs.append(f"""<section id="{verdict}" class="bucket">
  <div class="wrap">
    <h2>{title} <span class="count">{len(b)}</span></h2>
    <p class="blurb">{blurb}</p>
    <div class="grid">
{cards}
    </div>
  </div>
</section>""")
    return page(f"{SITE_NAME} — AI skills, workflows and configs, dated and checked",
                TAGLINE, hero + "\n" + "\n".join(secs), "")


def build_entry(e):
    a = age_days(e)
    cls = "stale" if is_stale(e) else "fresh"
    against = ", ".join(e.get("checked_against") or []) or "—"
    link = (f'<a class="ext" href="{html.escape(e["url"])}" rel="noopener">'
            f'{html.escape(e["url"])}</a>' if e.get("url") else "")
    note = ('<p class="notice">I have not re-checked this in over 90 days. It may well still be '
            'right — I just haven\'t confirmed it lately.</p>' if is_stale(e) else "")

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

    body = f"""<article class="entry">
  <div class="wrap narrow">
    <p class="crumb"><a href="../../">{html.escape(SITE_NAME)}</a> ›
       <a href="../../#{e.get('verdict')}">{html.escape(str(e.get('verdict','')).title())}</a></p>
    <h1>{html.escape(e.get('name',''))}</h1>
    <p class="lede">{html.escape(e.get('what',''))}</p>
    <dl class="facts">
      <div><dt>Verdict</dt><dd class="v-{e.get('verdict')}">{html.escape(str(e.get('verdict','')))}</dd></div>
      <div><dt>Kind</dt><dd>{html.escape(str(e.get('kind','')))}</dd></div>
      <div><dt>Last checked</dt><dd class="date {cls}">{html.escape(fmt_date(e.get('last_checked')))}</dd></div>
      <div><dt>Checked against</dt><dd>{html.escape(against)}</dd></div>
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
                f"{e.get('what','')} Verdict: {e.get('verdict')}. "
                f"Last checked {fmt_date(e.get('last_checked'))} against {against}.",
                body, f"e/{e['_slug']}", jsonld)


def _j(s):
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def build_readme(items):
    intro = ROOT / "_intro.md"
    parts = [intro.read_text(encoding="utf-8").rstrip() if intro.exists() else f"# {SITE_NAME}", ""]
    for verdict, title, blurb in BUCKETS:
        b = sorted([e for e in items if e.get("verdict") == verdict],
                   key=lambda x: str(x.get("name", "")).lower())
        parts += [f"## {title} ({len(b)})", "", blurb, ""]
        if not b:
            parts += ["_Nothing here yet._", ""]
            continue
        parts += ["| | What | Kind | Last checked |", "|---|---|---|---|"]
        for e in b:
            name = e.get("name", "")
            target = e.get("url") or (e.get("source") or "")
            link = f"[{name}]({target})" if target else name
            parts.append(f"| **{link}**{' ★' if e.get('mine') else ''} | {e.get('what','')} | "
                         f"`{e.get('kind','')}` | {fmt_date(e.get('last_checked'))}"
                         f"{' ⚠️' if is_stale(e) else ''}"
                         f"<br><sub>{', '.join(e.get('checked_against') or []) or '—'}</sub> |")
        parts.append("")
    stale_n = sum(1 for e in items if is_stale(e))
    parts += ["---", "",
              f"**{len(items)} {'entry' if len(items)==1 else 'entries'} · {stale_n} overdue for "
              f"a re-check.** ⚠️ means the date is more than {STALE_AFTER_DAYS} days old — the "
              "entry may still be right, but I haven't confirmed it lately. That's the point of "
              "showing the date.", "",
              f"<sub>Generated by `build.py` on {datetime.date.today().isoformat()}. "
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

# Deploy

Two surfaces, both free, one repo. Nothing here costs money per visitor.

## 1. Set the URL first

`build.py` has `SITE_URL` near the top. It drives canonical tags and `sitemap.xml` — both
matter for Google. Set it before the first deploy, then rebuild.

```python
SITE_URL = "https://ai-hub.pages.dev"     # or your domain, later
```

## 2. GitHub — the repo

For this audience the repo *is* the product: stars, issues, `git clone`. `README.md` is
generated and renders as the hub on the repo front page.

```bash
gh repo create ai-hub --public --source=. --push
```

Then enable **Issues**. That's the whole feedback mechanism — `notes/PLAN.md` milestone 4 is a
stranger opening one.

## 3. Cloudflare Pages — the site

`site/` is **committed**, so Pages needs no build step and nothing breaks when a build image
changes Python versions.

**Dashboard route** (easiest, no CLI):

1. Cloudflare → Workers & Pages → Create → Pages → Connect to Git
2. Pick the repo. **Build command:** leave empty. **Output directory:** `site`
3. Deploy → you get `<project>.pages.dev` in about a minute

**CLI route:**

```bash
npx wrangler login          # opens a browser — run this yourself
npx wrangler pages deploy site --project-name=ai-hub
```

Every push redeploys. No account system, no database, no functions.

## 4. Domain — later

Not until `notes/PLAN.md` milestone 2. When you do: register **at Cloudflare** (cost price,
~$12/yr, no second-year markup), then Pages → Custom domains. HTTPS is automatic. Update
`SITE_URL`, rebuild, push.

## 5. Getting found

Already handled by the build: per-entry pages at `/e/<slug>/`, canonical URLs, OG tags,
`TechArticle` JSON-LD with `dateModified`, `sitemap.xml`, `robots.txt`.

What's left to you, once there are real entries:

- Submit `sitemap.xml` in Google Search Console.
- **The per-entry pages are what rank.** "does <tool> still work", "<tool> vs <tool>", and
  "why I stopped using <tool>" are queries with real volume and almost no honest answers.
  The `dropped` entries are the strongest SEO asset here for exactly that reason.

## The working loop

```bash
python3 build.py --stale     # what's overdue — start a burst here
# re-check, edit entries/, bump last_checked + checked_against
python3 build.py --check     # gate: fails empty checked_against, thin 'dropped' text
python3 build.py             # regenerate README.md + site/
python3 build.py --serve     # preview on localhost:8000
git commit -am "Re-check pass" && git push
```

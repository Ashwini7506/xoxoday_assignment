# xoxoday_assignment

SEO & AEO audit and page rebuild for two Xoxoday pages — Consumer Goods landing page and Medical Devices blog post.

## What's In This Repo

### Rebuilt Pages
| File | Description |
|------|-------------|
| `consumer-goods-rebuilt.html` | Rebuilt Consumer Goods landing page — corrected meta tags, Service schema, FAQ section, comparison table, full OG/Twitter tags |
| `xoxoday-rebuilt.html` | Rebuilt Medical Devices blog post — corrected schema, BlogPosting type, fixed author entity, question-format headings, Xoxoday brand design |

### Audit Report
| File | Description |
|------|-------------|
| `SEO-AUDIT-REPORT.md` | Full SEO + AEO audit — verified findings from raw HTML, before/after comparison, scoring logic, expected impact |

### Visual Evidence
| File | Description |
|------|-------------|
| `screenshots/problems-report.html` | Interactive report showing every code problem with actual bad HTML (red) and correct fix (green) |
| `screenshots/problems-cg.png` | Consumer Goods page code problems — screenshot |
| `screenshots/problems-blog.png` | Blog post code problems — screenshot |
| `screenshots/problems-full-page.png` | All 17 problems in one full-page view |
| `screenshots/consumer-goods-desktop.png` | Consumer Goods rebuilt page — desktop render |
| `screenshots/consumer-goods-mobile.png` | Consumer Goods rebuilt page — mobile render |
| `screenshots/blog-desktop.png` | Blog rebuilt page — desktop render |
| `screenshots/blog-mobile.png` | Blog rebuilt page — mobile render |

### SEO Skills
All skills used for this audit, plus two new ones created during this project:

| Skill | Purpose |
|-------|---------|
| `skills/seo/` | Master skill — orchestrates all sub-skills |
| `skills/seo-technical/` | Technical SEO — crawlability, indexability, security, Core Web Vitals |
| `skills/seo-content/` | Content quality — E-E-A-T, readability, thin content, AI citation readiness |
| `skills/seo-geo/` | GEO / AI Search Optimization — AI Overviews, ChatGPT, Perplexity citability |
| `skills/seo-page/` | Single-page deep analysis — on-page SEO, schema, images, CWV flags |
| `skills/seo-humanize/` | **New** — Content humanization and readability — rewrites AI/corporate copy into plain human English |
| `skills/seo-design/` | **New** — SEO design audit — brand tokens, visual hierarchy, CTA placement, mobile, above-the-fold |

## Pages Audited

| Page | URL | Original Score | Rebuilt Score |
|------|-----|---------------|---------------|
| Consumer Goods | `xoxoday.com/industry/consumer-goods` | SEO: 32/100, AEO: 18/100 | SEO: 74/100, AEO: 71/100 |
| Medical Devices Blog | `blog.xoxoday.com/medical-devices-home-healthcare-loyalty-engagement/` | SEO: 34/100, AEO: 28/100 | SEO: 68/100, AEO: 58/100 |

## Key Problems Found

### Consumer Goods Page
- Meta description says "insurance" — copied from wrong page
- Title is 33 chars, missing brand name
- H1 is just "Consumer Goods" — 2 words
- All 211 images have `alt=""` (empty)
- Schema type is WebPage, not Service
- Meta description attributes in reverse order — hidden from most tools

### Blog Post
- Title 69 chars — truncated in Google SERPs
- Same H2 heading appears twice
- Author URL points to `/404/`
- `twitter:site = @ghost` — CMS default never updated
- jQuery loaded 3 times (3 different versions)
- Tailwind CDN loads 4MB of unused CSS
- `maximum-scale=1` blocks mobile zoom

## Skills Used

This project used the [claude-seo plugin](https://github.com/agricidaniel/claude-seo) skill framework:
- `/seo technical` — 9-category technical audit
- `/seo content` — E-E-A-T and content quality
- `/seo geo` — AI search readiness (GEO)
- `/seo page` — on-page SEO deep dive
- `/seo-humanize` — content humanization (new)
- `/seo-design` — design and brand consistency (new)

## Scoring Methodology

| Category | Weight |
|----------|--------|
| Technical | 22% |
| Content Quality | 23% |
| On-Page SEO | 20% |
| Schema | 10% |
| Performance / CWV | 10% |
| AI Search Readiness | 10% |
| Images | 5% |

AEO scores: Citability 25% · Structural Readability 20% · Multi-Modal 15% · Authority 20% · Technical AI Accessibility 20%

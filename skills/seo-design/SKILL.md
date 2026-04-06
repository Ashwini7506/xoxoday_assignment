---
name: seo-design
description: >
  SEO-focused design and visual hierarchy analysis. Audits page design for brand
  consistency, typography, spacing, CTA placement, above-the-fold content, and
  visual signals that affect dwell time, bounce rate, and AI citation readiness.
  Also rebuilds HTML pages to match a brand's design system.
  Use when user says "design audit", "brand consistency", "visual hierarchy",
  "redesign", "rebuild page", "fix the design", "brand tokens", or "CSS audit".
user-invokable: true
argument-hint: "[url or file path] [brand reference file (optional)]"
license: MIT
metadata:
  author: Ashwini
  version: "1.0.0"
  category: seo
---

# SEO Design Audit & Rebuild

## Why Design Is an SEO Signal

Google does not rank pages based on their looks — but design directly drives the
behavioral signals Google does measure:

| Design Problem | SEO/UX Impact |
|---------------|---------------|
| Wrong brand colors, mismatched fonts | Bounce rate increase (user distrust) |
| No visual hierarchy (all text same size) | Low dwell time, poor content scannability |
| CTA buried below fold | Zero conversions; low engagement signal |
| Images missing width/height | CLS (Cumulative Layout Shift) penalty |
| Mobile font < 16px | Mobile usability score drop |
| Touch targets < 48px | Core Web Vitals INP penalty |
| Dark background + light text without contrast check | Accessibility failure, lower dwell |
| No whitespace between sections | Cognitive load increase, early exit |

**Design signals that directly affect AI Overviews and GEO:**
- Content in a visually isolated block (card or callout) with a clear heading
  is 2.7× more likely to be cited by AI systems
- Tables, comparison grids, and numbered lists are the top 3 most-cited formats
  in Google AI Overviews
- Above-the-fold content clarity (does the user immediately understand the page?)
  affects whether AI extracts the right summary

---

## Brand Token System (Required Before Any Rebuild)

Before auditing or rebuilding a page, extract the brand's design tokens.

### How to Extract Brand Tokens

1. Inspect the brand's main website (homepage or product pages)
2. Read CSS custom properties in `:root {}` or equivalent
3. Extract: primary colors, secondary colors, background colors, text colors, border radius, font stacks

### Xoxoday Brand Tokens (Reference Implementation)

```css
:root {
  /* Colors */
  --navy:   #041a2f;   /* Primary dark — headlines, nav, footer */
  --blue:   #035bff;   /* Action color — CTAs, links, active states */
  --orange: #f5a623;   /* Accent — badges, highlights, hover states */

  /* Backgrounds */
  --bg:     #ffffff;   /* Page background */
  --bg-lt:  #f6f7f9;   /* Section alternating background */

  /* Text */
  --text:   #041a2f;   /* Body text (same as navy) */
  --text-2: #394960;   /* Secondary text */
  --text-3: #798099;   /* Captions, metadata, dates */

  /* Borders */
  --border: #e2e6ed;   /* Dividers, card borders, input borders */

  /* Radius */
  --r-pill: 100px;     /* Pill badges, full-round buttons */
  --r-card: 12px;      /* Cards, modals, image containers */
  --r-sm:   8px;       /* Small elements, inputs, tags */

  /* Typography */
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
}
```

### Colored-Dots Wordmark (Xoxoday-specific)

The Xoxoday logo in HTML contexts uses colored letters, not an image SVG:

```html
<a href="/" class="xo-logo">
  X<span class="dot-r">o</span>x<span class="dot-o">o</span>d<span class="dot-b">a</span>y
</a>
```

```css
.xo-logo       { font-weight: 700; font-size: 1.5rem; color: var(--navy); letter-spacing: -.02em; }
.xo-logo .dot-r { color: #e63946; }   /* red o */
.xo-logo .dot-o { color: var(--orange); }  /* orange o */
.xo-logo .dot-b { color: var(--blue); }    /* blue a */
```

---

## Design Audit Categories

### 1. Brand Consistency (25%)

**Check for:**
- Color values match the brand's defined palette (hex-exact, not approximate)
- Font family matches brand guidelines (Inter for Xoxoday, not system sans-serif fallback)
- Logo implementation: wordmark vs SVG vs icon — matches brand usage rules
- Header and footer match the live brand site exactly
- No legacy design system tokens mixed in (e.g., zinc-gray shadcn tokens on a navy brand)

**Common failures:**
- Tailwind zinc grays (`#09090b`, `#f4f4f5`, `#71717a`) left in place on a brand-colored page
- Radius values (`1.5rem` rounded corners) from a generic template, not the brand's `12px` card radius
- Hero button using `btn-primary` (black) instead of brand `btn-navy` or `btn-blue`

### 2. Visual Hierarchy (25%)

**Check for:**
- H1 is visually the largest element on the page (not overridden by a decorative element)
- H2s have a consistent step-down in size from H1 (minimum 4px difference)
- H3s are visually subordinate to H2s
- Body text is 16px minimum, line-height 1.6 minimum
- Section headers are visually distinct from body copy (weight, size, or color change)
- No two elements compete equally for attention in the same viewport area

**Visual hierarchy score map:**
| Level | Suggested size | Weight |
|-------|---------------|--------|
| H1 | 40–52px | 700–800 |
| H2 | 28–36px | 600–700 |
| H3 | 20–24px | 600 |
| Body | 16–18px | 400 |
| Caption/meta | 13–14px | 400, color: --text-3 |

### 3. Above-the-Fold Content (20%)

The first viewport (typically 700–900px height on desktop) must answer:
1. **What is this page?** — clear H1
2. **Who is it for?** — named audience in first sentence or subheading
3. **What do I get?** — outcome or value proposition
4. **What do I do next?** — one primary CTA, visually prominent

**Failures:**
- Hero image takes up 70%+ of viewport with no text (user cannot extract value without scrolling)
- CTA is below a long paragraph of body text
- Subheadline is in `--text-3` (too light) — not readable on mobile
- Social proof (logos, testimonials) placed above the value proposition

### 4. CTA Design & Placement (15%)

**Primary CTA rules:**
- One primary CTA per viewport section (not three competing buttons)
- Primary button: filled, brand action color (`--blue` for Xoxoday), minimum 48px height
- Ghost/secondary button: border only, used for secondary actions
- CTA copy: verb-first ("Get a Demo", "See Pricing", "Start Free") — not "Click Here" or "Learn More"
- CTA must be visible without scrolling on desktop AND mobile

**Button style reference:**
```css
.btn-navy  { background: var(--navy); color: #fff; }
.btn-blue  { background: var(--blue); color: #fff; }
.btn-ghost { background: transparent; border: 1.5px solid var(--border); color: var(--text); }
```

### 5. Spacing & Whitespace (10%)

**Section spacing:**
- Minimum 80px vertical padding between major sections
- Cards: 24px internal padding minimum
- Between heading and body copy: 12–16px gap
- Between list items: 8–12px gap
- No content flush against viewport edge (minimum 16px horizontal padding on mobile)

**Spacing scale (8px base grid):**
```
4px  — icon-to-label gap
8px  — tight spacing (badge padding, list item gap)
12px — form field internal padding
16px — card padding (mobile), paragraph gap
24px — card padding (desktop), section sub-spacing
32px — component gap within section
48px — between heading and content group
80px — section vertical padding
```

### 6. Mobile Responsiveness (5%)

**Check for:**
- Viewport meta: `width=device-width, initial-scale=1` — no `maximum-scale=1`
- Font size: minimum 16px body (no override to 14px or smaller)
- Touch targets: minimum 48×48px with 8px gap between targets
- No horizontal overflow (tables, code blocks, images wider than viewport)
- Navigation: hamburger menu or stacked nav on < 768px
- Images: `max-width: 100%` on all img elements
- Cards: stack to single column on < 640px

---

## Rebuild Workflow (When Asked to Redesign a Page)

1. **Extract brand tokens** from reference URL or design file
2. **Audit current CSS variables** — identify legacy/wrong values
3. **Replace CSS block entirely** — do not patch variable by variable
4. **Update header HTML** — logo, nav links, CTA buttons
5. **Update footer HTML** — logo, link columns, legal text
6. **Replace button classes** — map old classes to brand classes
7. **Replace SVG inline colors** — use sed to replace hex values in embedded SVGs
8. **Verify visual hierarchy** — H1 > H2 > H3 > body visually
9. **Check above-the-fold** — value prop visible without scroll
10. **Mobile check** — render at 375px, 768px, 1280px

### SVG Color Replacement (sed commands)

When a brand switches from a dark/generic template to a light brand palette:

```bash
# Replace zinc grays with Xoxoday tokens
sed -i '' 's/#09090b/#041a2f/g' page.html    # fg → navy
sed -i '' 's/#f4f4f5/#f6f7f9/g' page.html    # muted bg → bg-lt
sed -i '' 's/#3f3f46/#394960/g' page.html    # muted-fg → text-2
sed -i '' 's/#71717a/#798099/g' page.html    # muted-fg-2 → text-3
sed -i '' 's/#e4e4e7/#e2e6ed/g' page.html    # border → border
```

---

## Design Score Card

```
Overall Design Score: XX/100

Brand Consistency:     XX/25  ████████░░░░░░░░░░░░░░░░░
Visual Hierarchy:      XX/25  ████████░░░░░░░░░░░░░░░░░
Above-the-Fold:        XX/20  ████████░░░░░░░░░░░░
CTA Design:            XX/15  ████████░░░░░░░
Spacing/Whitespace:    XX/10  ████████░░
Mobile:                XX/5   █████
```

### Issues Found
Critical → High → Medium → Low

### CSS Fixes
Exact variable replacements, ready to paste.

### HTML Fixes
Specific markup changes for header, footer, buttons.

---

## Quick Wins

1. Replace wrong color hex values in CSS `:root {}`
2. Fix button classes to use brand action color
3. Add `max-width: 100%` to all images missing it
4. Remove `maximum-scale=1` from viewport meta
5. Increase body `line-height` to 1.6 if below

## Medium Effort

1. Rebuild header with correct brand logo and nav
2. Standardize H1/H2/H3 sizing to visual hierarchy scale
3. Add 80px section padding to sections flush against each other
4. Make all CTAs verb-first copy

## High Impact

1. Full CSS variable replacement (template tokens → brand tokens)
2. Mobile-first layout rebuild (single column base, responsive up)
3. Above-the-fold redesign: H1 + subtext + CTA visible without scroll
4. Replace inline SVG colors to match brand palette

---

## Error Handling

| Scenario | Action |
|----------|--------|
| No brand reference provided | Extract tokens from the live brand homepage. Ask user to confirm before applying. |
| File is minified CSS (unreadable) | Flag minification. Extract readable variables only. Suggest unminifying before full audit. |
| Page uses a CSS framework (Tailwind, Bootstrap) | Identify framework version. Audit for brand overrides. Check if utility classes conflict with brand tokens. |
| SVG logo is raster (PNG/JPG) | Flag: recommend SVG. Check alt text and display size. |
| Design uses images for text (text in JPG/PNG) | Flag as accessibility and SEO failure — screen readers and Google cannot read image-text. |

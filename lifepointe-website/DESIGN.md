# Lifepointe Website Prototype — Design System

Prototype replacement for lifepointechiropractic.com. Static HTML/CSS/JS, no build step
required to serve — but the pages are generated (see Regenerating below) so the shared
chrome stays identical across all seven.

## Concept
The page's structural device is the subject itself: **alignment**. A vertical "spine rail"
runs down the content gutter with one vertebra node per section; nodes light gold as each
section enters view (IntersectionObserver; static without JS; motion killed by
`prefers-reduced-motion`). "Lifepointe" = points along a line. Everything else stays quiet
so the one signature element carries the design.

## Tokens
| Token | Value | Use |
|---|---|---|
| --ink | #24283f | headings, body on light |
| --ink-soft | #565b76 | secondary text |
| --navy | #3d437c | primary brand, hero/CTA fills, links |
| --navy-ink | #2c3160 | footer + large dark fills, text on gold |
| --indigo | #545da8 | hover states, eyebrows, focus ring on light |
| --gold | #fec741 | primary CTA, rail nodes, on-dark accents (eyebrows, focus ring, step numerals), small wayfinding marks (active-nav underline, quote marks) |
| --gold-deep | #f5b64a | gold CTA hover |
| --paper | #f7f8fc | page background (cool, from brand #edf0f5) |
| --card | #ffffff | raised surfaces |
| --line | #dfe3f0 | borders, the rail |
| --navy-muted / --navy-link / --navy-faint | #c9cfe8 / #e6e9f7 / #9aa3d0 | text tiers on navy fills |
| --indigo-tint | #eef0f9 | hover wash, icon chips |
| --header-h | 76px | header height; drives scroll-padding + sticky offsets |

Logo red and green stay in the logo. No red or green UI in healthcare.

## Type
- Display: **Bricolage Grotesque** 700/800 — `.display-1` (home h1) > `.display-page`
  (interior h1) > `.display-2` (section h2) > `.display-3` (card h3)
- Body/UI: **Lato** 400/700, 17px, 1.65 line-height
- Eyebrow: Lato 700, 12px, +.17em tracking, uppercase — indigo on light, gold on dark

## Rhythm
Post-heading gap `.mt-15` (1.5rem); pre-CTA / group gap `.mt-2` (2rem). No other inline
spacing — new one-offs should become classes.

## Pages
index, about, services, new-patients, success-stories, recipe-book, contact — the real IA
of the live site, real extracted copy only (testimonials verified against the live pages).
Shared header (sticky, gold CTA → contact#appointment) + footer (navy-ink, white logo).
The closing CTA band is shared verbatim on five pages; new-patients tailors it ("Ready for
your first visit?") and contact omits it — deliberate: never CTA to the page you're on.

## Floor
Skip link + `scroll-padding-top` clearing the sticky header, landmarks, aria-current nav,
focus-visible everywhere (gold on dark), AA contrast, reduced-motion kills all animation,
mobile nav = button + aria-expanded + focus-scoped Escape, hours table marks "(today)" for
screen readers, no horizontal scroll at 320px. Hamburger below 1081px (the desktop bar
needs ~976px of content width).

## Regenerating
`python3 build.py` from this directory rewrites the seven HTML files. Edit page content in
build.py, shared styling in css/site.css, behavior in js/site.js. Screenshots need a
browser with system libs this WSL box lacks — test in a real browser.

## Known placeholders
- Ten success-story categories link out to the live site (marked ↗); five are on-page.

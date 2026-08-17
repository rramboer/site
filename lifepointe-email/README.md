# Lifepointe Chiropractic — HTML Email

`index.html` is a standalone, email-client-safe HTML template for Lifepointe Chiropractic and
Wellness Center. Open it in a browser to preview, or paste the source into your email platform
(Mailchimp, Constant Contact, Brevo, etc.) as a custom HTML campaign.

## What's in it
- 600px table-based layout, centered on a `#edf0f5` background
- Hidden preheader text (inbox preview line)
- Hero with a bulletproof VML/HTML button that renders in Outlook
- 2×2 services grid that stacks to one column under 600px
- Office hours + address/phone/email block
- Dark footer with social icons and a text-link fallback
- Unsubscribe / preferences links

## Logo files (`images/`)
| File | What it is |
|---|---|
| `lifepointe-logo.png` | 440×166, wordmark recolored to navy `#3d437c` — **used by the email** |
| `lifepointe-logo-white.png` | 1347×508, original artwork, white wordmark for dark backgrounds |
| `recolor-logo.py` | The Pillow script that produced the navy version, if you need to redo it |

The original logo was a WebP with a **white** wordmark, built for a dark background — invisible
on the email's white header, and WebP doesn't render in Outlook 2016–2021 on Windows anyway.
Both problems are solved: converted to PNG, and every white pixel in the wordmark and the family
figures recolored to navy. The red heart and the green banner (including its white
"& WELLNESS CENTER" text, which sits on green and needed to stay white) are untouched.

## Typography
Everything in the email uses one stack:
`'Lato', 'Helvetica Neue', Helvetica, Arial, sans-serif` — Lato being the typeface the website
itself runs on. Hierarchy comes from weight, size, and letter-spacing rather than a second
typeface, which is what keeps it looking like one designed piece instead of a template.

| Element | Size / line-height | Weight | Tracking |
|---|---|---|---|
| H1 (hero) | 33 / 41 | 900 | −0.5px |
| H2 (section) | 23 / 31 | 900 | −0.3px |
| Eyebrow labels | 11–12 | 700 | +1.2 to +2.5px, uppercase |
| Body | 15–16 / 25–26 | 400 | normal |
| Buttons | 16 | 700 | normal |

The heavy 900 headings deliberately echo the bold condensed wordmark in the logo. Lato loads via
Google Fonts for clients that support webfonts (Apple Mail, iOS, Outlook.com, Samsung); Gmail and
Outlook desktop fall back to Helvetica/Arial, which have close enough proportions that nothing
reflows. An `[if mso]` block forces Outlook desktop onto Arial so it never defaults to Times.

## Brand colors (pulled from lifepointechiropractic.com)
| Role | Hex |
|---|---|
| Primary navy | `#3d437c` |
| Secondary indigo | `#545da8` |
| Accent gold (CTA) | `#fec741` |
| Body text | `#474747` |
| Page background | `#edf0f5` |
| Footer | `#212121` |

## Before you send — three things to replace
1. **Logo — host it and use an absolute URL.** `images/lifepointe-logo.png` is referenced by a
   relative path so the file previews correctly in a browser. Email clients can't resolve
   relative paths — upload the PNG to your email platform's image host and replace the `src`
   with the full `https://` URL. Leave `width="220" height="83"` as-is.
2. **Social icons** (footer): currently hotlinked from flaticon's CDN. Self-host these —
   third-party CDNs can rate-limit or disappear, and self-hosted images look more trustworthy
   to spam filters. 60×60px PNGs displayed at 30×30.
3. **Unsubscribe links**: `{{UnsubscribeURL}}` and `{{PreferencesURL}}` are placeholders —
   replace with your platform's merge tags (Mailchimp uses `*|UNSUB|*`, Brevo uses
   `{{ unsubscribe }}`, etc.). CAN-SPAM requires a working unsubscribe on commercial email.

## Email best practices already applied
- Inline styles everywhere (Gmail strips `<style>` in some contexts; the `<style>` block only
  holds resets and media queries, which is the safe split)
- Tables for layout, no flexbox/grid, no external CSS or fonts
- One typeface throughout (see Typography below)
- Every image has `alt` text and the design still reads with images off
- `role="presentation"` on layout tables so screen readers skip them
- Apple/Gmail auto-link detection suppressed on the address and phone blocks
- Absolute URLs with `target="_blank"` on every link
- `tel:` and `mailto:` links for one-tap contact on mobile

## Testing
Send yourself a test before any real send. Gmail (web + iOS/Android), Outlook desktop, and
Apple Mail cover most of the audience. Litmus or Email on Acid will render all of them at once
if you want to be thorough.

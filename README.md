# CFT Apartments & Shops

Static website for **Cyabukombe Family Trading (CFT)** — furnished apartments and commercial shops for rent in Kimironko, Kigali, Rwanda.

**Live site:** https://cftproperty.rw/

## Pages

All pages are generated output — see [Development](#development) below before editing any `.html` file directly.

| File | Description |
|---|---|
| `index.html` | Home page — hero, "Why Choose CFT" feature grid, featured apartment/shop cards, guest testimonials, and a booking call-to-action. |
| `apartments.html` | Full apartment listings: a pricing/availability table for Inganji Estate rooms (Apartments 13, 14, 16, 18, 19), property cards for each bookable unit, and a photo gallery. |
| `apartment-vision-city.html` | Detail page for the Luxury 3BR apartment in Vision City — gallery, amenities, house rules, map, and an inquiry form. |
| `apartment-kimironko.html` | Detail page for **Inganji Apartment 19** (Kimironko) — same structure as the Vision City page. |
| `apartment-inganji.html` | Detail page for **Inganji Apartment 16** — same structure again, separate unit and photo set. |
| `shops.html` | Commercial shop listings at Imena Estate — current availability (Shop 9 / SH9), ideal tenant types, and an inquiry CTA. |
| `gallery.html` | Site-wide photo gallery across all properties, filterable by category. |
| `about.html` | Company background — who CFT is and how the business operates. |
| `contact.html` | Contact details, address, business hours, and a general inquiry form. |
| `booking.html` | General booking form covering any property/unit. |

## Project structure

```
build.py              Python script that generates every HTML page below from shared templates
css/styles.css         Stylesheet
js/main.js              Site behavior (nav, lightbox gallery, form handling)
images/                 Property photos
.github/workflows/build.yml   GitHub Actions: auto-runs build.py and commits the regenerated
                               HTML whenever build.py changes on main (see Development below)
```

## Development

**`build.py` is the only file you should hand-edit for content.** It holds:
- **Constants** at the top — `WA` (WhatsApp number), `PHONE`, `EMAIL`, `ADDRESS_LINE1/2`, the three `AIRBNB*` listing URLs, the Google `MAP` embed, and the `FORMSPREE` endpoint that inquiry forms submit to. Change these once here and they update everywhere they're used (footer, WhatsApp buttons, contact page, etc.).
- **`header()` / `FOOTER` / `shell()`** — the shared nav, footer, and page wrapper (meta tags, favicon, stylesheet) that every page is built from.
- **One `..._body` variable per page** (e.g. `home_body`, `apts_body`, `vc_body`, `km_body`, `ig_body`, `shops_body`) — the actual content of each page, passed into `shell()` and written out by a `write("page.html", ...)` call at the bottom of each section.

To make a change: edit the relevant constant or `_body` block in `build.py`, then regenerate:

```bash
python build.py
```

This overwrites all 10 HTML files from scratch. **Never edit the generated `.html` files directly** — any manual change to them is silently wiped out the next time `build.py` runs, since the HTML is fully regenerated every time, not merged.

### Automatic rebuilding

`.github/workflows/build.yml` runs `python build.py` automatically and commits the regenerated HTML whenever `build.py` is changed and pushed to `main` — including edits made directly in GitHub's web editor. You (or I) still need to run `python build.py` locally before pushing if you want to preview the result first, but it's no longer possible to push a `build.py` change without the site catching up.

## Deployment

Hosted on GitHub Pages, serving from the `main` branch root, with a custom domain (`cftproperty.rw`) configured via the `CNAME` file and DNS managed through Cloudflare.

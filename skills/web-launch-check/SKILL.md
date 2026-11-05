---
name: web-launch-check
description: "Pre-launch checklist for web apps covering build, performance, SEO, accessibility and security headers. Use before deploying a web app to production."
---

Check each item and report PASS / FAIL / N/A with evidence (file path or command output).

## Build
- Production build succeeds; no type or lint errors.
- Environment variables documented; no secrets exposed to the client bundle (e.g. only `NEXT_PUBLIC_*` / `VITE_*` are public by design).

## Performance
- Images sized and in modern formats; heavy routes/components lazy-loaded.
- Bundle size reasonable; no large unused dependencies.
- If a browser or Lighthouse is available, record LCP, CLS, INP.

## SEO and sharing
- Unique `<title>` and meta description per page, Open Graph tags, `robots.txt`, sitemap, canonical URLs.

## Accessibility
- Semantic landmarks, alt text, labeled form fields, keyboard navigation, visible focus, sufficient contrast.

## Security
- HTTPS; security headers (CSP, HSTS, X-Content-Type-Options, frame-ancestors / X-Frame-Options).
- Cookies `Secure`, `HttpOnly`, `SameSite` where applicable; CORS not `*` for authenticated APIs.
- Dependency audit run (`npm audit` or equivalent).

## Reliability
- Custom 404 / error pages; error monitoring configured; analytics consent respects privacy rules.

End with a go / no-go verdict and the list of FAIL items.

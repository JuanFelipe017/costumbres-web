---
name: webapp-testing
description: Test local web apps with Playwright - verify frontend behavior, debug UI, take screenshots and read browser console logs. Use after any visual or JS change to actually look at the result.
license: Apache-2.0 (adapted from anthropics/skills webapp-testing)
---

# Web Application Testing

Write native Python Playwright scripts. After building or changing UI, actually look at it (screenshots) instead of assuming it works.

## Serve the site

This project is static HTML. Serve it from the site folder:

```bash
cd Costumbres_Web && python -m http.server 8000
```
Run it in the background, wait until `http://localhost:8000` answers, and stop it when done.

## Script template

```python
from playwright.sync_api import sync_playwright

URL = "http://localhost:8000/index.html"
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    logs = []
    page.on("console", lambda m: logs.append(f"{m.type}: {m.text}"))
    page.on("pageerror", lambda e: logs.append(f"pageerror: {e}"))
    page.goto(URL)
    page.wait_for_load_state("networkidle")  # CRITICAL for JS / Tailwind CDN
    page.screenshot(path="shots/desktop.png", full_page=True)
    page.set_viewport_size({"width": 390, "height": 844})
    page.screenshot(path="shots/mobile.png", full_page=True)
    print("\n".join(logs) or "no console output")
    browser.close()
```

Then open the screenshots and check them.

## What to check

- Desktop (1440px) and mobile (390px) for every page touched, ES and EN.
- Horizontal scroll, overlapping or cut-off elements, broken images.
- Console errors.
- Mobile menu opens/closes; carousels advance.

## Pitfalls

- Wait for `networkidle` before inspecting the DOM.
- Prefer `text=`, `role=`, IDs, then CSS selectors.
- Always close the browser.
- If Playwright is missing: `pip install playwright` then `playwright install chromium`.

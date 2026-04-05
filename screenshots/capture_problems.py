from playwright.sync_api import sync_playwright

URL = "file:///Users/ashwinimishra/seo/screenshots/problems-report.html"

def get_abs_top(locator):
    """Return the element's top position relative to the document (not the viewport)."""
    return locator.evaluate(
        "el => el.getBoundingClientRect().top + window.scrollY"
    )

def get_abs_bottom(locator):
    """Return the element's bottom position relative to the document."""
    return locator.evaluate(
        "el => el.getBoundingClientRect().bottom + window.scrollY"
    )

def capture():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        page.goto(URL, wait_until="networkidle")

        # Total document height (needed for clipping)
        total_height = page.evaluate("document.body.scrollHeight")
        width = 1280

        # ── 1. Full-page desktop screenshot ───────────────────────────────
        page.screenshot(
            path="/Users/ashwinimishra/seo/screenshots/problems-full-page.png",
            full_page=True,
        )
        print("Saved: problems-full-page.png")

        # ── 2. Consumer Goods section (section header + first 4 problems) ─
        cg_header   = page.locator(".section-header").nth(0)
        cg_problems = page.locator(".problems").nth(0)
        first4      = cg_problems.locator(".problem")

        top_cg    = int(get_abs_top(cg_header))
        bottom_cg = int(get_abs_bottom(first4.nth(3))) + 24   # +24px padding

        page.screenshot(
            path="/Users/ashwinimishra/seo/screenshots/problems-cg.png",
            clip={"x": 0, "y": top_cg, "width": width, "height": bottom_cg - top_cg},
            full_page=True,
        )
        print("Saved: problems-cg.png")

        # ── 3. Blog section (section header + all blog problem cards) ─────
        blog_header    = page.locator(".section-header").nth(1)
        blog_problems  = page.locator(".problems").nth(1)
        blog_cards     = blog_problems.locator(".problem")
        blog_card_count = blog_cards.count()

        top_blog    = int(get_abs_top(blog_header))
        bottom_blog = int(get_abs_bottom(blog_cards.nth(blog_card_count - 1))) + 24

        page.screenshot(
            path="/Users/ashwinimishra/seo/screenshots/problems-blog.png",
            clip={"x": 0, "y": top_blog, "width": width, "height": bottom_blog - top_blog},
            full_page=True,
        )
        print("Saved: problems-blog.png")

        browser.close()
        print("\nAll screenshots captured successfully.")

if __name__ == "__main__":
    capture()

from playwright.sync_api import sync_playwright

def test_mvp_listing_displays_cards(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:8080")

    # Check if the grid exists
    grid = page.locator("#mvp-grid")
    if not grid.is_visible():
        raise Exception("Grid is not visible")

    # Check if cards are created (should be 1 initially based on index.html)
    cards = page.locator(".card")
    if cards.count() != 1:
        raise Exception(f"Expected 1 card, got {cards.count()}")

    # Verify card content
    first_card = cards.first
    if "Sample MVP" not in first_card.locator("h2").text_content():
         raise Exception("Card title does not match")
    if "A starter demo page" not in first_card.locator("p").text_content():
         raise Exception("Card description does not match")
    if "/mvps/sample-mvp/" not in first_card.locator("a").get_attribute("href"):
         raise Exception("Card link does not match")

    context.close()
    print("test_mvp_listing_displays_cards passed")

def test_empty_mvp_listing(browser):
    context = browser.new_context()
    page = context.new_page()

    # Intercept the request and return modified HTML
    def handle_route(route):
        response = route.fetch()
        body = response.text()
        # More robust replacement
        body = body.replace('const MVP_LIST = [', 'const MVP_LIST = []; const OLD_LIST = [')
        route.fulfill(body=body, content_type="text/html")

    page.route("**/", handle_route)
    page.goto("http://localhost:8080")

    # Wait for the script to execute and update the DOM
    page.wait_for_timeout(1000)

    # Log the innerHTML of the grid for debugging
    grid_html = page.locator("#mvp-grid").inner_html()
    print(f"Grid HTML: {grid_html}")

    # Check if the empty message is displayed
    empty_msg = page.locator("#mvp-grid .empty")
    if not empty_msg.is_visible():
         raise Exception(f"Empty message is not visible. Grid content: {grid_html}")

    if "No MVPs available yet" not in empty_msg.text_content():
        raise Exception("Empty message text does not match")

    # Ensure no cards are displayed
    cards = page.locator(".card")
    if cards.count() != 0:
        raise Exception(f"Expected 0 cards, got {cards.count()}")

    context.close()
    print("test_empty_mvp_listing passed")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            test_mvp_listing_displays_cards(browser)
            test_empty_mvp_listing(browser)
            print("All tests passed!")
        finally:
            browser.close()

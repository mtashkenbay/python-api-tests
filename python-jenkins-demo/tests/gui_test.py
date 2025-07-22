from playwright.sync_api import sync_playwright

def test_open_url():
    with sync_playwright() as p:
        b = p.chromium.launch(headless=False)
        page = b.new_page()
        page.goto("https://the-internet.herokuapp.com/")

        assert "The Internet" in page.title()
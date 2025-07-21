from playwright.sync_api import Page

def test_open_url(page: Page, base_url):
    page.goto(base_url,wait_until="domcontentloaded")

    assert "The Internet" in page.title()
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.fixture(scope="session")
def base_url():
    return "https://the-internet.herokuapp.com/"
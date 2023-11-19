import pytest
import time
import math
from playwright.sync_api import Page,  Playwright, sync_playwright, expect




@pytest.fixture(scope="function" , autouse=True)
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome", headless=True , args=["--start-maximized"])
        context = browser.new_context(ignore_https_errors=True,no_viewport=True)
        page = context.new_page()
        yield page
        page.close()
        browser.close()
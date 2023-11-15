import pytest
import time
import math
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.options import Options
from playwright.sync_api import Playwright, sync_playwright, expect




@pytest.fixture(scope="function" , autouse=True)
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome", headless=False , args=["--start-maximized"])
        context = browser.new_context(ignore_https_errors=True,no_viewport=True)
        page = context.new_page()
        yield page
        page.close()
        browser.close()
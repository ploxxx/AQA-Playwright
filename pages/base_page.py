from socket import timeout
import pytest
import time
import math
import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import Page


class BasePage():
    def __init__(self, page: Page):
        self.page = page

    
    def open(self):
        self.page.get(self.url)
        
    def make_screenshot(self, screenshot_name):
        screenshot = self.page.screenshot()
        allure.attach(
            body=screenshot,
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )
from socket import timeout
import pytest
import time
import math
import allure
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import Page


class BasePage():
    def __init__(self, page: Page):
        self.page = page

    
    def open(self):
        self.page.get(self.url)
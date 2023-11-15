from socket import timeout
import pytest
import time
import math
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import Page


class BasePage():
    def __init__(self, page: Page):
        self.page = page

    
    def open(self):
        self.page.get(self.url)
import pytest
import allure
import time
from .base_page import BasePage
from playwright.sync_api import Page, Playwright, sync_playwright, expect


class MainPageLocators(BasePage):
    
    POPUP_IC_LABEL = 'Close dialog 1'
import pytest
import allure
import time
from .base_page import BasePage
from .locators import MainPageLocators
from playwright.sync_api import Page, Playwright, sync_playwright, expect

class MainPage(BasePage):

    @allure.step("Добавление в корзину")
    def add_to_cart(self):
        self.page.get_by_label(MainPageLocators.POPUP_IC_LABEL).click()
        self.page.locator(".featured_products__inner").scroll_into_view_if_needed()
        self.page.locator(".label").first.click()
        self.page.locator(".product_wrap > div:nth-child(2)").first.click()
        self.page.get_by_role("link", name="Continue to Checkout").click()

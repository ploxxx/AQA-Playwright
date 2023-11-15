import pytest
import allure
import time
from .base_page import BasePage
from .locators import MainPageLocators
from playwright.sync_api import Page, Playwright, sync_playwright, expect


class CheckoutPage(BasePage):

    @allure.step("Авторизация на странице чекаута")
    def authorization_on_the_checkout_page(self):
        self.page.get_by_role("button", name="Log In").click()
        self.page.locator("form").filter(has_text="Email address Password Show Remember me Lost your password? Sign In Don’t have a").locator("#username").click()
        self.page.locator("form").filter(has_text="Email address Password Show Remember me Lost your password? Sign In Don’t have a").locator("#username").fill("vladz@levhaolam.com")
        self.page.locator("form").filter(has_text="Email address Password Show Remember me Lost your password? Sign In Don’t have a").locator("#password").click()
        self.page.locator("form").filter(has_text="Email address Password Show Remember me Lost your password? Sign In Don’t have a").locator("#password").fill("Vld5444789")
        self.page.get_by_role("button", name="Sign In").click()


    @allure.step("Переход на страницу способа доставки")
    def go_to_the_delivery_selection_page(self):
        self.page.locator("label").filter(has_text="I agree to the website terms and conditions and privacy policy *").locator("div").first.click()
        self.page.get_by_role("button", name="Continue to Shipping").click()
        self.page.get_by_role("button", name="Continue anyway").click()
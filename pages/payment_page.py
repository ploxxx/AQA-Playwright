import pytest
import allure
import time
from .base_page import BasePage
from .locators import MainPageLocators , ThankYouPageLocators , PaymentPageLocators
from playwright.sync_api import Page, Playwright, sync_playwright, expect


class PaymentPage(BasePage):

    @allure.step("Оплата через Bluesnap")
    def payment_via_bluesnap(self):
        self.page.frame_locator(PaymentPageLocators.BLUESNAP_FRAME_INPUT).locator("#ccn").click()
        self.page.frame_locator(PaymentPageLocators.BLUESNAP_FRAME_INPUT).get_by_placeholder("XXXX XXXX XXXX XXXX").fill("4557430402053423 ")
        self.page.frame_locator(PaymentPageLocators.BLUESNAP_FRAME_DATE).locator("#exp").click()
        self.page.frame_locator(PaymentPageLocators.BLUESNAP_FRAME_DATE).locator("#exp").fill("12 / 25")
        self.page.frame_locator(PaymentPageLocators.BLUESNAP_FRAME_CVV).locator("#cvv").click()
        self.page.frame_locator(PaymentPageLocators.BLUESNAP_FRAME_CVV).locator("#cvv").fill("288")
        self.page.get_by_role("button", name="Pay now").click()

    @allure.step("Успешная оплата")
    def check_for_successful_payment(self):
        self.page.wait_for_selector(ThankYouPageLocators.ORDER_CLASS)
        expect(self.page.locator(ThankYouPageLocators.TITLE_CLASS).locator(ThankYouPageLocators.TITLE_NUM)).to_have_text(ThankYouPageLocators.THANKYOU_TEXT)
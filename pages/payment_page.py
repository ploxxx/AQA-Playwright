import pytest
import allure
import time
from .base_page import BasePage
from .locators import MainPageLocators , ThankYouPageLocators
from playwright.sync_api import Page, Playwright, sync_playwright, expect


class PaymentPage(BasePage):

    @allure.step("Оплата через Bluesnap")
    def payment_via_bluesnap(self):
        self.page.frame_locator("#bluesnap-hosted-iframe-ccn").get_by_placeholder("XXXX XXXX XXXX XXXX").click()
        self.page.frame_locator("#bluesnap-hosted-iframe-ccn").get_by_placeholder("XXXX XXXX XXXX XXXX").fill("4557430402053423 ")
        self.page.frame_locator("#bluesnap-hosted-iframe-exp").get_by_placeholder("MM / YY").click()
        self.page.frame(url="https://sandbox.bluesnap.com/web-sdk/4.12.7/hpfExpInput.html").get_by_placeholder("MM / YY").fill("12 / 25")
        self.page.frame(url="https://sandbox.bluesnap.com/web-sdk/4.12.7/hpfCvvInput.html").get_by_placeholder("XXX").click()
        self.page.frame(url="https://sandbox.bluesnap.com/web-sdk/4.12.7/hpfCvvInput.html").get_by_placeholder("XXX").fill("288")
        self.page.get_by_role("button", name="Pay now").click()

    @allure.step("Успешная оплата")
    def check_for_successful_payment(self):
        self.page.wait_for_selector(ThankYouPageLocators.ORDER_CLASS)
        expect(self.page.locator(ThankYouPageLocators.TITLE_CLASS).locator(ThankYouPageLocators.TITLE_NUM)).to_have_text(ThankYouPageLocators.THANKYOU_TEXT)
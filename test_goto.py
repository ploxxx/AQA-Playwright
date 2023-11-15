import pytest
import allure
import time
from pages.base_page import BasePage
from pages.main_page import MainPage 
from pages.checkout_page import CheckoutPage
from pages.global_variables import GlobalVariables
from pages.locators import MainPageLocators
from playwright.sync_api import Page, Playwright, sync_playwright, expect

@allure.title("Полный флоу юзера на израелькарте")
def test_israelcart(page: Page):
    page.goto(GlobalVariables.LINK_IC)
    main_page = MainPage(page)
    main_page.add_to_cart()
    checkout_page = CheckoutPage(page)
    checkout_page.authorization_on_the_checkout_page()
    checkout_page.go_to_the_delivery_selection_page()
    page.locator("label").filter(has_text="Economy: Delivery usuall $10.74").locator("div").nth(1).click()
    page.get_by_role("button", name="Continue to Payment").click()
    page.frame_locator("#bluesnap-hosted-iframe-ccn").get_by_placeholder("XXXX XXXX XXXX XXXX").click()
    page.frame_locator("#bluesnap-hosted-iframe-ccn").get_by_placeholder("XXXX XXXX XXXX XXXX").fill("4557430402053423 ")
    page.frame_locator("#bluesnap-hosted-iframe-exp").get_by_placeholder("MM / YY").click()
    page.frame(url="https://sandbox.bluesnap.com/web-sdk/4.12.7/hpfExpInput.html").get_by_placeholder("MM / YY").fill("12 / 25")
    page.frame(url="https://sandbox.bluesnap.com/web-sdk/4.12.7/hpfCvvInput.html").get_by_placeholder("XXX").click()
    page.frame(url="https://sandbox.bluesnap.com/web-sdk/4.12.7/hpfCvvInput.html").get_by_placeholder("XXX").fill("288")
    page.get_by_role("button", name="Pay now").click()
    page.goto("https://uat.israelcart.com/checkout/order-received/43777/?key=wc_order_Fl4DxNm76IvDR")
    page.get_by_text("Thank you!").click()


# Мониторинг сетевых запросов
# def test_listen_network(page: Page):
#     page.on("request", lambda request: print(">>", request.method, request.url))
#     page.on("response", lambda response: print("<<", response.status, response.url))
#     page.goto('https://osinit.ru/')

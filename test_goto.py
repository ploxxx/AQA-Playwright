import pytest
import allure
import time
from pages.base_page import BasePage
from pages.payment_page import PaymentPage
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
    checkout_page.choosing_a_delivery_method()
    payment_page = PaymentPage(page)
    payment_page.payment_via_bluesnap()
    payment_page.check_for_successful_payment()
    payment_page.make_screenshot("Success")


@allure.title("Мониторинг сетевых запросов")
def test_listen_network(page: Page):
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    page.goto(GlobalVariables.LINK_IC)

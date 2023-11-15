import pytest
import allure
import time
from playwright.sync_api import Playwright, sync_playwright, expect

def test_add_todo(page):
    page.goto("https://playwright-todomvc.antonzimaiev.repl.co/#/")
    expect(page).to_have_url("arertwewetwetwe")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")

def test_israelcart(page):
    page.goto("https://uat.israelcart.com/")
    page.get_by_label("Close dialog 1").click()
    page.mouse.move(0,1000)
    page.locator(".label").first.click()
    page.locator(".product_wrap > div:nth-child(2)").first.click()
    page.get_by_role("link", name="Continue to Checkout").click()
    page.get_by_role("button", name="Log In").click()
    page.locator("form").filter(has_text="Email address Password Show Remember me Lost your password? Sign In Don’t have a").locator("#username").click()
    page.locator("form").filter(has_text="Email address Password Show Remember me Lost your password? Sign In Don’t have a").locator("#username").click()
    page.locator("form").filter(has_text="Email address Password Show Remember me Lost your password? Sign In Don’t have a").locator("#username").fill("vladz@levhaolam.com")
    page.locator("form").filter(has_text="Email address Password Show Remember me Lost your password? Sign In Don’t have a").locator("#password").click()
    page.locator("form").filter(has_text="Email address Password Show Remember me Lost your password? Sign In Don’t have a").locator("#password").fill("Vld5444789")
    page.get_by_role("button", name="Sign In").click()
    page.locator("label").filter(has_text="I agree to the website terms and conditions and privacy policy *").locator("div").first.click()
    page.get_by_role("button", name="Continue to Shipping").click()
    page.get_by_role("button", name="Continue anyway").click()
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
def test_listen_network(page):
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    page.goto('https://osinit.ru/')

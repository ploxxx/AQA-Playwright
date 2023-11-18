import pytest
import allure
import time
from .base_page import BasePage
from playwright.sync_api import Page, Playwright, sync_playwright, expect


class MainPageLocators(BasePage):
    
    POPUP_IC_LABEL = 'Close dialog 1'


# class CartPageLocators(BasePage):


# class CheckoutPageLocators(BasePage):

class PaymentPageLocators(BasePage):

    BLUESNAP_FRAME_INPUT = "#bluesnap-hosted-iframe-ccn"
    BLUESNAP_FRAME_DATE = "#bluesnap-hosted-iframe-exp"
    BLUESNAP_FRAME_CVV = "#bluesnap-hosted-iframe-cvv"


class ThankYouPageLocators(BasePage):

    THANKYOU_TEXT = "Thank you!"
    ORDER_CLASS = ".woocommerce-order"
    TITLE_CLASS = ".title"
    TITLE_NUM = "nth=0"

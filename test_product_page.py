from .pages.product_page import ProductPage
from time import sleep
import pytest
from selenium.common.exceptions import NoAlertPresentException

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.compare_name_and_name_added_to_basket()
    page.compare_price_and_price_to_basket()
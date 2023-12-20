from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.bucket_page import BucketPage
import pytest


link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_bucket()
    page.go_to_busket()
    bucket_page = BucketPage(browser, browser.current_url)
    bucket_page.should_not_be_items()
    bucket_page.text_about_emptiness_presented()
    
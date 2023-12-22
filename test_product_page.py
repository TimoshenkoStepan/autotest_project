from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, login_link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        login_page.register_new_user(email, "password123!")
        login_page.should_be_authorized_user()
        self.page = ProductPage(browser, link)
        self.page.open()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        self.page.add_to_basket()
        self.page.solve_quiz_and_get_code()
        self.page.compare_name_and_name_added_to_basket()
        self.page.compare_price_and_price_to_basket()

    def test_user_cant_see_success_message(self):
        self.page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.compare_name_and_name_added_to_basket()
    page.compare_price_and_price_to_basket()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items()
    basket_page.text_about_emptiness_presented()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link, 0)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link, 0)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link, 0)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_dissapear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
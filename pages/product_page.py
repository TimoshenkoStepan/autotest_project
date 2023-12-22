from .base_page import BasePage
import math
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    def add_to_basket(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_btn.click()

    def compare_name_and_name_added_to_basket(self):
        name = self.browser.find_element(*ProductPageLocators.NAME).text
        basket_name = self.browser.find_element(*ProductPageLocators.BASKET_NAME).text
        assert basket_name == name, f"Name and name added to basket do not match"

    def compare_price_and_price_to_basket(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert basket_price == price, f"Price: '{price}' and price to basket: '{basket_price}' do not match"

    def should_dissapear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"

    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")



        
        
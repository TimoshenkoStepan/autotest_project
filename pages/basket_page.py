from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Items is presented in basket"

    def text_about_emptiness_presented(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_ABOUT_EMPTINESS), \
            "The text about emptiness was not found"

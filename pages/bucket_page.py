from .base_page import BasePage
from .locators import BucketPageLocators


class BucketPage(BasePage):
    def should_not_be_items(self):
        assert not self.is_element_present(*BucketPageLocators.BUSKET_ITEMS), \
            "Items is presented in bucket"

    def text_about_emptiness_presented(self):
        assert self.is_element_present(*BucketPageLocators.TEXT_ABOUT_EMPTINESS), \
            "The text about emptiness was not found"


        
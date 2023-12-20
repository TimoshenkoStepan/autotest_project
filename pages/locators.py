from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BUSKET = (By.CSS_SELECTOR, ".basket-mini a.btn-default")

class BucketPageLocators():
    TEXT_ABOUT_EMPTINESS = (By.CSS_SELECTOR, "#content_inner>p")
    BUSKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class MainPageLocators():
    pass
    
class ProductPageLocators():
    ADD_TO_BUSKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    BASKET_NAME = (By.CSS_SELECTOR, "#messages :first-child .alertinner>strong")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner>p>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


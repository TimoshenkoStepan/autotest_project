from selenium.webdriver.common.by import By


class BasePageLocators():
    BASKET = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    TEXT_ABOUT_EMPTINESS = (By.CSS_SELECTOR, "#content_inner>p")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form .btn-primary")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")

class MainPageLocators():
    pass
    
class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_NAME = (By.CSS_SELECTOR, "#messages :first-child .alertinner>strong")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner>p>strong")
    NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


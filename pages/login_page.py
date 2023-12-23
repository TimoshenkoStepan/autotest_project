from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.should_be_login_page()
        self.filling_out_registration_emial_field(email)
        self.filling_out_registration_password_field(password)
        self.filling_out_registration_repeat_password_field(password)
        self.click_registration_button()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not found"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, f"Login is not a substring of current URL: {self.url}"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form not found"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "Registration button not found"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration email not found"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), \
            "Registration password not found"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT), \
            "Registration repeat password not found"

    def filling_out_registration_emial_field(self, email):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_field.send_keys(email)

    def filling_out_registration_password_field(self, password):
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_field.send_keys(password)

    def filling_out_registration_repeat_password_field(self, password):
        password_repeat_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT)
        password_repeat_field.send_keys(password)

    def click_registration_button(self):
        registation_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registation_button.click()

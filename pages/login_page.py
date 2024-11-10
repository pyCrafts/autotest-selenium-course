from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert (
            self.browser.current_url
            == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        ), "Current URL does not match the expected login page URL"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.BTN_LOGIN
        ), "Element not found!"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.BTN_REGISTRATION
        ), "Element not found!"

    def register_new_user(self, email, password):
        self.is_element_present(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.is_element_present(*LoginPageLocators.PASS_INPUT).send_keys(password)
        self.is_element_present(*LoginPageLocators.CONFIRM_PASS_INPUT).send_keys(
            password
        )
        self.click_button(*LoginPageLocators.BTN_REGISTRATION)

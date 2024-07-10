from .base_page import BasePage
from .locators import BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        if (
            self.browser.current_url
            == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        ):
            assert True
        else:
            assert False

    def should_be_login_form(self):
        self.is_element_present(*BasePageLocators.BTN_LOGIN)
        assert True

    def should_be_register_form(self):
        self.is_element_present(*BasePageLocators.BTN_REGISTRATION)
        assert True

    def register_new_user(self, email, password):
        self.is_element_present(*BasePageLocators.EMAIL_INPUT).send_keys(email)
        self.is_element_present(*BasePageLocators.PASS_INPUT).send_keys(password)
        self.is_element_present(*BasePageLocators.CONFIRM_PASS_INPUT).send_keys(
            password
        )
        self.click_button(*BasePageLocators.BTN_REGISTRATION)
        return True

from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def check_products_in_basket(self):
        assert self.is_not_element_present(
            *BasePageLocators.BTN_CHECKOUT
        ), "Good/goods found"
        assert not self.is_disappeared(
            *BasePageLocators.URL_CONTINUE_SHOPPING
        ), "Not url 'continue shopping'"

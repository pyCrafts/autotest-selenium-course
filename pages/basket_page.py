from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def check_products_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BTN_CHECKOUT
        ), "The Checkout button is displayed"
        assert not self.is_disappeared(
            *BasketPageLocators.URL_CONTINUE_SHOPPING
        ), "Not url 'continue shopping'"

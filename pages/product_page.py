from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_basket_product(self):
        self.should_be_check_btn_add_basket()
        self.should_be_click_btn_add_basket()
        self.should_be_send_and_give_answer_code_for_task()
        self.should_be_check_and_comparison_title_with_answer()

    def should_be_check_btn_add_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.BTN_ADD_BASKET
        ), "Button add busket is not presented"

    def should_be_click_btn_add_basket(self):
        self.click_button(*ProductPageLocators.BTN_ADD_BASKET)

    def should_be_send_and_give_answer_code_for_task(self):
        self.solve_quiz_and_get_code()

    def should_be_check_and_comparison_title_with_answer(self):
        product_name = self.get_text(*ProductPageLocators.PRODUCT_NAME)
        product_name_in_alert = self.get_text(
            *ProductPageLocators.PRODUCT_NAME_IN_ALERT
        )
        assert (
            product_name == product_name_in_alert
        ), f"Expected '{product_name}' to be different from '{product_name_in_alert}'"

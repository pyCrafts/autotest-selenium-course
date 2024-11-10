from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BTN_VIEW_BASKET = (By.CSS_SELECTOR, "div.basket-mini > span > a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class ProductPageLocators:
    BTN_ADD_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_NAME_IN_ALERT = (By.CSS_SELECTOR, ".alertinner > strong")


class BasketPageLocators:
    BTN_CHECKOUT = (By.CSS_SELECTOR, ".form-group > div > div > a.btn")
    URL_CONTINUE_SHOPPING = (By.CSS_SELECTOR, "#content_inner > p > a")


class LoginPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name="registration-email"]')
    PASS_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASS_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    BTN_REGISTRATION = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
    BTN_LOGIN = (By.CSS_SELECTOR, 'button[name="login_submit"]')

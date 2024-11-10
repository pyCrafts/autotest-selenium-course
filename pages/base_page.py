from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
    NoAlertPresentException,
)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def click_button(self, how, what):
        try:
            WebDriverWait(self.browser, 30).until(
                EC.element_to_be_clickable((how, what))
            ).click()
        except StaleElementReferenceException as e:
            print("StaleElementReferenceException encountered. Retrying...")
        except TimeoutException as e:
            print("Timed out waiting for confirmation element to load")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_text(self, how, what):
        try:
            element = WebDriverWait(self.browser, 30).until(
                EC.presence_of_element_located((how, what))
            )
            text = element.text
            return text
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

    def go_to_basket_page(self):
        self.browser.find_element(*BasePageLocators.BTN_VIEW_BASKET).click()

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            el = WebDriverWait(self.browser, 30).until(
                EC.presence_of_element_located((how, what))
            )
        except NoSuchElementException:
            return False
        return el

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False

        return True

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), (
            "User icon is not presented," " probably unauthorised user"
        )

    def should_be_login_link(self):
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK
        ), "Login link is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

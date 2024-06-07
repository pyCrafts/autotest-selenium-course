from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_btn_buy(browser):
    browser.get(link)
    time.sleep(30)
    btn_buy = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert btn_buy, "Button buy not found!"

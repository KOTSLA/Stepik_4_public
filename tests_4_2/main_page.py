import time

from tests_4_2.locators_4_2 import MainPageLocators

from tests_4_2.base_page import BasePage
from tests_4_2.login_page import LoginPage

class MainPage(BasePage):
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        time.sleep(3)
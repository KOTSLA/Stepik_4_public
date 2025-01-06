from tests_4_2.base_page import BasePage

from tests_4_2.locators_4_2 import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Check id url is correct
        current_url = self.browser.current_url
        assert "login" in current_url, f"Expected 'login' to be in URL, but got {current_url}"

    def should_be_login_form(self):
        # check if login form is presented
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login form is not presented"

    def should_be_register_form(self):
        # check if registration form is presented
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register form is not presented"
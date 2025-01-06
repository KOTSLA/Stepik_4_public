import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException


url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"

class MainPage():
    def __init__(self, url, browser):
        self.url = url
        self.browser = browser

    def open(self):
        """Open page with item"""
        self.browser.get(self.url)

    def should_be_add_to_cart_button(self):
        """Check if button "Add to card" exist."""
        try:
            self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        except NoSuchElementException:
            raise AssertionError("Button 'Add to card' does not find on page")

    def add_product_to_cart(self):
        """Add item to bucket."""
        add_button = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(ProductPageLocators.ADD_TO_CART_BUTTON)
            )
        add_button.click()

    def should_be_success_massage_about_include_in_bucket(self):
        """Check if message 'has been added to your basket.' is enabled."""
        success_message_element = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(ProductPageLocators.SUCCESS_MESSAGE)
        )
        print(success_message_element.text)
        try:
            self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        except NoSuchElementException:
            raise AssertionError("Item does not add to bucket")

    def go_to_review_section(self):
        """Go to write review."""
        review_link = self.browser.find_element(*ProductPageLocators.REVIEW_LINK)
        review_link.click()

    def should_have_product_details(self):
        """Check if exist on page item name, price and description."""
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Item name does not find on page"
        name_text = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME)
        )
        print(name_text.text)

        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Item price does not find on page"
        price_text = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(ProductPageLocators.PRODUCT_PRICE)
        )
        print(price_text.text)

        assert self.is_element_present(*ProductPageLocators.PRODUCT_DESCRIPTION), "Item description does not find on page"
        description_text = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(ProductPageLocators.PRODUCT_DESCRIPTION)
        )
        print(description_text.text)

        assert self.is_element_present(
            *ProductPageLocators.ADD_PRODUCT_DESCRIPTION), "Item description information text field does not find on page"
        add_description_element = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_DESCRIPTION)
        print(add_description_element.text)
        add_description_text = add_description_element.text.strip()
        assert add_description_text, "Item description information text field is empty"

    def return_to_main_page(self):
        """Go to main page."""
        home_link = self.browser.find_element(*ProductPageLocators.HOME_LINK)
        home_link.click()
        time.sleep(2)

    def is_element_present(self, how, what):
        """is_element_present method."""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True


def test_language(language):
    assert language in ["en", "ru", "es", "fr"], f"Unsupported language: {language}"
    print(f"Running test with language: {language}")

def test_add_to_cart(browser):
    page = MainPage(url, browser=browser)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_product_to_cart()
    page.should_be_success_massage_about_include_in_bucket()
    page.go_to_review_section()
    page.should_have_product_details()
    page.return_to_main_page()

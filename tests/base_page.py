import time
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException

url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"

class BasePage():
    def __init__(self, url, browser):
        self.url = url
        self.browser = browser

    def open(self):
        """Открыть страницу товара."""
        self.browser.get(self.url)

    def should_be_add_to_cart_button(self):
        """Pārbauda, vai ir poga 'Pievienot grozam'."""
        try:
            self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        except NoSuchElementException:
            raise AssertionError("Poga 'Pievienot grozam' nav atrasta uz lapas")

    def add_product_to_cart(self):
        """Добавить товар в корзину."""
        add_button = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(ProductPageLocators.ADD_TO_CART_BUTTON)
            )
        add_button.click()

    def should_be_success_massage_about_include_in_bucket(self):
        """Pārbauda, vai ir paziņojums 'has been added to your basket.'."""
        success_message_element = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(ProductPageLocators.SUCCESS_MESSAGE)
        )
        print(success_message_element.text)
        try:
            self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        except NoSuchElementException:
            raise AssertionError("Prece nav pievienota grozam")

    def go_to_review_section(self):
        """Перейти к написанию отзыва."""
        review_link = self.browser.find_element(*ProductPageLocators.REVIEW_LINK)
        review_link.click()

    def should_have_product_details(self):
        """Проверить, что есть название, цена и описание товара."""
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Название товара отсутствует"
        name_text = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME)
        )
        print(name_text.text)

        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Цена товара отсутствует"
        price_text = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(ProductPageLocators.PRODUCT_PRICE)
        )
        print(price_text.text)

        assert self.is_element_present(*ProductPageLocators.PRODUCT_DESCRIPTION), "Описание товара отсутствует"
        description_text = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(ProductPageLocators.PRODUCT_DESCRIPTION)
        )
        print(description_text.text)

        assert self.is_element_present(
            *ProductPageLocators.ADD_PRODUCT_DESCRIPTION), "Papildu apraksta lauks nav atrasts"
        add_description_element = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_DESCRIPTION)
        print(add_description_element.text)
        add_description_text = add_description_element.text.strip()
        assert add_description_text, "Papildu apraksta lauks ir tukšs"

    def return_to_main_page(self):
        """Вернуться на главную страницу."""
        home_link = self.browser.find_element(*ProductPageLocators.HOME_LINK)
        home_link.click()
        time.sleep(2)

    def is_element_present(self, how, what):
        """Универсальный метод для проверки наличия элемента."""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True


def test_language(language):
    assert language in ["en", "ru", "es", "fr"], f"Unsupported language: {language}"
    print(f"Running test with language: {language}")

def test_add_to_cart(browser):
    page = BasePage(url, browser=browser)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_product_to_cart()
    page.should_be_success_massage_about_include_in_bucket()
    page.go_to_review_section()
    page.should_have_product_details()
    page.return_to_main_page()

from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_BUTTON = (By.XPATH, "//*[@id='register_form']/button")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='login_form']/button")
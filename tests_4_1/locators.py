from selenium.webdriver.common.by import By

class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[@id='add_to_basket_form']/button")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div")
    REVIEW_LINK = (By.XPATH, "//*[@id='write_review']")
    PRODUCT_NAME = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    PRODUCT_DESCRIPTION = (By.XPATH, "//div[@id='product_description']")
    ADD_PRODUCT_DESCRIPTION = (By.XPATH, "//*[@id='content_inner']/article/p")
    HOME_LINK = (By.XPATH, "//a[contains(text(), 'Hacking')]")


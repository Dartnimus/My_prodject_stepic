from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPagesLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_TOTAL = (By.XPATH, "//div[strong[text()='Basket total:']]")
    ADD_TO_BASKED_BTN = (By.CLASS_NAME,"btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRODUCT_PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    ADD_TO_BASKET_MSG = (
    By.XPATH, '//div[strong[text()="{0}"] and normalize-space(text()="has been added to your basket.")]')
    VIEW_BASKET_BTN = (By.LINK_TEXT, 'View basket')
    CHECKOUT_NOW_BTN = (By.LINK_TEXT, 'Checkout now')
    BASKET_MSG = (By.XPATH, '//p[normalize-space(text()="Your basket total is now") and strong[text()="{0}"]]')
    SUCCESS_MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")




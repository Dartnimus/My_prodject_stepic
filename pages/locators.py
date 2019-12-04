from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REGISTER_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REGISTER_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_REGISTER_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTER = (By.NAME, "registration_submit")


class ProductPageLocators():
    BUTTON_ADD_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE_PAGE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alert-success")
    MESSAGE_PRICE_BASKET = (By.CSS_SELECTOR, ".alert-info")
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, ".alert-success strong")
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, ".alert-info strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span a.btn")
    BASKET_NOT_EMPTY = (By.CSS_SELECTOR, ".basket_summary")
    TEXT_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
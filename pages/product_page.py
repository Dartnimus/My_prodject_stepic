from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_to_basket(self): # добавление в корзину
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKED_BTN).click()

    def check_product_page(self): # проверка
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKED_BTN), '"Add to basket" button not found'
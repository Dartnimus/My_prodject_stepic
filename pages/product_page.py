from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium import webdriver



class ProductPage(BasePage):
    def add_to_basket(self): # добавление в корзину
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKED_BTN).click()

    def check_product_page(self): # проверка
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKED_BTN), '"Add to basket" button not found'


    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    def check_add_to_basket_message(self, name):
        assert self.is_element_present(ProductPageLocators.ADD_TO_BASKET_MSG[0],
                                       ProductPageLocators.ADD_TO_BASKET_MSG[1].format(name)), \
            'Added to basket message is not displayed'

    def check_basket_total(self, price):
        current_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert current_price.startswith(f'Basket total: {price}'), f'{current_price} != {price}. Should be the same'

    def check_basket_notification(self, price):
        assert self.is_element_present(*ProductPageLocators.VIEW_BASKET_BTN), '"View basket" button not found'
        assert self.is_element_present(*ProductPageLocators.CHECKOUT_NOW_BTN), '"Checkout now" button not found'
        assert self.is_element_present(ProductPageLocators.BASKET_MSG[0],
                                       ProductPageLocators.BASKET_MSG[1].format(price)), \
            'Basket status message is wrong'
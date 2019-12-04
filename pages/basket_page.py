from .pages.base_page import BasePage
from .pages.locators import BasePageLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        assert not self.is_element_present(*BasePageLocators.BASKET_NOT_EMPTY), "Basket not empty"

    def should_be_basket_empty_text(self):
        text = self.browser.find_element(*BasePageLocators.TEXT_BASKET_EMPTY).text
        assert "Your basket is empty." in text, "Not have a text - Basket not empty"
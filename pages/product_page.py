from .pages.base_page import BasePage
from .locators import ProductPageLocators
class ProductPage(BasePage):
    def should_be_product_page_after_click_add_to_basket(self):
        self.should_be_success_message()
        self.should_be_message_with_price_basket()
        self.should_be_product_in_page_equal_product_in_basket()
        self.should_be_price_in_page_equal_price_in_basket()

    def should_be_click_add_basket(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET).click()

    def should_be_success_message(self):
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_ADD_TO_BASKET)
        assert success_message, "Success message not implemented"

    def should_be_message_with_price_basket(self):
        message_with_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_BASKET)
        assert message_with_price, "Message with price not implemented"

    def should_be_product_in_page_equal_product_in_basket(self):
        product_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_PAGE).text
        product_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_BASKET).text
        assert product_page == product_basket, "Product name in page not equal product name in basket"

    def should_be_price_in_page_equal_price_in_basket(self):
        price_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_PAGE).text
        price_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_BASKET).text
        assert price_page == price_basket, "Price product in page not equal price product in basket"

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_ADD_TO_BASKET), \
            "Success message is presented, but should not be"

    def test_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_ADD_TO_BASKET), \
            "Success message is presented, but should not be"

    def test_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_ADD_TO_BASKET), \
            "Success message is presented, but should not be"
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_busket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()

    def valid_names(self):
        name1 = self.browser.find_element(*ProductPageLocators.NAME_BOOK_ON_PAGE)
        name2 = self.browser.find_element(*ProductPageLocators.NAME_BOOK_IN_BASKET)
        assert name1.text == name2.text, "WRONG NAME OF BOOK IN BASKET"

    def valid_price(self):
        price1 = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_ON_PAGE)
        price2 = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_IN_BASKET)
        assert price1.text == price2.text, "WRONG PRICE OF BOOK"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
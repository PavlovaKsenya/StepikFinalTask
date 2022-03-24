from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert "empty" in self.browser.find_element(*BasketPageLocators.BASKET_TEXT).text, "Basket is not empty"
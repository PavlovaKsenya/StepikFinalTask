import allure

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    @allure.step
    def should_be_empty_basket_message(self):
        assert "empty" in self.browser.find_element(*BasketPageLocators.BASKET_TEXT).text, "Basket is not empty"

    @allure.step
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_INNER), \
            "Basket contains books, but should not be"
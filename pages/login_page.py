import allure

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    @allure.step
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    @allure.step
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Current url don't contain 'login'"

    @allure.step
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    @allure.step
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is not presented"

    @allure.step
    def register_new_user(self, email, password):
        login = self.browser.find_element(*LoginPageLocators.EMAIL)
        login.send_keys(email)
        passw = self.browser.find_element(*LoginPageLocators.PASSWORD)
        passw.send_keys(password)
        passw2 = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM)
        passw2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        button.click()
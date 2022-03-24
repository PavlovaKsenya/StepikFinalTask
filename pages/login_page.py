from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Current url don't contain 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is not presented"

    def register_new_user(self, email, password):
        login = self.browser.find_element(*LoginPageLocators.EMAIL)
        login.send_keys(email)
        passw = self.browser.find_element(*LoginPageLocators.PASSWORD)
        passw.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.LOG_IN_BUTTON)
        button.click()

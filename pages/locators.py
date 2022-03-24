from selenium.webdriver.common.by import By

class MainPageLocators():
    pass

class LoginPageLocators():
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")
    EMAIL = (By.NAME, "registration-email")
    PASSWORD = (By.NAME, "registration-password1")
    PASSWORD_CONFIRM = (By.NAME, "registration-password2")
    REG_BUTTON = (By.NAME, "registration_submit")
    # PRODUCT = (By.CSS_SELECTOR, ".product_pod a")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_BOOK_ON_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    NAME_BOOK_IN_BASKET = (By.CSS_SELECTOR, "#messages strong")
    PRICE_BOOK_ON_PAGE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_BOOK_IN_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner")

class BasePageLocators():
    BASKET = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")
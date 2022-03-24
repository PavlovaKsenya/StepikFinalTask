from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")

class ProductPageLocators():
    ADD_TO_BUSKET = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_BOOK_ON_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    NAME_BOOK_IN_BASKET = (By.CSS_SELECTOR, "#messages strong")
    PRICE_BOOK_ON_PAGE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_BOOK_IN_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
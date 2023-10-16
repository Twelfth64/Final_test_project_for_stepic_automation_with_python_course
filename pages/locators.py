from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
        ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '''[class*='btn-add-to-basket"]''')
    TITLE_OF_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    TITLE_OF_ADDED_TO_CART_PRODUCT = (By.CSS_SELECTOR, ".alertinner strong")
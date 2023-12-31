from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_CART = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasketPageLocators():
    CONTINUE_PURCHASING = (By.CSS_SELECTOR, "#content_inner a")
    CART_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCT_LIST = (By.CSS_SELECTOR, ".basket-items")

class LoginPageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_REPEATE_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[class*='btn-add-to-basket']")
    TITLE_OF_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    TITLE_OF_ADDED_TO_CART_PRODUCT = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    TOTAL_PRICE_OF_CART = (By.CSS_SELECTOR, '''[class*="alert-info"] p strong''')
    SUCCESS_MESSAGE = (By.XPATH, '''//div[@class="alertinner "][contains(., 'has been added to your basket')]''')
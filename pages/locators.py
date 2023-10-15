from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
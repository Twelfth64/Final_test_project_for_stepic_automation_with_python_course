from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def cart_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_LIST), \
            "Product is presented, but should not be"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.CART_IS_EMPTY), \
            "Basket is empty message is not presented"
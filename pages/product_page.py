from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):

    def add_product_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented"

    def title_of_product_should_be_displayed_in_success_message(self):
        title_of_product = self.browser.find_element(*ProductPageLocators.TITLE_OF_PRODUCT)
        title_of_product_in_success_message = self.browser.find_element(*ProductPageLocators.TITLE_OF_ADDED_TO_CART_PRODUCT)
        assert title_of_product_in_success_message.text == title_of_product.text, "The title of product in success message is different from title of added product"

    def total_of_basket_should_be_change_on_price_of_added_product(self):
        price_of_product = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT)
        total_of_basket = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_OF_CART)
        assert price_of_product.text == total_of_basket.text, "The total of basket is incorrect"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def element_should_disappers(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


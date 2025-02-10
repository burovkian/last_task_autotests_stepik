from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import LoginPageLocators
from .locators import BasketPageLocators

class ProductPage(BasePage):
    def should_be_added_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        add_to_basket_btn.click()
        self.solve_quiz_and_get_code()

    def should_be_message_about_add_product(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCT_IN_BASKET_ALERT), "Alert about product addition does not exist"
        assert self.is_element_present(*BasketPageLocators.PRODUCT_NAME), "Product name does not exist"
        prod_name = self.browser.find_element(*BasketPageLocators.PRODUCT_NAME).text
        prod_name_alert = self.browser.find_element(*BasketPageLocators.PRODUCT_IN_BASKET_ALERT).text
        assert prod_name == prod_name_alert, "Product name in product card and alert does not match"


    def should_be_same_price_in_alert(self):
        assert self.is_element_present(*BasketPageLocators.PRICE_ALERT), "Alert with price does not exist"
        assert self.is_element_present(*BasketPageLocators.PRICE_PRODUCT), "Product price does not exist"
        prod_price = self.browser.find_element(*BasketPageLocators.PRICE_PRODUCT).text
        prod_price_alert = self.browser.find_element(*BasketPageLocators.PRICE_ALERT).text
        assert prod_price == prod_price_alert, "Prices does not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*BasketPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should be disappeared"





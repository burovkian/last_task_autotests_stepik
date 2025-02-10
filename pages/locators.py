from selenium.webdriver.common.by import By
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "[id='login_form']")
    REGISTRATION_FORM = (By.CSS_SELECTOR,"[id='register_form']")

class BasketPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR,"[class='add-to-basket'] [type='submit']")
    PRODUCT_NAME = (By.CSS_SELECTOR,"div.product_main h1")
    PRODUCT_IN_BASKET_ALERT = (By.CSS_SELECTOR,"div.alertinner strong")
    PRICE_ALERT = (By.CSS_SELECTOR,"div.alert-info strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR,".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
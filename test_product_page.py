import pytest, time, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from .pages.main_page import MainPage
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(2)]


@pytest.mark.xfail
@pytest.mark.parametrize('link' ,urls)
def test_guest_can_add_product_to_basket(browser, link):

    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_added_to_basket()   # выполняем метод страницы - клик по кнопке -добавляем товар в корзину и решаем задачку
    page.should_be_message_about_add_product()
    page.should_be_same_price_in_alert()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser,link)
    page.open()
    page.should_be_added_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser,link)
    page.open()
    page.should_be_added_to_basket()
    page.should_be_disappeared_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
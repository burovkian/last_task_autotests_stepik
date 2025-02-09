import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOption
from selenium.webdriver.firefox.options import Options as firefoxOption


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default="en", help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    chosen_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        options = chromeOption()
        options.add_experimental_option('prefs', {'intl.accept_languages': chosen_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = firefoxOption()
        options.set_preference("intl.accept_languages", chosen_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
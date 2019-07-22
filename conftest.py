import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromedriver = '/home/sergey/python/chromedriver' # ссылка на драйвер chrome
geckodriver = '/home/sergey/python/geckodriver' # ссылка на драйвер firefox

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="es", help="Choose languages")

@pytest.fixture(scope="function")
def browser(request):

    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(chromedriver, options=options)
        print("\nstart chrome browser for test...options - 'user_language' = {}".format(language))
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(executable_path=geckodriver, firefox_profile=fp)
        print("\nstart firefox browser for test...options - 'user_language' = {}".format(language))
    else:
        print("Browser {} still is not implemented! - start chrome browser for test..".format(browser_name))
        browser = webdriver.Chrome(chromedriver)

    yield browser
    print("\nquit browser..")
    browser.quit()

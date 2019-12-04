import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None, help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None, help="Choose language: ru or es or fr")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\n\nStart Chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intil.accept_languages", user_language)
        print("\n\nStart Firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\n\nStart Chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()





#def pytest_addoption(parser):
#    parser.addoption('--browser_name', action='store', default=None,
#                     help="Choose browser: chrome or firefox")


#@pytest.fixture(scope="function")
#def browser(request):
#    browser_name = request.config.getoption("browser_name")
#    browser = None
#    if browser_name == "chrome":
#        print("\nstart chrome browser for test..")
#        browser = webdriver.Chrome(options=options)
#    elif browser_name == "firefox":
#        print("\nstart firefox browser for test..")
#        browser = webdriver.Firefox(options=options)
#   else:
#        raise pytest.UsageError("--browser_name should be chrome or firefox")
#    yield browser
#    print("\nquit browser..")
#    browser.quit()
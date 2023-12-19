import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Enter the language code")

@pytest.fixture(scope="function")
def browser(request):
    """Returns the Chrome browser in the selected language"""
    language = request.config.getoption("language") or 'en'
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()



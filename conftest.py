import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from seleniumwrapper import SeleniumWrapper


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose lang: ru/en/es...")

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.tryfirst
def pytest_runtest_makereport(item, call, __multicall__):
    rep = __multicall__.execute()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(scope="function")
def screenshot_on_failure(request):
    def fin():
        driver = SeleniumWrapper().driver
        attach = driver.get_screenshot_as_png()
        if request.node.rep_setup.failed:
            allure.attach(request.function.__name__, attach, allure.attach_type.PNG)
        elif request.node.rep_setup.passed:
            if request.node.rep_call.failed:
                allure.attach(request.function.__name__, attach, allure.attach_type.PNG)
    request.addfinalizer(fin)
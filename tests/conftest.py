import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose lang: ru/en/es...")
    parser.addoption('--headless',
                     default='true',
                     help='headless options: "true" or "false"')

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    headless = request.config.getoption('--headless')
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        if headless == 'true':
            options.add_argument("--headless")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        if headless == 'true':
            fp.add_argument("--headless")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    attach = browser.get_screenshot_as_png()
    if request.node.rep_setup.failed:
        allure.attach(attach, request.function.__name__, allure.attachment_type.PNG)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            allure.attach(attach, request.function.__name__, allure.attachment_type.PNG)
    browser.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # выполняем все остальные хуки до получения report object
    outcome = yield
    rep = outcome.get_result()
    # устанавливаем атрубут отчета на каждом этапе вызова:
    # "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)
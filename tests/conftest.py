import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose lang: ru/en/es...")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)

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
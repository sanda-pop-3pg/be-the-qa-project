import pytest

from selenium import webdriver


@pytest.fixture(scope='session', autouse=True)
def driver():
    capabilities = {
        'browserName': 'chrome',
        'platform': 'ANY',
        'version': '',
        'acceptSslCerts': True
    }
    browser = webdriver.Remote(
        command_executor='http://selenium-host:4444/wd/hub',
        desired_capabilities=capabilities)
    browser.implicitly_wait(10)

    yield browser

    browser.quit()

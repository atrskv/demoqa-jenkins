from selene.support.shared import browser
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach


@pytest.fixture(scope='function', autouse=True)
def browser_management():

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    options.capabilities.update(selenoid_capabilities)  # capabilites - словарь

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    browser.config.base_url = 'https://demoqa.com'
    browser.config.browser_name = 'chrome'
    browser.config.hold_browser_open = False
    browser.config.timeout = 20
    browser.config.window_width = 1920
    browser.config.window_height = 1200

    yield

    attach.add_screenshot(browser)
    attach.add_html(browser)
    attach.add_logs(browser)

    browser.quit()
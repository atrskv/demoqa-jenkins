from selene.support.shared import browser
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach

from selene import Browser, Config  # для кастомного браузера


@pytest.fixture(scope='function', autouse=True)
def browser_management():

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)  # capabilites - словарь

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser = Browser(Config(driver))  # кастомный браузер

    browser.base_url = 'https://demoqa.com'
    browser.browser_name = 'chrome'
    browser.hold_browser_open = False
    browser.timeout = 20
    browser.window_width = 1920
    browser.window_height = 1200

    yield

    attach.add_screenshot(browser)
    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()

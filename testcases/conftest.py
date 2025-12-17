import allure
import pytest
import time
from selenium import webdriver

from config.path import FAIL_PIC_PATH
from page_objects.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    time.sleep(3)
    driver.quit()

@pytest.fixture(scope="function")
def login_driver(driver):
    login_page = LoginPage(driver)
    login_page.login("/cn/customer/account/login", "18817750834", "123456")
    yield driver

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     if report.when == "call" and report.failed:
#         driver = getattr(item, "driver", None)
#         if driver:
#             take_screenshot(driver, item.name)
#
# def take_screenshot(driver, name):
#     timestamp = time.strftime("%Y%m%d-%H%M%S")
#     filename = name+"_"+timestamp+".png"
#     filepath = FAIL_PIC_PATH/filename
#     try:
#         driver.save_screenshot(filepath)
#         with open(filepath, "rb") as f:
#             allure.attach(f.read(),
#                           name=f"失败截图_{name}_{timestamp}",
#                           attachment_type=allure.attachment_type.PNG)
#     except Exception as e:
#         print(f"\n[截图失败]：{e}")
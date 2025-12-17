from pathlib import Path
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.yaml_util import read_config
from config.path import DATA_PATH


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.config = read_config()
        self.timeout = self.config["common"]["timeout"]

    def open(self, url):
        self.driver.maximize_window()
        self.driver.get(url)

    def find_element(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        except Exception as e:
            print(f"元素定位失败：{locator}")
            raise e

    def input_text(self, locator, text):
        if text is None:
            self.find_element(locator).clear()
        else:
            self.find_element(locator).send_keys(text)

    def click(self, locator):
        self.find_element(locator).click()

    def upload_file(self, locator, file):
        path = str(DATA_PATH/file)
        self.find_element(locator).send_keys(path)

    def screenshot(self, locator, file):
        path = str(DATA_PATH/file)
        self.find_element(locator).screenshot(path)
import time
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from selenium import webdriver
from selenium.common import TimeoutException

class RegisterPage(BasePage):
    account_loc = (By.CSS_SELECTOR, '#phone')
    password_loc = (By.CSS_SELECTOR, '#password')
    conf_pass_loc = (By.CSS_SELECTOR, '#confirmation')
    btn_register_loc = (By.CSS_SELECTOR, '#register-btn')
    # Please input the phone
    account_error_loc = (By.CSS_SELECTOR, '#register-form > div > ul > div > li:nth-child(2) > span > em')
    # 请输入密码
    password_error_loc = (By.CSS_SELECTOR, '#register-form > div > ul > div > li:nth-child(3) > span > em')
    # 请输入确认密码
    conf_pass_error_loc = (By.CSS_SELECTOR, '#register-form > div > ul > div > li.relative.confirmation-login > span > em')
    # Password应该包含至少6个字符。
    # this phone is exist!
    # this phone is exist!,Password应该包含至少6个字符。
    user_error_loc = (By.CSS_SELECTOR, 'body > div.main-container > div > div.fecshop_message > div > div')
    error_loc_list = [account_error_loc, password_error_loc, conf_pass_error_loc, user_error_loc]

    def register(self, url, account, password, conf_pass):
        self.open(self.config["common"]["base_url"]+url)
        self.input_text(self.account_loc, account)
        self.input_text(self.password_loc, password)
        self.input_text(self.conf_pass_loc, conf_pass)
        self.click(self.btn_register_loc)

    def get_error_msg(self):
        for error_loc in self.error_loc_list:
            try:
                element = self.find_element(error_loc)
                if element.is_displayed():
                    return element.text
            except TimeoutException:
                pass




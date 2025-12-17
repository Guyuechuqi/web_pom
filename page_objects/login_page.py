from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class LoginPage(BasePage):
    account_loc = (By.CSS_SELECTOR, '#phone')
    password_loc = (By.CSS_SELECTOR, '#password')
    btn_login = (By.CSS_SELECTOR, '#login-btn')
    # Please input the phone
    account_error_loc = (By.CSS_SELECTOR, '#loginForm > div > ul > div > li:nth-child(2) > span > em')
    # 请输入密码
    password_error_loc = (By.CSS_SELECTOR, '#loginForm > div > ul > div > li:nth-child(3) > span > em')
    # phone is not exist
    # 用户的账号密码不正确
    # Phone是无效的。
    # 请输入密码
    # Please input the phone
    user_error_loc = (By.CSS_SELECTOR, 'body > div.main-container > div > div.fecshop_message > div > div')
    error_loc_list = [account_error_loc, password_error_loc, user_error_loc]

    def login(self, url, account, password):
        self.open(self.config["common"]["base_url"]+url)
        self.input_text(self.account_loc, account)
        self.input_text(self.password_loc, password)
        self.click(self.btn_login)

    def get_error_msg(self):
        for error_loc in self.error_loc_list:
            from selenium.common import TimeoutException
            try:
                element = self.find_element(error_loc)
                if element.is_displayed():
                    return element.text
            except TimeoutException:
                pass
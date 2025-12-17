import time
from selenium.webdriver.common.by import By
from common.captcha_util import get_captcha
from page_objects.base_page import BasePage
from selenium import webdriver

from page_objects.login_page import LoginPage


class DistributorPage(BasePage):
    name_loc = (By.CSS_SELECTOR, '#firstname')
    phone_loc = (By.CSS_SELECTOR, '#telephone')
    qq_loc = (By.CSS_SELECTOR, '#qq')
    id_card_loc = (By.CSS_SELECTOR, '#id_number')
    referrer_loc = (By.CSS_SELECTOR, '#distribute_parent_code')
    id_positive_loc = (By.CSS_SELECTOR, '#id_card_positive')
    id_reverse_loc = (By.CSS_SELECTOR, '#id_card_reverse')
    captcha_loc = (By.CSS_SELECTOR, '#captcha')
    captcha_pic_loc = (By.CSS_SELECTOR, '#register-form > div > ul > div > li:nth-child(9) > img')
    btn_application = (By.CSS_SELECTOR, '#register-btn')
    correct_msg_loc = (By.CSS_SELECTOR, 'body > div.main-container > div > div.fecshop_message > div > div')

    name_error_loc = (By.CSS_SELECTOR, '#register-form > div > ul > div > li:nth-child(2) > span > em')
    phone_error_loc = (By.CSS_SELECTOR, '#register-form > div > ul > div > li:nth-child(3) > span > em')
    referrer_error_loc = (By.CSS_SELECTOR, '#register-form > div > ul > div > li:nth-child(6) > span > em')
    error_loc_list = [name_error_loc, phone_error_loc, referrer_error_loc]

    def distributor_application(self, url, name, phone, qq, id_card, referrer, id_positive, id_reverse):
        self.open(self.config["common"]["base_url"]+url)
        self.input_text(self.name_loc, name)
        self.input_text(self.phone_loc, phone)
        self.input_text(self.qq_loc, qq)
        self.input_text(self.id_card_loc, id_card)
        self.input_text(self.referrer_loc, referrer)
        self.upload_file(self.id_positive_loc, id_positive)
        self.upload_file(self.id_reverse_loc, id_reverse)
        self.screenshot(self.captcha_pic_loc, "captcha.png")
        captcha = get_captcha()
        self.input_text(self.captcha_loc, captcha)
        time.sleep(3)
        self.click(self.btn_application)

    def get_correct_msg(self):
        return self.find_element(self.correct_msg_loc).text

    def get_error_msg(self):
        for error_loc in self.error_loc_list:
            from selenium.common import TimeoutException
            try:
                element = self.find_element(error_loc)
                if element.is_displayed():
                    return element.text
            except TimeoutException:
                pass
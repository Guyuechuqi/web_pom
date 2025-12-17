import allure
import pytest
from common.yaml_util import read_yaml
from page_objects.register_page import RegisterPage

@pytest.mark.skip
class TestRegister:
    @pytest.mark.parametrize("case_info", read_yaml("register_data.yaml"))
    def test_register(self, driver, case_info):
        allure.dynamic.epic(case_info["epic"])
        allure.dynamic.feature(case_info["feature"])
        allure.dynamic.story(case_info["story"])
        allure.dynamic.title(case_info["title"])
        register_page = RegisterPage(driver)
        register_page.register(case_info["url"], **case_info["payload"])
        for msg, assertion in case_info["validate"]["equals"].items():
            method, expected = assertion[0], assertion[1]
            if method == "current_url":
                assert driver.current_url == expected
            else:
                assert register_page.get_error_msg() == expected, msg
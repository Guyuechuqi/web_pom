import allure
import pytest
from common.yaml_util import read_yaml
from page_objects.distributor_page import DistributorPage

# @pytest.mark.skip
class TestDistributor:
    @pytest.mark.parametrize("case_info", read_yaml("distributor_data.yaml"))
    def test_distributor(self, login_driver, case_info):
        allure.dynamic.epic(case_info["epic"])
        allure.dynamic.feature(case_info["feature"])
        allure.dynamic.story(case_info["story"])
        allure.dynamic.title(case_info["title"])
        distribute_page = DistributorPage(login_driver)
        distribute_page.distributor_application(case_info["url"], **case_info["payload"])
        for msg, assertion in case_info["validate"]["equals"].items():
            method, expected = assertion[0], assertion[1]
            if method == "correct_msg":
                msg = distribute_page.get_correct_msg()
                assert msg == expected
            else:
                assert distribute_page.get_error_msg() == expected, msg
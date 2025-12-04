import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.automation_wrapper import AutomationWrapper
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utilities.data_source import DataSource


class TestLogin(AutomationWrapper):

    @pytest.mark.parametrize("username,password,expected_value", DataSource.data_valid_login)
    def test_valid_login(self, username, password, expected_value):
        login = LoginPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_on_login()

        dashboard=DashboardPage(self.driver)
        actual_value = dashboard.get_quick_launch_text()
        assert_that(expected_value).is_equal_to(actual_value)

    @pytest.mark.parametrize("username, password, expected_error", DataSource.data_invalid_login_excel)
    def test_invalid_login(self, username, password, expected_error):
        login = LoginPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_on_login()

        actual_value = login.get_invalid_error_message()
        assert_that(expected_error).contains(actual_value)

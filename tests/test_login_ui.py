import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.automation_wrapper import AutomationWrapper
from pages.login_page import LoginPage


class TestLoginUI(AutomationWrapper):

    @pytest.mark.regression
    @pytest.mark.ui
    def test_title(self):
        actual_title = self.driver.title
        assert_that("OrangeHRM").is_equal_to(actual_title)

    @pytest.mark.regression
    def test_header(self):
        login = LoginPage(self.driver)
        actual_header = login.get_login_header()
        assert_that("Login").is_equal_to(actual_header)

    @pytest.mark.regression
    def test_placeholder(self):
        login = LoginPage(self.driver)
        assert_that("Username").is_equal_to(login.get_username_placeholder())
        assert_that("Password").is_equal_to(login.get_password_placeholder())

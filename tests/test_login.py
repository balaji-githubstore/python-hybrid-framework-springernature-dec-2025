import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.automation_wrapper import AutomationWrapper
from utilities.data_source import DataSource


class TestLogin(AutomationWrapper):

    @pytest.mark.parametrize("username,password,expected_value", DataSource.data_valid_login)
    def test_valid_login(self, username, password, expected_value):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Login')]").click()
        actual_value = self.driver.find_element(By.XPATH, "//p[contains(normalize-space(),'Quick')]").text
        assert_that(expected_value).is_equal_to(actual_value)

    @pytest.mark.parametrize("username, password, expected_error", DataSource.data_invalid_login)
    def test_invalid_login(self, username, password, expected_error):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Login')]").click()
        actual_value = self.driver.find_element(By.XPATH, "//p[contains(normalize-space(),'Invalid')]").text
        assert_that(expected_error).contains(actual_value)

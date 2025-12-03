import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.automation_wrapper import AutomationWrapper


class TestLogin(AutomationWrapper):

    def test_valid_login(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Login')]").click()
        actual_value = self.driver.find_element(By.XPATH, "//p[contains(normalize-space(),'Quick')]").text
        assert_that("Quick Launch").is_equal_to(actual_value)

    @pytest.mark.parametrize("username, password, expected_error", [
        ("saul", "saul123", "Invalid credentials"),
        ("peter", "pete123", "Invalid credentials")
    ])
    def test_invalid_login(self, username, password, expected_error):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Login')]").click()
        actual_value = self.driver.find_element(By.XPATH, "//p[contains(normalize-space(),'Invalid')]").text
        assert_that(expected_error).contains(actual_value)

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

    def test_invalid_login(self):
        self.driver.find_element(By.NAME, "username").send_keys("john")
        self.driver.find_element(By.NAME, "password").send_keys("john123")
        self.driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Login')]").click()
        # Assert the error text - Invalid credentials
        actual_value = self.driver.find_element(By.XPATH, "//p[contains(normalize-space(),'Invalid')]").text
        assert_that("Invalid credentials").contains(actual_value)

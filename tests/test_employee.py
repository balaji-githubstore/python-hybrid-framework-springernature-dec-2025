import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.automation_wrapper import AutomationWrapper
from pages.login_page import LoginPage


class TestEmployee(AutomationWrapper):
    def test_add_valid_employee(self):
        print("test employee")
        print("test employee")
        print("test employee")

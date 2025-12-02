import pytest
from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginUI:

    @pytest.fixture(scope="function", autouse=True)
    def set_up(self):
        # runs before each test
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        # runs after each test even test fails
        self.driver.quit()

    def test_title(self):
        actual_title = self.driver.title
        assert_that("OrangeHRM").is_equal_to(actual_title)

    def test_header(self):
        actual_header = self.driver.find_element(By.XPATH, "//h5[text()='Login']").text
        assert_that("Login").is_equal_to(actual_header)

    def test_placeholder(self):
        print("placeholder")
#         Assert Username placeholder  - Username
#           Assert Password placeholder  - Username

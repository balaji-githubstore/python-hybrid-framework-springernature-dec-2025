from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.__driver: WebDriver = driver

    def enter_username(self, username):
        self.__driver.find_element(By.NAME, "username").send_keys(username)

    def enter_password(self, password):
        self.__driver.find_element(By.NAME, "password").send_keys(password)

    def click_on_login(self):
        self.__driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Login')]").click()

    def get_invalid_error_message(self):
        return self.__driver.find_element(By.XPATH, "//p[contains(normalize-space(),'Invalid')]").text

    def get_login_header(self):
        return self.__driver.find_element(By.XPATH, "//h5[text()='Login']").text

    def get_username_placeholder(self):
        return self.__driver.find_element(By.NAME, "username").get_attribute("placeholder")

    def get_password_placeholder(self):
        return self.__driver.find_element(By.NAME, "password").get_attribute("placeholder")

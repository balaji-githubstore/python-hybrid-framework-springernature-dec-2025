
import pytest

from utilities.excel_utils import ExcelSource
"""Setup and Teardown in parent class in different package & 2 test method in child class"""
"""running test method from csv and excel """


class TestLogin:
    @pytest.mark.parametrize("username, password, exp_value",
                             ExcelSource.get_one_row(
                                 file_path=r"D:\Balaji\Company\SpringerNature Nov 2025\Projects\pytest_python_selenium_automation_framework\test_data\hrm_data.xlsx"
                                 , sheet_name="test_valid_login",
                                 row_num=2
                             ))
    def test_one_row(self, username, password, exp_value):
        print(username)
        print(password)
        print(exp_value)


    @pytest.mark.parametrize("username, password, exp_value",
                             ExcelSource.get_exact_rows(
                                 file_path=r"D:\Balaji\Company\SpringerNature Nov 2025\Projects\pytest_python_selenium_automation_framework\test_data\hrm_data.xlsx"
                                 , sheet_name="test_valid_login",
                                 row_num=[2,3]
                             ))
    def test_exact_rows(self, username, password, exp_value):
        print(username)
        print(password)
        print(exp_value)

    @pytest.mark.parametrize("key_value_set",
                             ExcelSource.get_all_rows_as_dicts(
                                 file_path=r"D:\Balaji\Company\SpringerNature Nov 2025\Projects\pytest_python_selenium_automation_framework\test_data\hrm_data.xlsx"
                                 , sheet_name="test_valid_login"
                             ))
    def test_list_of_dics(self, key_value_set:dict):
        print(key_value_set["username"])
        print(key_value_set["password"])

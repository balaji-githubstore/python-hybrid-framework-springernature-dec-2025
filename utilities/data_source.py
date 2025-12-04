""" This module contains data for all test methods """

import os.path

from utilities import data_reader
from config import Config


class DataSource:
    data_invalid_login = [("saul", "saul123", "Invalid credentials"),
                          ("peter", "pete123", "Invalid credentials")]

    data_valid_login = [("Admin", "admin123", "Quick Launch")]

    data_invalid_login_excel = data_reader.get_sheet_into_list(os.path.join(Config.DATA_DIR, "orange_hrm_data.xlsx"),
                                                               "test_invalid_login")

""" Config class - helps to get Root Directory, Test Data Directory, Report Directory inside the project   """
import os


class Config:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(ROOT_DIR, "test_data")
    REPORT_DIR = os.path.join(ROOT_DIR, "report")

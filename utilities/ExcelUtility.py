import pandas as pd

from ..common.logger_config import setup_logger

# Setup logger
logger = setup_logger('ExcelUtility')


class ExcelUtility:
    def __init__(self, excel_file_path: str ="", sheet_name: str =""):
        self.file_path = excel_file_path
        self.sheet_name = sheet_name
    
    def update_excel_file_path(self, new_file_path: str) -> None:
        self.file_path = new_file_path
        logger.debug("Excel file path updated.")
    
    def update_sheet_name(self, new_sheet_name: str) -> None:
        logger.debug("Sheet Name Updated.")
        self.sheet_name = new_sheet_name

    def get_file_path(self) -> str:
        return self.file_path
    
    def get_sheet_name(self) -> str:
        return self.sheet_name
    
    def read_excel_file(self):
        # Read the Excel file into a pandas DataFrame
        if not self.sheet_name:
            df = pd.read_excel(self.file_path)
        else:
            df = pd.read_excel(self.file_path, sheet_name=self.sheet_name)
        return df
    
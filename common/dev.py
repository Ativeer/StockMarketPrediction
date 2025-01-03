from prod_config import Config


class DevelopmentConfig(Config):

    DEBUG = True
    TESTING = True
    EXCEL_FILE_PATH = "../resources/stocks/TSLA.csv"

    @staticmethod
    def get_config_name():
        return "Development"
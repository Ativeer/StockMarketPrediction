class Config(object):

    DEBUG = False
    TESTING = False
    EXCEL_FILE_PATH = ""

    @staticmethod
    def get_config_name():
        return "Production"
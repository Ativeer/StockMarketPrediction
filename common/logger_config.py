import logging


def setup_logger(name):
    # Create a logger
    logger = logging.getLogger(name)
    
    # Set the log level (you can change it to DEBUG, INFO, WARNING, etc.)
    logger.setLevel(logging.DEBUG)

    # Create a formatter for log messages
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(log_format)
    
    # Create a console handler to output logs to the console
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)  # Set the level of logging for console
    ch.setFormatter(formatter)
    
    # Create a file handler to output logs to a file
    fh = logging.FileHandler('stock_market_feature_ranking.log')
    fh.setLevel(logging.DEBUG)  # Set the level of logging for file
    fh.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(ch)
    logger.addHandler(fh)
    
    return logger
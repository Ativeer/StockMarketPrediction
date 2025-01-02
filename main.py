from common.logger_config import setup_logger

# Setup logger
logger = setup_logger('Main')

def main():
    logger.info("Starting the application")
    
    try:
        logger.info("Hello!")
    except Exception as e:
        logger.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
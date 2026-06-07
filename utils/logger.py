import logging
from config.config import LOG_FILE

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_info(message):
    logging.info(message)
    print("[INFO]", message)

def log_error(message):
    logging.error(message)
    print("[ERROR]", message)
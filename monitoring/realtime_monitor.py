import time
from utils.logger import log_info
from scanner.port_scanner import start_scan

def start_monitoring(interval=30):
    log_info("Starting real-time monitoring...")

    while True:
        log_info("Running scheduled scan...")
        start_scan()
        time.sleep(interval)
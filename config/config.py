TARGET = "127.0.0.1"

PORT_RANGE = (1, 1024)
THREADS = 100
TIMEOUT = 1

LOG_FILE = "logs/scan.log"

ENABLE_EMAIL_ALERTS = False
EMAIL_RECEIVER = "receiver@gmail.com"

RISK_LEVELS = {
    "LOW": (0, 3),
    "MEDIUM": (4, 7),
    "HIGH": (8, 10)
}
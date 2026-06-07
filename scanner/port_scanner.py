import socket
import threading
from config.config import THREADS, TIMEOUT, PORT_RANGE, TARGET
from utils.logger import log_info

open_ports = []

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(TIMEOUT)

        if s.connect_ex((TARGET, port)) == 0:
            log_info(f"OPEN PORT: {port}")
            open_ports.append(port)

        s.close()
    except:
        pass


def start_scan():
    log_info(f"Starting scan on {TARGET}")

    threads = []

    for port in range(PORT_RANGE[0], PORT_RANGE[1]):
        t = threading.Thread(target=scan_port, args=(port,))
        threads.append(t)
        t.start()

        if len(threads) >= THREADS:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

    log_info(f"Scan completed. Open ports: {open_ports}")

    return open_ports
from utils.logger import log_info

def detect_threats(vuln_results):
    threats = []

    for item in vuln_results:
        if item["risk"] == "HIGH":
            threats.append(item)

    log_info(f"Threats detected: {len(threats)}")

    return threats
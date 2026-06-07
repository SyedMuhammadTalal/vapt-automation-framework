from utils.logger import log_info

RISK_SCORE_MAP = {
    "LOW": 2,
    "MEDIUM": 5,
    "HIGH": 9
}

def calculate_risk(vuln_results):
    log_info("Calculating risk score...")

    total = 0
    scored = []

    for item in vuln_results:
        score = RISK_SCORE_MAP.get(item["risk"], 1)
        total += score

        scored.append({
            "port": item["port"],
            "service": item["service"],
            "risk": item["risk"],
            "score": score
        })

        log_info(f"Port {item['port']} score: {score}")

    avg = total / len(vuln_results) if vuln_results else 0

    if avg <= 3:
        level = "LOW"
    elif avg <= 6:
        level = "MEDIUM"
    else:
        level = "HIGH"

    return {
        "results": scored,
        "average_score": round(avg, 2),
        "overall_risk": level
    }
def format_ip(ip):
    return str(ip).strip()

def severity_color(risk):
    return {
        "LOW": "GREEN",
        "MEDIUM": "YELLOW",
        "HIGH": "RED"
    }.get(risk, "UNKNOWN")
from utils.logger import log_info

def analyze_logs(log_file="logs/scan.log"):
    try:
        with open(log_file, "r") as f:
            logs = f.readlines()

        errors = [line for line in logs if "ERROR" in line]

        log_info(f"Log analysis complete. Errors found: {len(errors)}")

        return {
            "total_logs": len(logs),
            "errors": len(errors)
        }

    except FileNotFoundError:
        log_info("Log file not found")
        return {}
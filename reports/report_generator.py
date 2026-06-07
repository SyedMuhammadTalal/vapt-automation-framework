import csv
import json
import os
from utils.logger import log_info

CSV_FILE = "output/scans/report.csv"
JSON_FILE = "output/json/report.json"

def generate_report(risk_data):

    log_info("Generating reports...")

    os.makedirs("output/scans", exist_ok=True)
    os.makedirs("output/json", exist_ok=True)

    # CSV
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Port", "Service", "Risk", "Score"])

        for r in risk_data["results"]:
            writer.writerow([r["port"], r["service"], r["risk"], r["score"]])

    # JSON
    with open(JSON_FILE, "w") as f:
        json.dump(risk_data, f, indent=4)

    log_info("Reports generated successfully")

    return {
        "csv": CSV_FILE,
        "json": JSON_FILE
    }
from scanner.port_scanner import start_scan
from vulnerability.vulnerability_checker import check_vulnerabilities
from risk_scoring.risk_calculator import calculate_risk
from reports.report_generator import generate_report
from alerts.email_alert import send_email
from config.config import ENABLE_EMAIL_ALERTS, EMAIL_RECEIVER


if __name__ == "__main__":

    # Step 1: Scan
    open_ports = start_scan()

    # Step 2: Vulnerability Check
    vuln_results = check_vulnerabilities(open_ports)

    # Step 3: Risk Scoring
    risk_report = calculate_risk(vuln_results)

    # Step 4: Report Generation
    report_files = generate_report(risk_report)

    print("\n✔ SCAN COMPLETED")
    print("Risk Level:", risk_report["overall_risk"])
    print("Average Score:", risk_report["average_score"])

    # Step 5: Email Alert (if enabled)
    if ENABLE_EMAIL_ALERTS:
        send_email(
            receiver_email=EMAIL_RECEIVER,
            subject=f"[VAPT REPORT] Risk: {risk_report['overall_risk']}",
            body=f"""
VAPT Scan Completed Successfully

Risk Level: {risk_report['overall_risk']}
Average Score: {risk_report['average_score']}
Open Ports Found: {len(open_ports)}

Reports Attached.
            """,
            attachments=[
                report_files["csv"],
                report_files["json"]
            ]
        )

        print("✔ Email Sent Successfully"):
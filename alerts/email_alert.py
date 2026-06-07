import smtplib
import os
from email.message import EmailMessage
from utils.logger import log_info

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"

def send_email(receiver_email, subject, body, attachments=[]):

    try:
        log_info("Sending email alert...")

        msg = EmailMessage()
        msg["From"] = SENDER_EMAIL
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.set_content(body)

        for file in attachments:
            if os.path.exists(file):
                with open(file, "rb") as f:
                    msg.add_attachment(
                        f.read(),
                        maintype="application",
                        subtype="octet-stream",
                        filename=os.path.basename(file)
                    )

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()

        log_info("Email sent successfully")

    except Exception as e:
        log_info(f"Email error: {e}")
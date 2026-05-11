import smtplib
from email.mime.text import MIMEText
from config.settings import *

def send_email(to_emails, student_data):

    try:

        subject = "Student Escalation Alert"

        body = f"""
Hi,

The following students crossed the threshold:

{student_data}

Please investigate the cases.

Regards,
Automated Student Tracking System
"""
        msg = MIMEText(body)

        msg["Subject"] = subject
        msg["From"] = SENDER_EMAIL
        msg["To"] = ", ".join(to_emails)

        print("Sending mail to:", to_emails)

        server = smtplib.SMTP(
            SMTP_SERVER,
            SMTP_PORT,
            timeout=30
        )

        server.starttls()

        server.login(
            SENDER_EMAIL,
            APP_PASSWORD
        )

        server.sendmail(
            SENDER_EMAIL,
            to_emails,
            msg.as_string()
        )

        server.quit()

        print("Mail sent successfully")

    except Exception as e:

        print("Error sending mail")

        print(e)
import smtplib
from email.mime.text import MIMEText
from config.settings import *

def send_email(to_emails, student_name, pending_days):

    subject = f"Student Escalation Alert - {student_name}"

    body = f"""
    Student escalation alert.

    Student Name: {student_name}
    Pending Days: {pending_days}

    The student's pending days have crossed the threshold.

    Please investigate the case.

    Regards,
    Automated Student Tracking System
    """

    msg = MIMEText(body)

    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = ", ".join(to_emails)

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

    server.starttls()

    server.login(SENDER_EMAIL, APP_PASSWORD)

    server.sendmail(
        SENDER_EMAIL,
        to_emails,
        msg.as_string()
    )

    server.quit()
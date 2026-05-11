from datetime import datetime
from processor import get_escalation_rows
from mailer import send_email

EXCEL_PATH = "data/final_dashboard_updated.xlsx"

df, rows = get_escalation_rows()

today = datetime.today().strftime("%Y-%m-%d")

for index, row in rows:

    recipients = [
        "yashika0432@gmail.com"
    ]

    send_email(
        recipients,
        row["FULL NAME"],
        row["DAYS ELAPSED"]
    )

    df.at[index, "LastMailSent"] = today

    print(f"Mail sent for {row['FULL NAME']}")

df.to_excel(EXCEL_PATH, index=False)

print("Automation completed.")
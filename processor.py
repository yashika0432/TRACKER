import pandas as pd
from datetime import datetime
from config.settings import THRESHOLD_DAYS

EXCEL_PATH = "data/final_dashboard_updated.xlsx"

def get_escalation_rows():

    df = pd.read_excel(EXCEL_PATH)

    today = datetime.today().strftime("%Y-%m-%d")

    filtered_rows = []

    for index, row in df.iterrows():

        pending_days = row["DAYS ELAPSED"]

        last_mail = str(row.get("LastMailSent", ""))

        if pending_days >= THRESHOLD_DAYS:

            if today not in last_mail:

                filtered_rows.append((index, row))

    return df, filtered_rows
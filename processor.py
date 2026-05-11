import pandas as pd
from datetime import datetime
from config.settings import THRESHOLD_DAYS, MAX_DAYS

EXCEL_PATH = "data/final_dashboard_updated.xlsx"

def get_escalation_rows():

    df = pd.read_excel(EXCEL_PATH, header=2)

    # Clean columns
    df.columns = (
        df.columns
        .str.strip()
        .str.upper()
        .str.replace("\n", "_")
        .str.replace(" ", "_")
    )

    # Convert APS_RECEIVED_DATE to datetime
    df["APS_RECEIVED_DATE"] = pd.to_datetime(
    df["APS_RECEIVED_DATE"],
    dayfirst=True,
    errors="coerce"
)

    # Calculate days elapsed
    today = pd.Timestamp.today()

    df["DAYS_ELAPSED"] = (
        today - df["APS_RECEIVED_DATE"]
    ).dt.days

    print(df[["FULL_NAME", "DAYS_ELAPSED"]].head())

    # Filter rows
    filtered = df[
        (df["DAYS_ELAPSED"] >= THRESHOLD_DAYS) &
        (df["DAYS_ELAPSED"] <= MAX_DAYS)
    ]

    return filtered
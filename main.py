from processor import get_escalation_rows
from mailer import send_email
from config.settings import RECIPIENTS

rows = get_escalation_rows()

if rows.empty:

    print("No students crossed threshold.")

else:

    student_data = ""

    for i, row in rows.iterrows():

        student_data += f"""
Student Name : {row['FULL_NAME']}

Contact      : {row['CONTACT']}

Email        : {row['EMAIL']}

Days Elapsed : {row['DAYS_ELAPSED']}

"""

    send_email(
        RECIPIENTS,
        student_data
    )
# scheduler.py
import schedule
import time
from main_app.utils import send_birthday_reminders

# Schedule the email reminder function to run daily at midnight
schedule.every().day.at('00:00').do(send_birthday_reminders)

while True:
    schedule.run_pending()
    time.sleep(1)

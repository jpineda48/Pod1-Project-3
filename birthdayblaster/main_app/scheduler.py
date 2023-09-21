import schedule
import time
from main_app.utils import send_birthday_reminders

# Schedules when the function to send email reminders should run
schedule.every().day.at('00:00').do(send_birthday_reminders) # Daily at midnight

while True:
    schedule.run_pending()
    time.sleep(1)

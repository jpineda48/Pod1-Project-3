# main_app/utils.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.utils import timezone
from .models import Birthday

def send_birthday_reminders():
    today = timezone.now()
    next_30_days = today + timezone.timedelta(days=30)
    upcoming_birthdays = Birthday.objects.filter(date__range=[today, next_30_days])

    for birthday in upcoming_birthdays:
        # Reminder email content
        subject = 'Upcoming Birthday Reminder'
        message = f"Don't forget, {birthday.first_name}'s birthday is on {birthday.date}!"
        from_email = 'bb.i.r.t.h.d.a.y.b.l.a.s.t.e.rr@gmail.com'
        to_email = birthday.email  # Email of user

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        # Connection to email SMTP server (currently Gmail)
        try:
            smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
            smtp_server.starttls()
            smtp_server.login('bb.i.r.t.h.d.a.y.b.l.a.s.t.e.rr@gmail.com', 'rhyn yrpe cigl vnfq') # Credentials (username, passkey)

            # Send email
            smtp_server.sendmail(from_email, to_email, msg.as_string())
            smtp_server.quit()
            print(f"Email reminder sent for {birthday.first_name}'s birthday.")
        except Exception as e:
            print(f"Error sending email: {str(e)}")

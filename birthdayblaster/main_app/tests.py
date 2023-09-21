from django.test import TestCase

from django.test import TestCase
from django.utils import timezone
from .models import Birthday
from .utils import send_birthday_reminders
from django.contrib.auth.models import User

# Create your tests here.

###### Test for birthday reminder email and email scheduling ######

### To run this test:
##### 1. Update the test email address below to desired test email address to receive test email notification
##### 2. Navigate to '~/Pod1-Project-3/birthdayblaster/' in the Terminal
##### 3. Run command: 'python3 manage.py test main_app'
##### 4. After the test runs, verify the test email address received the notification

from django.contrib.auth.models import User

class BirthdayReminderTestCase(TestCase):
    def test_send_birthday_reminders(self):
        # Test user
        test_user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            ###
            email="srtm88@gmail.com"  ### Test email address to receive test email notification ###
            ###
        )

        # Test birthday
        future_date = timezone.now() + timezone.timedelta(days=10)
        test_birthday = Birthday.objects.create(
            first_name="Test",
            last_name="User",
            date=future_date,
            user=test_user
        )

        # Send reminder email function
        send_birthday_reminders()

####################################################################
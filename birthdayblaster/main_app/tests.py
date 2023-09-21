from django.test import TestCase

from django.test import TestCase
from django.utils import timezone
from .models import Birthday
from .utils import send_birthday_reminders
from django.contrib.auth.models import User

# Create your tests here.
from django.contrib.auth.models import User  # Import User model

class BirthdayReminderTestCase(TestCase):
    def test_send_birthday_reminders(self):
        # Create a test user
        test_user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        # Create a test birthday instance associated with the test user
        future_date = timezone.now() + timezone.timedelta(days=10)
        test_birthday = Birthday.objects.create(
            first_name="Test",
            last_name="User",
            date=future_date,
            email="r.tom.sears@gmail.com",  # Replace with a valid email address
            user=test_user  # Associate with the test user
            # Add other required fields
        )

        # Call the function to send reminders
        send_birthday_reminders()


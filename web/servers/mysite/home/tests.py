from django.test import TestCase
from django.core.mail import send_mail
from django.conf import settings

# Create your tests here.

status = send_mail('[confirm]', 'Message : Your code is ...', 'bookingroom.group@gmail.com', ['kudohdtt@gmail.com'], fail_silently=False)
print(status)
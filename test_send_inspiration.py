import os
import smtplib
import unittest

from send_inspiration import send_email

EMAIL_TO = os.environ.get('EMAIL_TO')

def test_send_email():
    send_email_to(EMAIL_TO)
    self.assertEmailSent(to=EMAIL_TO)
    self.assertEqual(len(self.get_sent_messages()), 1)

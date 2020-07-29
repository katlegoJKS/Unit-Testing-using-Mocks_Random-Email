import os
import smtplib
import unittest

from send_inspiration import send_email

EMAIL_TO = os.environ.get('EMAIL_TO')

class TestSendEmail(unittest.TestCase):

    def test_send_email(self):
        # send_email()
        # assertEmailSent(to=EMAIL_TO)
        self.assertEqual(len(self.get_sent_messages()), 1)
   
if __name__ == '__main__':
    unittest.main()    

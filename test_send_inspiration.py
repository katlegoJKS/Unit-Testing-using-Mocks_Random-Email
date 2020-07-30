import os
import smtplib
import unittest

from send_inspiration import send_email
from mock import patch, call

EMAIL_LOGIN = os.environ.get('EMAIL_LOGIN')
EMAIL_TO = os.environ.get('EMAIL_TO')

class TestSendEmail(unittest.TestCase):

    def test_send_email(self):
        with patch("smtplib.SMTP") as mock_smtp:
            From_Address = EMAIL_LOGIN
            To_Address = EMAIL_TO
            
        send_email()
   
if __name__ == '__main__':
    unittest.main()    

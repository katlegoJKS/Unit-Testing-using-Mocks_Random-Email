import smtplib, unittest
from unittest.mock import Mock
from send_inspiration import main
import logging

mock = Mock()
m = mock.Mock()

class send_inspiration(unittest.TestCase):
    def set_up(self):
        self.emails = []
    
    def test_get_contacts(self,*args):
        for i in self.emails:
            self.assertTrue(i == main(),'Incorrect')
        s = 'katlego.malatjie@umuzi.org'
        self.assertEqual(s.split(), ['katlego.malatjie@umuzi.org'])
        with self.assertRaises(TypeError):
            s.split(2)
            self.assertEqual(len(s.emails), 2)
            self.assertEqual(s.emails[0].frm, 'katlego.malatjie@umuzi.org')
            self.assertEqual(s.emails[0].to, ['katlego.malatjie@umuzi.org'])
            self.assertEqual(s.emails[0].msg, 'This is TEST')
            self.assertEqual(m.get_contacts) == False

    def tear_down(self):
        self.emails = None

if __name__ == '__main__':
    unittest.main()
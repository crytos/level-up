"""test_main.py"""

import unittest
from signup import Signup


class SignupTestCase(unittest.TestCase):
    """Runs test for signup module"""

    def test_if_signup_object_is_created(self):
        """"test creation of signup object"""
        signup = Signup()
        self.assertIsInstance(signup, Signup)

    def test_if_a_field_is_not_filled(self):
        """"test if there is a missing parameter for signup form"""
        signup = Signup('julius', 'mubajje', 256)
        self.assertTrue(signup.message['err'] == True)
        self.assertFalse(signup.message['msg'] == 'Successfully Registered')
        self.assertFalse(signup.count_users() == 1)

    def test_if_all_fields_are_filled_but_some_are_invalid(self):
        """"test if all fields are filled but some are invalid"""
        signup = Signup("julius123", "m", 256, 758572829,
                        'jay@gmail.com', 'secret@123')
        self.assertTrue(signup.message['err'] == True)
        self.assertFalse(signup.message['msg'] == 'Successfully Registered')
        self.assertFalse(signup.count_users() == 1)

    def test_if_all_fields_are_filled_and_valid(self):
        """"test if all fields are filled and valid"""
        signup = Signup("julius", "mubajje", 256, 758572829,
                        'jay@gmail.com', 'secret@123')
        self.assertTrue(signup.message['err'] == False)
        self.assertTrue(signup.message['msg'] == 'Successfully Registered')
        self.assertIn(signup.message['msg'], 'Successfully Registered')
        self.assertTrue(signup.count_users() == 1)

    def tearDown(self):
        """"empty users list in signup"""
        return Signup.empty_users()

    # def test_when_afield_isnot_filled(self):
    #     """"test if there is a missing parameter for signup form"""
    #     signup = Signup('julius', 'mubajje', 256)
    #     self.assertTrue(signup.message['err'] == True)

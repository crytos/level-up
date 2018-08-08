"""validate_email.py"""
from validate.base import Validate


class ValidateEmail(Validate):
    """validates Email"""

    def __init__(self, value):
        super().__init__(value)
        self.message = {
            'err': True,
            'msg': ''
        }
        self.value = str(value)
        self.v_email()

    # main email validator method

    def v_email(self):
        if super(ValidateEmail, self).check_length(6, 35):
            if self.__email_verify():
                if "@" in self.value:
                    email = self.value.split("@")
                    if len(email) == 2:
                        if "." in email[1] and len(email[1]) > 4 and len(email[0]) > 1:
                            dot = email[1].split(".")
                            if len(dot) == 2 and len(dot[1]) > 1 and len(dot[0]) > 1:
                                self.message['err'] = False
                                return True
        self.message['err'] = True
        self.message['msg'] = self.value+' is an invalid Email'

    # validate characters in the email

    def __email_verify(self):
        check_list = self.__char_list()
        for character in list(self.value):
            if character not in check_list:
                return False
        return True

    # returns a list of characters allowed in the email

    def __char_list(self):
        alphas = [chr(i) for i in range(ord('a'), ord('z')+1)]
        nums = [str(i) for i in range(10)]
        chars = ['@', '.', '-', '_']
        check_list = alphas + nums + chars
        return check_list

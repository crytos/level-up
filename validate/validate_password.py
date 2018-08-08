"""validate_password.py"""
from validate.base import Validate

class ValidatePassword(Validate):
    """validates Password"""

    def __init__(self, value):
        super().__init__(value)
        self.v_password()

    #check password length

    def v_password(self):
        if super(ValidatePassword, self).check_length(8, 50):
            self.message['err'] = False
            return True
        self.message['err'] = True
        self.message['msg'] = "min 8 characters for password please!"

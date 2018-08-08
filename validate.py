"""validate.py"""


class Validate():
    """""Base Validator"""

    def __init__(self, value):
        self.value = value
        # return the error status and validation message
        self.message = {
            'err': True,
            'msg': ''
        }

    # check if the string is an alpha

    def check_alpha(self):
        """""validates alpha"""
        value = str(self.value)
        if value.isalpha():
            self.message['err'] = False
            self.message['msg'] = ''
            return True
        else:
            self.message['err'] = True
            self.message['msg'] = value+' is not alphabetic'
            return False

    # check if the string is a decimal

    def check_int(self):
        """""validates int"""
        value = str(self.value)
        if value.isdecimal():
            self.message['err'] = False
            self.message['msg'] = ''
            return True
        else:
            self.message['err'] = True
            self.message['msg'] = value+' is not a number'
            return False

    # check the length of the string

    def check_length(self, mini=3, maxi=15):
        """""validates length"""
        value = str(self.value)
        if len(value) < mini:
            self.message['err'] = True
            self.message['msg'] = value+' is too short'
            return False
        elif len(value) > maxi:
            self.message['err'] = True
            self.message['msg'] = value+' is too long'
            return False
        else:
            self.message['err'] = False
            return True


class ValidateName(Validate):
    """validates names"""

    def __init__(self, value):
        super().__init__(value)
        self.v_name()

    # validate name by calling the base validator class methods

    def v_name(self):
        if super(ValidateName, self).check_length():
            if super(ValidateName, self).check_alpha():
                return True


class ValidateCode(Validate):
    """validates code"""

    def __init__(self, value):
        super().__init__(value)
        self.v_code()

    # validate code by calling the base validator class methods

    def v_code(self):
        if super(ValidateCode, self).check_length(1, 3):
            if super(ValidateCode, self).check_int():
                return True


class ValidatePhone(Validate):
    """validates Phone"""

    def __init__(self, value):
        super().__init__(value)
        self.v_phone()

    # validate phone by calling the base validator class methods

    def v_phone(self):
        if super(ValidatePhone, self).check_length(9, 9):
            if super(ValidatePhone, self).check_int():
                return True


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
        

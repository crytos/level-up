"""base.py"""

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

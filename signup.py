""""signup.py"""
from validate import ValidateName, ValidateCode


class Signup():
    """signup base for user input authentication"""

    #List of users
    __users = []

    def __init__(self, firstname='', lastname='', code=''):
        self.firstname = firstname
        self.lastname = lastname
        self.code = code
        # signup response message
        self.message = {
            'err': True,
            'msg': ''
        }
        # run all validation methods
        self.__start_validation()

    # validate first name

    def check_first_name(self):
        check = ValidateName(self.firstname)
        if check.message['err']:
            self.message['err'] = True
            self.message['msg'] = check.message['msg']
            return False
        self.message['err'] = False
        return True

    # validate last name

    def check_last_name(self):
        check = ValidateName(self.lastname)
        if check.message['err']:
            self.message['err'] = True
            self.message['msg'] = check.message['msg']
            return False
        self.message['err'] = False
        return True

    # validate code

    def check_code(self):
        check = ValidateCode(self.code)
        if check.message['err']:
            self.message['err'] = True
            self.message['msg'] = check.message['msg']
            return False
        self.message['err'] = False
        return True

    # check all validation methods for error

    def __start_validation(self):
        if self.check_first_name():
            if self.check_last_name():
                if self.check_code():
                    self.message['msg'] = 'Successfully Registered'
                    self.__users.append({
                        'first name': self.firstname,
                        'last name': self.lastname,
                        'code': self.code
                    })
                    return True

    # static method that gets all users added
    @staticmethod
    def get_users():
        return Signup.__users

    # static method that counts all users added
    @staticmethod
    def count_users():
        return len(Signup.get_users())

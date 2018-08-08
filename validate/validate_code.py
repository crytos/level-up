"""validate_code.py"""

from validate.base import Validate


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

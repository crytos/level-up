"""validate_phone.py"""

from validate.base import Validate


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

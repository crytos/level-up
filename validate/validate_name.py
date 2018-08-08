"""validate_name.py"""
from validate.base import Validate


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

"""Subtraction Class"""
from calculator.operations.calculation import Calculation


class Subtraction(Calculation):  # pylint: disable=too-few-public-methods
    """Subtraction class"""

    def get_result(self):
        """Returns difference between two numbers"""
        result = self.values[0]
        for val in self.values[1:]:
            result -= val
        return result

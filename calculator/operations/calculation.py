"""Calculation Class"""

class Calculation: #pylint: disable=too-few-public-methods
    """Calculation class"""

    def __init__(self, *args):
        """Default constructor"""
        self.value = []
        for arg in args:
            self.values.append(arg)
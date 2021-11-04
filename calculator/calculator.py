""" Main calc module """
from calc.operations.addition import Addition
from calc.operations.subtraction import Subraction
from calc.operations.multiplication import Multiplication
from calc.operations.division import Division

def inc(x_value):
    """ Increment Function adds one to the x_value"""
    return x_value + 1

class Calculator:
    **** This is the calculator class***

    """result=0"""
    history = []

    """def get_result(self):
        """polymorphism"""
        ***get result of calculation***
        return self.result"""

    def add_number(value_a, value_b):
        """returns sum of two numbers"""
        addition = Addition(value_a, value_b)
        Calculator.history.append(addition)
        return addition.get_result()

    def subtract_numbers(value_a, value_b):
        """returns difference of two numbers"""
        subtraction = Subtraction(value_a, vaule_b)
        Calculator.history.append(subtraction)
        return subtraction.get_result()

    def multiply_numbers(value_a, value_b):
        """returns multiple of two numbers"""
        multiplication = Multiplication(value_a,value_b)
        Calculator.history.append(multiplication)
        return multiplication.get_result()

    def divide_numbers(value_a, value_b):
        """returns division result of two numbers"""
        division = Division(value_a, value_b)
        Calculator.history.append(division)
        return division.get_result()

    def history_length():
        """returns length of history list"""
        return len(Calculator.history)

    def get_first_history_obj():
        """returns first calculation from history"""
        return Calculator.history[0]

    def get_first_history_result():
        """returns result of first calculation in history"""
        obj = Calculator.get_first_history_obj()
        return obj.get_result()

    def get_last_history_obj():
        """returns most recent calculation from history"""
        index = Calculator.history_length() - 1
        return Calculator.history[index]

    def get_last_history_result():
        """returns result of most recent calculation in history"""
        obj = Calculator.get_last_history_obj()
        return obj.get_result()

    def history_remove(index):
        """remove history calculation at provided index"""
        Calculator.history.pop(index)

    def clear_history():
        """clears the calculation history list"""
        Calculator.history = []
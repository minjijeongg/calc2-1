""" Main calc module """
from calculator.operations.addition import Addition
from calculator.operations.subtraction import Subtraction
from calculator.operations.multiplication import Multiplication
from calculator.operations.division import Division


class Calculator:
    """This is the calculator class"""
    history = []


    @staticmethod
    def add_numbers(value_a, value_b):
        """returns sum of two numbers"""
        addition = Addition(value_a, value_b)
        Calculator.history.append(addition)
        return addition.get_result()

    @staticmethod
    def subtract_numbers(value_a, value_b):
        """returns difference of two numbers"""
        subtraction = Subtraction(value_a, value_b)
        Calculator.history.append(subtraction)
        return subtraction.get_result()

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """returns multiple of two numbers"""
        multiplication = Multiplication(value_a,value_b)
        Calculator.history.append(multiplication)
        return multiplication.get_result()

    @staticmethod
    def divide_numbers(value_a, value_b):
        """returns division result of two numbers"""
        division = Division(value_a, value_b)
        Calculator.history.append(division)
        return division.get_result()

    @staticmethod
    def history_length():
        """returns length of history list"""
        return len(Calculator.history)

    @staticmethod
    def get_first_history_obj():
        """returns first calculation from history"""
        return Calculator.history[0]

    @staticmethod
    def get_first_history_result():
        """returns result of first calculation in history"""
        obj = Calculator.get_first_history_obj()
        return obj.get_result()

    @staticmethod
    def get_last_history_obj():
        """returns most recent calculation from history"""
        index = Calculator.history_length() - 1
        return Calculator.history[index]

    @staticmethod
    def get_last_history_result():
        """returns result of most recent calculation in history"""
        obj = Calculator.get_last_history_obj()
        return obj.get_result()

    @staticmethod
    def history_remove(index):
        """remove history calculation at provided index"""
        Calculator.history.pop(index)

    @staticmethod
    def clear_history():
        """clears the calculation history list"""
        Calculator.history = []

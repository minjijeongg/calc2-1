"""Testing Multiplication class"""
from calculator.operation.multiplication import Multiplication

def test_calculator_multiply_static():
    """Tests multiplication"""
    multiplication = Multiplication(5,2)
    assert multiplication.get_result() == 10
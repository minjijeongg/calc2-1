"""Testing Addition class"""
from calculator.operations.addition import Addition

def test_operation_addition():
    """Tests addition"""
    addition = Addition(1,2)
    assert addition.get_result() == 3
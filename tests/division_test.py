"""Testing Division class"""
from calculator.operations.division import Division


def test_calculator_subtract_static():
    """Test division"""
    division = Division(6,2)
    assert division.get_result() == 3
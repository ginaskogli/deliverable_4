import pytest 
from task_2_fractions import Fraction

@pytest.mark.parametrize("x, expected", [[Fraction(1, 2), Fraction(2, 4)], 
                                         [Fraction(3, 4), Fraction(7, 5)]])

class test_Fraction: #?
    def test__eq__():
        assert "x" == "expected"
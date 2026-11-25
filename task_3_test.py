from task_2_fractions import Fraction

def test__eq__() -> None:
    assert Fraction(1, 2) == Fraction(2, 4)

def test__ne__() -> None:
    assert Fraction(1, 2) != Fraction(4, 4)

def test__lt__() -> None:
    assert Fraction(1, 3) < Fraction(1, 2)

def test__le__() -> None:
    assert Fraction(1, 2) <= Fraction(4, 8)

def test__gt__() -> None:
    assert Fraction(1, 2) > Fraction(1, 5)

def test__ge__() -> None:
    assert Fraction(1, 2) >= Fraction(1, 3)

def test__add__() -> None:
    assert Fraction(1, 2) + Fraction(2, 4) == Fraction(1, 1)

def test__sub__() -> None:
    assert Fraction(8, 10) - Fraction(3, 10) == Fraction(1, 2)

def test__mul__() -> None:
    assert Fraction(1, 2) * Fraction(1, 3) == Fraction(1, 6)

def test__truediv__() -> None:
    assert Fraction(1, 2) / Fraction(4, 2) == Fraction(1, 4)

# Write a `test_temperature.py` script that imports the `Temperature` class and uses pytest for the following tests:
# 1. Initialization: Default unit, case-insensitive units, and read-only behavior.
# 2. Validation: Invalid unit strings and temperatures below absolute zero in "C", "F", and "K".
# 3. Conversions: Test conversion accuracy across reference points:
#     * Absolute zero ($-273.15^\circ\text{C} = -459.67^\circ\text{F} = 0\text{ K}$)
#     * Celsius–Fahrenheit crossover ($-40^\circ\text{C} = -40^\circ\text{F} = 233.15\text{ K}$)
#     * Freezing point of water ($0^\circ\text{C} = 32^\circ\text{F} = 273.15\text{ K}$)
#     * Human body temperature ($37^\circ\text{C} = 98.6^\circ\text{F} = 310.15\text{ K}$)
#     * Boiling point of water ($100^\circ\text{C} = 212^\circ\text{F} = 373.15\text{ K}$)
# 4. Round-trip conversions: Converting "C" -> "F" -> "K" -> "C" reproduces the original Temperature.
# 5. Cross-unit comparisons: Equality and ordering (<, <=, >, >=) across mixed units.
# 6. Formatting: Outputs of `str()` and `repr()`

import pytest

from task1_temperatures import Temperature


# 1. Initialization: Default unit, case-insensitive units, and read-only behavior.
def test_initialization():
    temp = Temperature(25, "C")

    assert temp.value == 25
    assert temp.unit == "C"


def test_default_unit():
    temp = Temperature(25)

    assert temp.value == 25
    assert temp.unit == "C"


def test_case_insensitive_units():
    temp_c = Temperature(25, "c")
    temp_f = Temperature(77, "f")
    temp_k = Temperature(298.15, "k")

    assert temp_c.unit == "C"
    assert temp_f.unit == "F"
    assert temp_k.unit == "K"


def test_read_only_attributes():
    """Testing the the read only attributes."""
    temp = Temperature(25, "C")

    # Testing the ability to change the temperature value
    with pytest.raises(AttributeError):
        temp.value = 30

    with pytest.raises(AttributeError):
        temp.unit = "F"


# 2. Validation: Invalid unit strings and temperatures below absolute zero in "C", "F", and "K".
def test_invalid_units():
    invalid_units = ["X", "celsius", ""]

    for unit in invalid_units:
        with pytest.raises(ValueError):
            Temperature(25, unit)


def test_below_absolute_zero():
    invalid_temperatures = [
        (-274, "C"),
        (-461, "F"),
        (-1, "K")
    ]

    for value, unit in invalid_temperatures:
        with pytest.raises(ValueError):
            Temperature(value, unit)

import pytest

from task1_temperatures import Temperature


# 1. Initialization: Default unit, case-insensitive units, and read-only behavior.
def test_initialization():
    """Test initialization with an explicitly provided unit."""
    temp = Temperature(25, "C")

    assert temp.value == 25
    assert temp.unit == "C"


def test_default_unit():
    """Test that celsius is the default unit."""
    temp = Temperature(25)

    assert temp.value == 25
    assert temp.unit == "C"


def test_case_insensitive_units():
    """Test that units are case-insensitive."""
    temp_c = Temperature(25, "c")
    temp_f = Temperature(77, "f")
    temp_k = Temperature(298.15, "k")

    assert temp_c.unit == "C"
    assert temp_f.unit == "F"
    assert temp_k.unit == "K"


def test_read_only_attributes():
    """Test that value and unit attributes are read-only."""
    temp = Temperature(25, "C")

    # Testing the ability to change the temperature value
    with pytest.raises(AttributeError):
        temp.value = 30

    with pytest.raises(AttributeError):
        temp.unit = "F"


# 2. Validation: Invalid unit strings and temperatures below absolute zero in "C", "F", and "K".
def test_invalid_units():
    """Test that invalid unit strings raise ValueError."""
    invalid_units = ["X", "celsius", ""]

    for unit in invalid_units:
        with pytest.raises(ValueError):
            Temperature(25, unit)


def test_below_absolute_zero():
    """Test that temperatures below absolute zero raise ValueError."""
    invalid_temperatures = [
        (-274, "C"),
        (-461, "F"),
        (-1, "K")
    ]

    for value, unit in invalid_temperatures:
        with pytest.raises(ValueError):
            Temperature(value, unit)


# 3. Conversions: Test conversion accuracy across reference points:
#     * Absolute zero (-273.15 C = -459.67 F = 0 K
#     * Celsius–Fahrenheit crossover -40 C = -40 F = 233.15 K
#     * Freezing point of water 0 C = 32 F = 273.15
#     * Human body temperature 37 C = 98.6 F = 310.15 K
#     * Boiling point of water 100 C = 212 F = 373.15 K

@pytest.mark.parametrize(
    "value, expected_f, expected_k",
    [
        [-273.15, -459.67, 0],
        [-40, -40, 233.15],
        [0, 32, 273.15],
        [37, 98.6, 310.15],
        [100, 212, 373.15]
    ]
)
def test_conversions(value, expected_f, expected_k):
    """Testing convertion between different referance values.
    Using abs which is the absolute tolerance allowed, and rel the relative toleranse is sett to 0."""

    temp = Temperature(value, "C")

    assert temp.to_celsius() == pytest.approx(value, abs=Temperature.tolerance, rel=0)
    assert temp.to_fahrenheit() == pytest.approx(expected_f, abs=Temperature.tolerance, rel=0)
    assert temp.to_kelvin() == pytest.approx(expected_k, abs=Temperature.tolerance, rel=0)


# 4. Round-trip conversions: Converting "C" -> "F" -> "K" -> "C" reproduces the original Temperature.

@pytest.mark.parametrize("start_value", [-40, 25, 100])
def test_round_trip_conversions(start_value):
    """Test round-trip conversion from Celsius to Fahrenheit, Kelvin and back to Celsius."""
    temp_c = Temperature(start_value, "C")

    temp_f = temp_c.convert_to("F")
    temp_k = temp_f.convert_to("K")
    temp_c_again = temp_k.convert_to("C")

    assert temp_c_again == temp_c


# 5. Cross-unit comparisons: Equality and ordering (<, <=, >, >=) across mixed units.

def test_comparisons():
    """Test all six comparison operators using Celsius temperatures."""
    temp_1 = Temperature(20, "C")
    temp_2 = Temperature(25, "C")

    # Testing equality and inequality
    assert (temp_1 == temp_2) is False
    assert temp_1 != temp_2

    # Testing ordering
    assert temp_1 < temp_2
    assert temp_1 <= temp_2
    assert (temp_1 > temp_2) is False
    assert (temp_1 >= temp_2) is False
    assert temp_2 > temp_1
    assert temp_2 >= temp_1


def test_cross_unit_comparisons():
    """Test comparisons between different temperature units."""
    temp_c = Temperature(0, "C")
    temp_f = Temperature(32, "F")

    assert temp_c == temp_f
    assert (temp_c != temp_f) is False
    assert temp_c <= temp_f

    # 20 C is higher than 50 F
    temp_c = Temperature(20, "C")
    temp_f = Temperature(50, "F")

    assert temp_c > temp_f
    assert (temp_c < temp_f) is False
    assert temp_c >= temp_f
    assert (temp_c <= temp_f) is False

    temp_k = Temperature(0, "K")
    temp_c = Temperature(-273.15, "C")

    assert temp_k == temp_c
    assert temp_k >= temp_c
    assert (temp_k != temp_c) is False
    assert temp_k <= temp_c

@pytest.mark.parametrize("other", [20, 20.0, "20", "", None])
def test_comparisons_with_other_types(other):
    """Test that comparison methods return NotImplemented for orher types."""
    temp = Temperature(20, "C")

    assert temp.__eq__(other) is NotImplemented
    assert temp.__ne__(other) is NotImplemented
    assert temp.__lt__(other) is NotImplemented
    assert temp.__le__(other) is NotImplemented
    assert temp.__gt__(other) is NotImplemented
    assert temp.__ge__(other) is NotImplemented


# 6. Formatting: Outputs of str() and repr()

def test_str():
    """Test the human-readable string representation of temperature."""
    temp_c = Temperature(25, "C")
    temp_f = Temperature(77, "F")
    temp_k = Temperature(300, "K")

    assert str(temp_c) == "25.00 °C"
    assert str(temp_f) == "77.00 °F"
    assert str(temp_k) == "300.00 K"


def test_repr():
    """Test the unambiguous representation of Temperature."""
    temp_c = Temperature(25, "C")
    temp_f = Temperature(77, "F")
    temp_k = Temperature(300, "K")

    assert repr(temp_c) == 'Temperature(25, "C")'
    assert repr(temp_f) == 'Temperature(77, "F")'
    assert repr(temp_k) == 'Temperature(300, "K")'

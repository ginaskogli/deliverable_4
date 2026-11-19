# Temperature class - supporting C, F, K
# initialised bt value and unit 
#     raise ValueError if not c, f, k or temperature under absolute zero (0K)
# tolerance 1e-9 for floats
# expose value and unit as read only attributes

# convertions
# to_celsius(self) -> float :
# From Kelvin: C = K - 273.15
# From Fahrenheit: C = (F - 32) * 5/9

# to_fahrenheit(self) -> float :
# From Celsius: F = C * 9/5 + 32
# From Kelvin: F = (K - 273.15) * 9/5 + 32

# to_kelvin(self) -> float :
# From Celsius: K = C + 273.15
# From Fahrenheit: K = (F - 32) * 5/9 + 273,15

# convert_to(self, target_unit: str) -> Temperature :
# Returns a new Temperature instance converted to target_unit (case-
# insensitive), raising ValueError if target_unit is invalid.

from typing import Literal


class Temperature:

    def __init__(
            self, 
            value: int | float, 
            unit: Literal["C", "F", "K"]
            ) -> None:

        # Check if a valid unit is given
        if unit not in ("C", "F", "K"):
            raise ValueError("Unit must be C, F og K")

        self._value = value
        self._unit = unit

        # Check if value is over absolute zero

    def to_celsius(self) -> float:
        """Converts temperature to celsius."""
        # From Kelvin: C = K - 273.15
        # From Fahrenheit: C = (F - 32) * 5/9

        # Kelvin to Celsius
        if self._unit == "K":
            celcius = self._value - 273.15

        # Fahrenheit to Celsius
        elif self._unit == "F":
            celcius = (self._value - 32) * (5 / 9)

        # Celsius to Celcius
        else:
            celcius = self._value

        return celcius

    def to_fahrenheit(self) -> float:
        """Converts temperature to farenheit."""
        # From Celsius: F = C * 9/5 + 32
        # From Kelvin: F = (K - 273.15) * 9/5 + 32

        # Celsius to Fahrenheit
        if self._unit == "C":
            fahrenheit = self._value * (9 / 5) + 32

        # Kelvin to Fahrenheit
        elif self._unit == "K":
            fahrenheit = (self._value - 273.15) * (9 / 5) + 32

        # Fahrenheit to Fahrenheit
        else:
            fahrenheit = self._value

        return fahrenheit

    def to_kelvin(self) -> float:
        """Converts temperature to kelvin"""
        # From Celsius: K = C + 273.15
        # From Fahrenheit: K = (F - 32) * 5/9 + 273,15

        # Celsius to Kelvin
        if self._unit == "C":
            kelvin = self._value + 273.15

        # Fahrenheit to Kelvin
        elif self._unit == "F":
            kelvin = (self._value - 32) * (5 / 9) + 273.15

        # Kelvin to Kelvin
        else:
            kelvin = self._value

        return kelvin

    def convert_to(self, target_unit: str) -> Temperature:
        # Returns a new Temperature instance converted to target_unit (case-
        # insensitive), raising ValueError if target_unit is invalid.
        pass

tempK = Temperature(300, "K")
print(tempK.to_celsius())

tempC = Temperature(300, "C")
print(tempC.to_fahrenheit())

tempF = Temperature(300, "F")
print(tempF.to_kelvin())

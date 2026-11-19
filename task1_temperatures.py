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

    def __init__(self, value: float, unit: Literal["C", "F", "K"]) -> None:

        self._value = value
        self._unit = unit

    def to_celsius(self) -> float:
        # From Kelvin: C = K - 273.15
        # From Fahrenheit: C = (F - 32) * 5/9
        if self._unit == "K":
            celcius = self._value - 273.15            # Kelvin to Celsius

        elif self._unit == "F":
            celcius = (self._value - 32) * 5 / 9      # Farenheit to Celsius

        else:
            celcius = self._value

        return celcius

    def to_fahrenheit(self) -> float:
        # From Celsius: F = C * 9/5 + 32
        # From Kelvin: F = (K - 273.15) * 9/5 + 32
        pass

    def to_kelvin(self) -> float:
        # From Celsius: K = C + 273.15
        # From Fahrenheit: K = (F - 32) * 5/9 + 273,15
        pass

    def convert_to(self, target_unit: str) -> Temperature:
        # Returns a new Temperature instance converted to target_unit (case-
        # insensitive), raising ValueError if target_unit is invalid.
        pass

temp = Temperature(300, "K")
print(temp.to_celsius())

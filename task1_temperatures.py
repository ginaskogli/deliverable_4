from types import NotImplementedType


class Temperature:
    """Represent a temperature in Celsius, Farenheit or Kelvin"""

    # Tolerance for floating point values
    tolerance: float = 1e-9

    def __init__(
            self,
            value: int | float,
            unit: str = "C"
            ) -> None:
        """
        Initialize a Temperature instance.

        Arguments:
            value: The numerical temperature value.
            unit: The temperature unit ("C", "F", "K").
                Defaults to Celsius.

        Raises:
            ValueError: If the unit is invalid or the temperature
                is below absolute zero."""

        # Convert all units to upper case
        unit = unit.upper()

        # Check if a valid unit is given
        if unit not in ("C", "F", "K"):
            raise ValueError("Unit must be C, F og K")

        self._value = value     # read only atribute
        self._unit = unit       # read only atribute

        # Check if value is over absolute zero, given tolerance
        if self.to_kelvin() < -self.tolerance:
            raise ValueError("Temperature cannot be below absolute zero")

    def to_celsius(self) -> float:
        """Converts temperature to Celsius.

        Returns:
            The temperature in degrees Celsius."""

        # Kelvin to Celsius: C = K - 273.15
        if self._unit == "K":
            celcius = self._value - 273.15

        # Fahrenheit to Celsius: C = (F - 32) * 5/9
        elif self._unit == "F":
            celcius = (self._value - 32) * (5 / 9)

        # Celsius to Celcius: C = C
        else:
            celcius = self._value

        return celcius

    def to_fahrenheit(self) -> float:
        """Converts temperature to Fahrenheit.

            Returns:
                The temperature in degrees Fahrenheit."""

        # Celsius to Fahrenheit: F = C * 9/5 + 32
        if self._unit == "C":
            fahrenheit = self._value * (9 / 5) + 32

        # Kelvin to Fahrenheit: F = (K - 273.15) * 9/5 + 32
        elif self._unit == "K":
            fahrenheit = (self._value - 273.15) * (9 / 5) + 32

        # Fahrenheit to Fahrenheit: F = F
        else:
            fahrenheit = self._value

        return fahrenheit

    def to_kelvin(self) -> float:
        """Converts temperature to Kelvin.

        Returns:
            The temperature in Kelvin."""

        # Celsius to Kelvin: K = C + 273.15
        if self._unit == "C":
            kelvin = self._value + 273.15

        # Fahrenheit to Kelvin: K = (F - 32) * 5/9 + 273.15
        elif self._unit == "F":
            kelvin = (self._value - 32) * (5 / 9) + 273.15

        # Kelvin to Kelvin: K = K
        else:
            kelvin = self._value

        return kelvin

    def convert_to(self, target_unit: str) -> Temperature:
        """ Convert the temperature to a different unit,
        by taking in a target unit, it returns a new temperature instanse.

        Arguments:
            target_unit: The unit to convert to ("C", "F" or "K").

        Returns:
            A new Temperature instance in the target unit.

        Raises:
            ValueError: If the target unit is invalid."""
        # Returns a new Temperature instance converted to target_unit (case-
        # insensitive), raising ValueError if target_unit is invalid.

        # Converts target unit to upper case
        target_unit = target_unit.upper()

        if target_unit == "C":
            new_value = self.to_celsius()
        elif target_unit == "F":
            new_value = self.to_fahrenheit()
        elif target_unit == "K":
            new_value = self.to_kelvin()
        else:
            raise ValueError("Invalid unit, unit must be C, F or K.")

        return Temperature(new_value, target_unit)

    def __repr__(self) -> str:
        """Return an unambiguous string representation of the Temperature object.

        Returns:
            str: A string that represents the object, including its value
            and unit, for example Temperature(25, "C)."""
        return f"Temperature({self._value}, \"{self._unit}\")"

    def __str__(self) -> str:
        """Return a human-readable representation of the temperature.

        The temperature value is formatted to two decimal places.
        Celsius and Fahrenheit include a degree symbol, while Kelvin
        is written without one.

        Returns:
            str: A formatted temperature, for eksample "25.00 °C"""

        # Adds the degree symbol to Celsius and Fahrenheit
        unit_symbol = f"°{self._unit}" if self._unit in ("C", "F") else "K"

        return f"{self._value:.2f} {unit_symbol}"

# Contain all six comparisons (==, !=, <, <=, >, >=) so temperatures can be compared across 
# different units (`Temperature(0, "C") == Temperature(32, "F")`). 
# Should return `NotImplemented` if a `Temperature` instance is compared to a non-Temperature instance.

    # Comparison functions
    # kan lage en felles hjelpefunskjon
    # har ferdige funksjoner for sammenlikning inkludert i python

    # for å sammenlikne må vi konvertere til en felles enhet - velger kelvin
    def compare_help(self, other: object) -> tuple[float, float] | NotImplementedType:
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_kelvin(), other.to_kelvin()

    # == equal to
    def __eq__(self, other) -> bool | NotImplementedType:
        """Compare two temperatures for equality."""

        comparison = self.compare_help(other)

        if comparison is NotImplemented:
            return NotImplemented

        self_kelvin, other_kelvin = comparison

        # The absolute difference is less than og equal to the tolerance
        return abs(self_kelvin - other_kelvin) <= self.tolerance

    # != not equal to
    def __ne__(self, other) -> bool | NotImplementedType:
        """Compare two temperatures for none equality."""

        comparison = self.compare_help(other)

        if comparison is NotImplemented:
            return NotImplemented

        self_kelvin, other_kelvin = comparison

        # The absolute difference is greater than the tolerance
        return abs(self_kelvin - other_kelvin) > self.tolerance

    # < less than
    def __lt__(self, other) -> bool | NotImplementedType:
        """Compare two temperatures, is one less than the other."""

        comparison = self.compare_help(other)

        if comparison is NotImplemented:
            return NotImplemented

        self_kelvin, other_kelvin = comparison

        # Is self less than other
        return self_kelvin < other_kelvin

    # <= less than or equal to
    def __le__(self, other) -> bool | NotImplementedType:
        """Compare two temperatures, is one less than or equal to the other."""

        comparison = self.compare_help(other)

        if comparison is NotImplemented:
            return NotImplemented

        self_kelvin, other_kelvin = comparison

        # Is self less than or equal to the other
        return self_kelvin <= other_kelvin

    # > greater than
    def __gt__(self, other) -> bool | NotImplementedType:
        """Compare two temperatures, is one greater than the other."""

        comparison = self.compare_help(other)

        if comparison is NotImplemented:
            return NotImplemented

        self_kelvin, other_kelvin = comparison

        # Is self greater than other
        return self_kelvin > other_kelvin

    # >= greater than or equal
    def __ge__(self, other) -> bool | NotImplementedType:
        """Compare two temperatures, is one greater than or equal to the other."""

        comparison = self.compare_help(other)

        if comparison is NotImplemented:
            return NotImplemented

        self_kelvin, other_kelvin = comparison

        # Is self greater than or equal to the other
        return self_kelvin >= other_kelvin

temp1 = Temperature(0, "C")
temp2 = Temperature(32, "F")
temp3 = Temperature(100, "C")

print(temp1 == temp2)  # True
print(temp1 != temp3)  # True
print(temp1 < temp3)   # True
print(temp1 <= temp2)  # True
print(temp3 > temp1)   # True
print(temp3 >= temp1)  # True

print(temp1 == 25)
# temp = Temperature(7, "K")

# print(repr(temp))
# print(str(temp))
# print(temp)

# tempk = Temperature(0, "K")
# print(tempk.to_celsius())

# tempc = Temperature(300, "C")
# print(tempk.to_fahrenheit())

# tempf = Temperature(300, "F")
# print(tempf.to_kelvin())

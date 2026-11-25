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

        self._value = value
        self._unit = unit

        # Check if value is over absolute zero, given tolerance
        if self.to_kelvin() < -self.tolerance:
            raise ValueError("Temperature cannot be below absolute zero")

    @property
    def value(self) -> float:
        """Return the numerical temperature value.

        Returns:
            The temperature value in the unit specified by the
            unit attribute. This property is read-only."""

        return self._value

    @property
    def unit(self) -> str:
        """Return the temperature unit.

        Returns:
            The temperature unit as a string ("C", "F, or "K").
            This property is read-only."""
        return self._unit

    def to_celsius(self) -> float:
        """Converts temperature to Celsius.

        Returns:
            The temperature in degrees Celsius."""

        if self._unit == "K":
            celcius = self._value - 273.15

        elif self._unit == "F":
            celcius = (self._value - 32) * (5 / 9)

        else:
            celcius = self._value

        return celcius

    def to_fahrenheit(self) -> float:
        """Converts temperature to Fahrenheit.

            Returns:
                The temperature in degrees Fahrenheit."""

        if self._unit == "C":
            fahrenheit = self._value * (9 / 5) + 32

        elif self._unit == "K":
            fahrenheit = (self._value - 273.15) * (9 / 5) + 32

        else:
            fahrenheit = self._value

        return fahrenheit

    def to_kelvin(self) -> float:
        """Converts temperature to Kelvin.

        Returns:
            The temperature in Kelvin."""

        if self._unit == "C":
            kelvin = self._value + 273.15

        elif self._unit == "F":
            kelvin = (self._value - 32) * (5 / 9) + 273.15

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
            and unit, for example Temperature(25, "C")."""
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

    def compare_help(self, other: object) -> tuple[float, float] | NotImplementedType:
        """Convert two Temperature instances to Kelvin for comparison.

        Arguments:
            other: the oject to compare with self.

        Returns:
            A tuple containing both temperatures in Kelvin.

        Returns NotImplemented if other is not at Temperature instance. """
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_kelvin(), other.to_kelvin()

    def __eq__(self, other) -> bool | NotImplementedType:
        """Check whether two temperatures are equal.
        Temperatures are converted to Kelvin before comparison.
        A tolerance is used to account for floating-point precision.

        Arguments:
            other: The temperature to compare with self.

        Returns:
            True if the temperature are equal within the defined
            tolerance, otherwise False.

            Returns NotImplemented if other is not a temperature instance."""

        comparison = self.compare_help(other)

        if comparison is NotImplemented:
            return NotImplemented

        self_kelvin, other_kelvin = comparison

        # The absolute difference is less than og equal to the tolerance
        return abs(self_kelvin - other_kelvin) <= self.tolerance

    def __ne__(self, other) -> bool | NotImplementedType:
        """Compare two temperatures for none equality.
        Temperatures are converted to Kelvin before comparison.
        A tolerance is used to account for floating-point precision.

        Arguments:
            other: The temperature to compare with self.

        Returns:
            True if the temperature differ by more than the defined
            tolerance, otherwise False.

            Returns NotImplemented if other is not a temperature instance."""

        comparison = self.compare_help(other)

        if comparison is NotImplemented:
            return NotImplemented

        self_kelvin, other_kelvin = comparison

        # The absolute difference is greater than the tolerance
        return abs(self_kelvin - other_kelvin) > self.tolerance

    def __lt__(self, other) -> bool | NotImplementedType:
        """ Check whether this temperature is less than another temperature.
        Both temperatures are converted to Kelvin before comparison.

        Argumentss:
            other: The temperature to compare with self.

        Returns:
            True if self is less than other, otherwise False.

            Returns NotImplemented if other is not a Temperature instance."""
        comparison = self.compare_help(other)

        if comparison is NotImplemented:
            return NotImplemented

        self_kelvin, other_kelvin = comparison

        # Is self less than other
        return self_kelvin < other_kelvin

    def __le__(self, other) -> bool | NotImplementedType:
        """Check whether this temperature is less than or equal to another.
        Both temperatures are converted to Kelvin before comparison.

        Arguments:
            other: The temperature to compare with self.

        Returns:
            True if self is less than or equal to other, otherwise False.

            Returns NotImplemented if other is not a Temperature instance."""

        comparison = self.compare_help(other)

        if comparison is NotImplemented:
            return NotImplemented

        self_kelvin, other_kelvin = comparison

        # Is self less than or equal to the other
        return self_kelvin <= other_kelvin

    def __gt__(self, other) -> bool | NotImplementedType:
        """Check whether this temperature is greater than another temperature.
        Both temperatures are converted to Kelvin before comparison.

        Arguments:
            other: The temperature to compare with self.

        Returns:
            True if self is greater than other, otherwise False.

            Returns NotImplemented if other is not a Temperature instance."""
        comparison = self.compare_help(other)

        if comparison is NotImplemented:
            return NotImplemented

        self_kelvin, other_kelvin = comparison

        # Is self greater than other
        return self_kelvin > other_kelvin

    def __ge__(self, other) -> bool | NotImplementedType:
        """Check whether this temperature is greater than or equal to another.
        Both temperatures are converted to Kelvin before comparison.

        Arguments:
            other: The temperature to compare with self.

        Returns:
            True if self is greater than or equal to other, otherwise False.

            Returns NotImplemented if other is not a Temperature instance."""

        comparison = self.compare_help(other)

        if comparison is NotImplemented:
            return NotImplemented

        self_kelvin, other_kelvin = comparison

        # Is self greater than or equal to the other
        return self_kelvin >= other_kelvin

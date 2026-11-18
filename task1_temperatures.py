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

class Temperature(self, temp_value, temp_unit: C, F, K):

    def to_celsius(self) -> float:
    # From Kelvin: C = K - 273.15
    # From Fahrenheit: C = (F - 32) * 5/9
        break

    def to_fahrenheit(self) -> float :
    # From Celsius: F = C * 9/5 + 32
    # From Kelvin: F = (K - 273.15) * 9/5 + 32
    break

    def to_kelvin(self) -> float:
# From Celsius: K = C + 273.15
# From Fahrenheit: K = (F - 32) * 5/9 + 273,15
    break

    def convert_to(self, target_unit: str) -> Temperature :
# Returns a new Temperature instance converted to target_unit (case-
# insensitive), raising ValueError if target_unit is invalid.
    break 
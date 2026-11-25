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

from task1_temperatures import Temperature

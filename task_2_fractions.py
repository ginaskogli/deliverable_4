import math

class Fraction:
    #representing fractions

    def __init__(self, numerator: int, denominator: int) -> None:
        """
        Args:
            numerator: upper number in fraction. Integers only.
            denominator: lower number in fraction. Positive integers only.

        """
        self.numerator = numerator
        self.denominator = denominator

        # bytt til exeptions?:
        if not isinstance(numerator, int):
            raise TypeError("Numerator must be integer.")

        if not isinstance(denominator, int):
            raise TypeError("Denominator must be integer.")

        if denominator <= 0:
            raise ValueError("Denominator must be a positive number.")
        
    def __eq__(self, other):
        # ved int - True dersom ?
        #if (isinstance(other, int)):
        #    pass
        #else:
            #return self.numerator*other.denominator == other.numerator*self.denominator
        return self.numerator*other.denominator == other.numerator*self.denominator
    
    def __ne__(self, other) -> "Fraction":
        return self.numerator*other.denominator != other.numerator*self.denominator
    
    def __lt__(self, other) -> "Fraction":
        return self.numerator*other.denominator < other.numerator*self.denominator

    def __le__(self, other) -> "Fraction":
        return self.numerator*other.denominator <= other.numerator*self.denominator
    
    def __gt__(self, other) -> "Fraction":
        return self.numerator*other.denominator > other.numerator*self.denominator
    
    def __ge__(self, other) -> "Fraction":
        return self.numerator*other.denominator >= other.numerator*self.denominator

    # lcm is least common multiplier
    def __add__(self, other) -> "Fraction":
        lcm = abs(self.denominator * other.denominator) // math.gcd(self.denominator, other.denominator)
        num = (self.numerator*(lcm//self.denominator))+(other.numerator*(lcm//other.denominator))
        return Fraction(num, lcm)

    def __sub__(self, other) -> "Fraction":
        lcm = abs(self.denominator * other.denominator) // math.gcd(self.denominator, other.denominator)
        num = (self.numerator*(lcm//self.denominator))-(other.numerator*(lcm//other.denominator))
        return Fraction(num, lcm)

    def __mul__(self, other) -> "Fraction":
        return Fraction(self.numerator*other.numerator, self.denominator*other.denominator)

    def __truediv__(self, other) -> float:
        x = self.numerator*other.denominator
        y = self.denominator*other.numerator
        return x/y

my_number = Fraction(1, 2)
your_number = Fraction(1, 4)

#print(my_number == your_number)
#print(your_number<my_number)
#print(my_number+your_number)
print(my_number / your_number)

"""    
    def __add__(self, other):
        x = (self.numerator*other.denominator)+(other.numerator*self.denominator)
        y = self.denominator*other.denominator

        lcm = abs(x * y) // math.gcd(x, y)

        num = int(x/lcm)
        denom = int(y/lcm)

        return (num, denom)
"""







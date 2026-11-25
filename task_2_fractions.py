
import math

class Fraction:
    # Representing fractions

    def __init__(self, numerator: int, denominator: int) -> None:
        """
        Args:
            numerator: upper number in fraction. Integers only.
            denominator: lower number in fraction. Positive integers only.

        """

        if not isinstance(numerator, int):
            raise TypeError("Numerator must be integer.")

        if not isinstance(denominator, int):
            raise TypeError("Denominator must be integer.")

        if denominator <= 0:
            raise ValueError("Denominator must be a positive number.")

        # devide numerator and denominator by the largest number that they both can be devided by, without any rest.
        g = math.gcd(numerator, denominator)

        self.numerator = numerator // g
        self.denominator = denominator // g
        
    def __eq__(self, other) -> None:
        """
        Returns True if self is equal to other.
        """
        return self.numerator*other.denominator == other.numerator*self.denominator
    
    def __ne__(self, other) -> None:
        """
        Returns True if self is not equal to other.
        """
        return self.numerator*other.denominator != other.numerator*self.denominator
    
    def __lt__(self, other) -> None:
        """
        Returns True if self is less than other.
        """
        return self.numerator*other.denominator < other.numerator*self.denominator

    def __le__(self, other) -> None:
        """
        Returns True if self is less than or equal to other.
        """
        return self.numerator*other.denominator <= other.numerator*self.denominator
    
    def __gt__(self, other) -> None:
        """
        Returns True if self is greater than other.
        """
        return self.numerator*other.denominator > other.numerator*self.denominator
    
    def __ge__(self, other) -> None:
        """
        Returns True if self is greater than or equal to other.
        """
        return self.numerator*other.denominator >= other.numerator*self.denominator


    def __add__(self, other) -> "Fraction":
        return Fraction(
            self.numerator * other.denominator
            + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def __sub__(self, other) -> "Fraction":
        return Fraction(
            self.numerator * other.denominator
            - other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def __mul__(self, other) -> "Fraction":
        """
        Returns Fraction object of multiplication of two fractions.
        """ 
        return Fraction(self.numerator*other.numerator, self.denominator*other.denominator)

    def __truediv__(self, other) -> "Fraction":
        """
        Returns Fraction object of self devided by other.
        """ 
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)





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

        # bytt til exeptions:
        if not isinstance(numerator, int):
            raise TypeError("Numerator must be integer.")

        if not isinstance(denominator, int):
            raise TypeError("Denominator must be integer.")

        if denominator <= 0:
            raise ValueError("Denominator must be a positive number.")
        
    def __eq__(self, other):
        return self.numerator*other.denominator == other.numerator*self.denominator

    def __ne__(self, other):
        return self.numerator*other.denominator != other.numerator*self.denominator
    
    def __lt__(self, other): 
        return self.numerator*other.denominator < other.numerator*self.denominator

    def __le__(self, other):
        return self.numerator*other.denominator <= other.numerator*self.denominator
    
    def __gt__(self, other):
        return self.numerator*other.denominator > other.numerator*self.denominator
    
    def __ge__(self, other):
        return self.numerator*other.denominator >= other.numerator*self.denominator
    
    def __add__(self, other):
        
# def __radd__(self, other):
# def __sub__(self, other):
# def __rsub__(self, other):

my_number = Fraction(1, 2)
your_number = Fraction(1, 4)

#print(my_number == your_number)
#print(your_number<my_number)









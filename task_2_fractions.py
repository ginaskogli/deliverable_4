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

        assert numerator or denominator is not int, "Both numerator and denominator must be integers."
        assert denominator <= 0, "Denominator must be a positive number."


    def compare(self, numerator, denominator):
        pass

    def 

    pass






number = Fraction(8.99)
improved_number = compare(number)

x = 2/9
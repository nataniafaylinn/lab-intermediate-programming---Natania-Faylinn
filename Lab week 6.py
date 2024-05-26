from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def to_float(self):
        return self.numerator / self.denominator

    def get_rational(self):
        return f"{self.numerator}/{self.denominator}"
    
    def get_float(self):
        return self.to_float()

fraction = Fraction(1, 3)
print(fraction.get_rational())  
print(fraction.get_float())     

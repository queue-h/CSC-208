class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if numerator == 0:  # zero fraction stored as 0/1
            self._numerator = 0
            self._denominator = 1
            return
        else: #nonzero
            if (numerator < 0 and denominator > 0 or 
                numerator >= 0 and denominator < 0):
                sign = -1
            else:
                sign = 1
        # Calculate the GCD of numerator and denominator
        # using Euclid's algorithm
        a = abs(numerator)
        b = abs(denominator)
        while a % b != 0:
            tempA = a
            tempB = b
            a = tempB
            b = tempA % tempB
        self._numerator = abs(numerator) // b * sign
        self._denominator = abs(denominator) // b
        return
    
        
    def __eq__(self, other):
        return (self._numerator == other._numerator and
                self._denominator == other._denominator)
    
    def __float__(self):
        return self._numerator/self._denominator
    
    def __lt__(self, rhsValue) :
        return (self._numerator * rhsValue._denominator <              
                self._denominator * rhsValue._numerator)
    
    def __add__(self, rhsValue):
        num = (self._numerator * rhsValue._denominator + 
               self._denominator * rhsValue._numerator)
        den = self._denominator * rhsValue._denominator
        return Fraction(num, den) 

    def __str__(self):
        return str(self._numerator)+"/"+str(self._denominator)
    
    def __gt__(self, rhsValue) :
        return (self._numerator * rhsValue._denominator >              
                self._denominator * rhsValue._numerator)   
    
    def __sub__(self, rhsValue):
        num = (self._numerator * rhsValue._denominator - 
               self._denominator * rhsValue._numerator)
        den = self._denominator * rhsValue._denominator
        return Fraction(num, den)
    
    def __ne__(self, rhsValue):
        return not self == rhsValue
    
    def __le__(self, rhsValue):
        return not self > rhsValue
    
    def __mul__(self, rhsValue):
        if isinstance(rhsValue, Fraction):
            num = (self._numerator * rhsValue._numerator)
            den = self._denominator * rhsValue._denominator
            return Fraction(num, den)
        if isinstance(rhsValue, int):
            num = (self._numerator * rhsValue)
            den = self._denominator
            return Fraction(num, den)
        else:
            raise TypeError("Multiply Fraction object by "
                            "Fraction or int values only!")
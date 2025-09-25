class Fraction:
    def __init__(self, numerator, denominator = 1):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be 0")
        if numerator == 0:
            self._numerator = 0
            self._denominator = 1
        else:
            if (numerator > 0 and denominator >= 0) or (numerator >= 0 and denominator < 0):
                self.sign = -1
            else:
                self.sign = 1

        a = abs(numerator)
        b = abs(denominator)

        while a % b != 0:
            tempA = a
            tempB = b
            a = tempB
            b = tempA % tempB

        self._numerator = abs(numerator)
        self._denominator = abs(denominator)

    def __eq__(self, rhs_value):
        return (self._numerator == rhs_value.get_numerator()) and (self._denominator == rhs_value.get_denominator())

    def get_numerator(self):
        return self._numerator
    def get_denominator(self):
        return self._denominator



class Fraction:
    pass

class Fraction:

    def __init__(self, num: int, denom: int):

        self.num = int(num)
        self.denom = int(denom)

        if (denom == 0):
            raise ZeroDivisionError

        if denom < 0:
            self.num *= -1
            self.denom *= -1

        g_c_d = Fraction.greatest_common_divisor(self.num, self.denom)
        self.num //= g_c_d
        self.denom //= g_c_d

    def __eq__(self, other: Fraction):
        
        if isinstance(other, Fraction):
            self_simplified_num, self_simplified_denom = Fraction.get_simplified_num_and_denom(self)
            other_simplified_num, other_simplified_denom = Fraction.get_simplified_num_and_denom(other)
            return (self_simplified_num == other_simplified_num 
                    and self_simplified_denom == other_simplified_denom)

        return False

    def __ne__(self, other: Fraction):
        
        if isinstance(other, Fraction):
            self_simplified_num, self_simplified_denom = Fraction.get_simplified_num_and_denom(self)
            other_simplified_num, other_simplified_denom = Fraction.get_simplified_num_and_denom(other)
            return not self == other

        return True

    @staticmethod
    def greatest_common_divisor(a: int, b: int):

        # Euclidean algorithm
        while b != 0:

            t = b
            b = a % b
            a = t

        return a
    
    @staticmethod
    def get_simplified_num_and_denom(fraction: Fraction):

        g_c_d = Fraction.greatest_common_divisor(fraction.num, fraction.denom)
        return (fraction.num // g_c_d, fraction.denom // g_c_d)

    @staticmethod
    def least_common_multiple(a: int, b: int):

        if a == 0 or b == 0:
            return 0

        g_c_d = Fraction.greatest_common_divisor(abs(a), abs(b))
        return (a * b) // g_c_d

    def add(self, other: Fraction):

        l_c_m = Fraction.least_common_multiple(self.denom, other.denom)

        new_num = (l_c_m // self.denom) * self.num + (l_c_m // other.denom) * other.num
        new_denom = l_c_m

        g_c_d = Fraction.greatest_common_divisor(new_num, new_denom)
        self.num = new_num // g_c_d
        self.denom = new_denom // g_c_d
import math
import unittest

number = int(input("Szam: "))

def sqrt_sajat(number:int):
    if number >= 0:
        sqrt_number = math.sqrt(number)
        return sqrt_number
    else:
        return "Negativ szambol nem vonunk negyzetgyokot!"


class TestSqrtFunc(unittest.TestCase):

    def test_number_not_neg(self):
        self.assertGreaterEqual(sqrt_sajat(-1), 0)

    def test_number_zero(self):
        self.assertEqual(sqrt_sajat(0), 0)


unittest.main()
    

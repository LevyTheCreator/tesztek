import unittest

def sum_even(start, end):
    szum = 0
    for i in range(start, end+1, 2):
        szum += i

    return szum

class TestSumEvenFunc(unittest.TestCase):

    def test_sum_even_pos(self):
        self.assertGreater(sum_even(0, 50), 0)

    def test_sum_even_iseven(self):
        self.assertEqual(sum_even(42, 100)%2, 0)

unittest.main()
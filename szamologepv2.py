import unittest   

def calculator(n1:int, n2:int, op:str):
    if op == "+":
        return f"Az eredmenyed: {round(n1 + n2, 2)}"
    elif op == "-":
        return f"Az eredmenyed: {round(n1 - n2, 2)}"
    elif op == "*":
        return f"Az eredmenyed: {round(n1 * n2, 2)}"
    elif op == "/":
        if n2 == 0:
            return "Ejnye, nullaval nem osztunk!"
        else:
            return f"Az eredmenyed: {round(n1 / n2, 2)}"
    else:
        return "Hibas muveleti jel!"


class TestCalcFunc(unittest.TestCase):

    def test_pos_plus_pos(self):
        self.assertGreater(calculator(4, 13, "+"), 0)

    def test_pos_times_neg(self):
        self.assertLess(calculator(-7, 4, "*"), 0)

    def test_div_by_zero(self):
        self.assertEqual(calculator(123, 0, "/"), "Ejnye, nullaval nem osztunk!")

    def test_wrong_operator(self):
        self.assertEqual(calculator())
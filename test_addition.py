import unittest


# Fonction à tester
def addition(a, b):
    return a + b


# Tests unitaires
class TestAddition(unittest.TestCase):

    def test_addition_positive(self):
        self.assertEqual(addition(2, 3), 5)

    def test_addition_zero(self):
        self.assertEqual(addition(5, 0), 5)

    def test_addition_negative(self):
        self.assertEqual(addition(-2, 3), 1)


if __name__ == "__main__":
    unittest.main()
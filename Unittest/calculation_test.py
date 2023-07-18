import unittest
import calculation as calc


class UnitTestCalculation(unittest.TestCase):
    def test_framework(self):

        self.assertEqual(1, 1)

    def test_framework2(self):
        self.assertEqual(2, 1+1)

    def test_least_square_calculation_with_no_arguments(self):
        out = calc.Calculation
        test_data1 = 0
        test_data2 = 0
        out_result = out.least_square_calculation(test_data1,  test_data2)
        self.assertEqual(0, out_result)


if __name__ == "__main__":
    unittest.main()
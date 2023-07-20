import unittest
import pandas as pd
import calculation as calc


class UnitTestCalculation(unittest.TestCase):
    def test_framework(self):
        self.assertEqual(1, 1)

    def test_framework2(self):
        self.assertEqual(2, 1+1)

    def test_least_square_calculation_with_no_arguments(self):
        out = calc.Calculation
        train_data = pd.DataFrame()
        ideal_data = pd.DataFrame()
        out_result = out.least_square_calculation(train_data, ideal_data)
        self.assertEqual(0, out_result)


if __name__ == "__main__":
    unittest.main()

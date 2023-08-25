import unittest
import pandas as pd
from calculation import Calculation


class UnitTestCalculation(unittest.TestCase):
    def test_least_square_calculation_with_empty_arguments(self):
        # out = object under test
        out = Calculation()
        train_data = pd.DataFrame()
        ideal_data = pd.DataFrame()

        out_result = out.least_square_calculation(train_data, ideal_data)
        expected_result = []

        self.assertEqual(expected_result, out_result)

    def test_least_square_calculation_with_arguments(self):
        # out = object under test
        out = Calculation()
        train_data = pd.read_csv("../Data/train.csv")
        ideal_data = pd.read_csv("../Data/ideal.csv")

        out_result = out.least_square_calculation(train_data, ideal_data)
        expected_result = [{'ideal_data_y': 36,
                            'minimal_deviation_index': 35,
                            'minimal_deviation_value': 33.71178854422821,
                            'train_data_y': 1},
                           {'ideal_data_y': 11,
                            'minimal_deviation_index': 10,
                            'minimal_deviation_value': 32.62893138832121,
                            'train_data_y': 2},
                           {'ideal_data_y': 2,
                            'minimal_deviation_index': 1,
                            'minimal_deviation_value': 33.11847188090256,
                            'train_data_y': 3},
                           {'ideal_data_y': 33,
                            'minimal_deviation_index': 32,
                            'minimal_deviation_value': 31.75243110139478,
                            'train_data_y': 4}]

        self.assertEqual(expected_result, out_result)

    def test_least_square_calculation_with_one_argument(self):
        # out = object under test
        out = Calculation()
        train_data = pd.read_csv("../Data/train.csv")
        ideal_data = pd.DataFrame()

        out_result = out.least_square_calculation(train_data, ideal_data)
        expected_result = []

        self.assertEqual(expected_result, out_result)

    def test_max_deviation_best_fits_to_test_data_calculation_with_no_arguments(self):
        # out = object under test
        out = Calculation()
        best_fits_data = pd.DataFrame()
        test_data = pd.DataFrame()

        out_result = out.max_deviation_best_fits_to_test_data_calculation(best_fits_data, test_data)
        expected_result = []

        self.assertEqual(expected_result, out_result)

    def test_max_deviation_best_fits_to_test_data_calculation_with_one_argument(self):
        # out = object under test
        out = Calculation()
        best_fits_data = pd.DataFrame()
        test_data = pd.read_csv("../Data/test.csv")
        test_data.name = "test.csv"
        sorted_test_data = test_data.sort_values(by="x", ignore_index=True)
        sorted_test_data.name = "sorted_test.csv"

        out_result = out.max_deviation_best_fits_to_test_data_calculation(best_fits_data, sorted_test_data)
        expected_result = []

        self.assertEqual(expected_result, out_result)

    def test_max_deviation_train_data_to_best_fits_calculation_with_one_argument(self):
        # out = object under test
        out = Calculation()
        train_data = pd.read_csv("../Data/train.csv")
        best_fits_data = pd.DataFrame()

        out_result = out.max_deviation_train_data_to_best_fits_calculation(train_data, best_fits_data)
        expected_result = []

        self.assertEqual(expected_result, out_result)


if __name__ == "__main__":
    unittest.main()

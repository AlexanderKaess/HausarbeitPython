import logging
import numpy as np
import pandas as pd

logger = logging.getLogger("HAUSARBEIT")


class Calculation:
    def __init__(self):
        logger.info("Calculation created object")

    def least_square_calculation(self, train_data, ideal_data):
        result_dict_list = []

        # get number of rows in train_data
        rows_train_data = len(train_data.index)
        logger.info("rows = " + str(rows_train_data))

        # get number of columns in train_data
        columns_train_data = len(train_data.columns) - 1
        logger.info("columns_train_data = " + str(columns_train_data))

        # get number of columns in ideal_data
        columns_ideal_data = len(ideal_data.columns) - 1
        # columns_ideal_data = 10
        logger.info("columns_ideal_data = " + str(columns_ideal_data))

        # 4 columns in train_data
        for column_train in range(1, columns_train_data + 1, 1):
            sum_array = 0.0
            result_dict = {"train_data_y": column_train,
                           "ideal_data_y": 0,
                           "minimal_deviation_value": 0.0,
                           "minimal_deviation_index": 0}

            logger.info("### train-function: y" + str(column_train) + " ###")
            # 50 columns in ideal_data
            new_sum_array = 100000.0
            for column_ideal in range(1, columns_ideal_data + 1, 1):
                current_column_sum = 0.0
                # create array from y column values
                train_y_array = np.array(train_data["y" + str(column_train)])
                ideal_y_array = np.array(ideal_data["y" + str(column_ideal)])

                # 400 rows to subtract
                for row in range(0, rows_train_data, 1):
                    # calculate least square deviation
                    result = np.square(np.subtract(train_y_array[row], ideal_y_array[row]))
                    current_column_sum += result

                sum_array = np.append(sum_array, current_column_sum)
                index_to_delete = 0
                new_sum_array = np.delete(sum_array, index_to_delete)

            logger.debug("sum_array: " + str(new_sum_array))
            minimal_deviation = np.min(new_sum_array)
            result_dict["minimal_deviation_value"] = minimal_deviation
            logger.debug("minimum deviation: " + str(minimal_deviation))

            minimal_deviation_index = np.argmin(new_sum_array)
            result_dict["minimal_deviation_index"] = minimal_deviation_index
            result_dict["ideal_data_y"] = minimal_deviation_index + 1
            logger.debug("minimum deviation index: " + str(minimal_deviation_index))
            logger.info("##### result_dict: " + str(result_dict))

            result_dict_list.append(result_dict)
        return result_dict_list

    # calculation of M
    def max_deviation_best_fits_to_test_data_calculation(self, best_fits_data, test_data):
        result_dict_list = []
        rows_test_data = len(test_data.index)

        logger.info("Get column values from best_fits_data and corresponding test_data")
        for column_best in best_fits_data:
            if column_best == "x":
                continue

            # --------- remove after testing -------------
            if  column_best == "y11":
                break

            result_array = 0.0
            result_dict = {"best_fits_data": column_best,
                           "M": column_best,
                           "maximal_deviation_value": 0.0,
                           "maximal_deviation_index": 0}

            for row in test_data.index:
                logger.info("############")
                logger.info("Column best: " + str(column_best))
                logger.info("test_data_row_index: " + str(row))

                # .loc[row, column] = get value of location
                x_value_test_data = test_data.loc[row, "x"]
                y_value_test_data = test_data.loc[row, "y"]
                logger.info("x_value: " + str(x_value_test_data))
                logger.info("y_value: " + str(y_value_test_data))

                selection = best_fits_data["x"]
                logger.info("y_value to find from x = " + str(selection[row]))

                # get index of x_value in the best_fits_Data
                position_index = pd.Index(selection).get_loc(x_value_test_data)

                # .loc[row, column] = get value of location
                y_value_best_fits = best_fits_data.loc[position_index, column_best]
                if y_value_best_fits is None:
                    logger.info("no y value found in best_fits for x: " + str(x_value_test_data))
                    continue
                logger.info("column : " + str(column_best) +
                            " --> position_in_column: " + str(position_index) +
                            " --> y_value: " + str(y_value_best_fits))

                logger.info("x value is " + str(x_value_test_data) + ", calculation of deviation ...")
                result = np.subtract(y_value_best_fits, y_value_test_data)
                logger.info("Result: " + str(y_value_best_fits) + " - " +
                            str("(") + str(y_value_test_data) + str(")") + " = " + str(result))
                result_array = np.append(result_array, result)

            index_to_delete = 0
            new_result_array = np.delete(result_array, index_to_delete)
            maximal_deviation = np.max(new_result_array)
            result_dict["maximal_deviation_value"] = maximal_deviation
            maximal_deviation_index = np.argmax(new_result_array)
            result_dict["maximal_deviation_index"] = maximal_deviation_index

            result_dict_list.append(result_dict)
        logger.info("result_dict: " + str(result_dict_list))
        return result_dict_list

    # calculation of N e.g. N36 = max(train_y1 - best_fits_y36)
    def max_deviation_train_data_to_best_fits_calculation(self, train_data, best_fits_data):
        result_dict_list = []
        columns_train_data = len(train_data.columns)
        rows_train_data = len(train_data.index)

        logger.info("Get column values from train_data and corresponding best_fits_data")
        for column_train in range(1, columns_train_data, 1):
            result_array = 0.0
            result_dict = {"train_data": 0,
                           "best_fits_data": 0,
                           "N": 0,
                           "maximal_deviation_value": 0.0,
                           "maximal_deviation_index": 0}

            # create array from y column values
            current_train_column = train_data.columns[column_train]
            train_y_array = np.array(train_data[current_train_column])
            result_dict["train_data"] = current_train_column
            current_best_fits_column = best_fits_data.columns[column_train]
            best_fits_y_array = np.array(best_fits_data[current_best_fits_column])
            result_dict["best_fits_data"] = current_best_fits_column
            result_dict["N"] = current_best_fits_column

            # 400 rows to subtract
            for row in range(0, rows_train_data, 1):
                result = np.subtract(train_y_array[row], best_fits_y_array[row])
                result_array = np.append(result_array, result)

            index_to_delete = 0
            new_result_array = np.delete(result_array, index_to_delete)
            maximal_deviation = np.max(new_result_array)
            result_dict["maximal_deviation_value"] = maximal_deviation
            maximal_deviation_index = np.argmax(new_result_array)
            result_dict["maximal_deviation_index"] = maximal_deviation_index

            result_dict_list.append(result_dict)
        logger.info("result_dict: " + str(result_dict_list))
        return result_dict_list

    # calculation of M < (sqrt(2)) * N
    def validation_calculation(self, train_data, best_fits_data, test_data):
        logger.info("Validation calculation")
        result = 0

        result_m = self.max_deviation_best_fits_to_test_data_calculation(best_fits_data, test_data)
        result_n = self.max_deviation_train_data_to_best_fits_calculation(train_data, best_fits_data)

        return result

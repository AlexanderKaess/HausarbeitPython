import logging
import pandas as pd
import numpy as np

import centrallogger
import visualization
from database import Database

logger = logging.getLogger("HAUSARBEIT")


def main():
    print("### Starting script for data comparison and validation ###")

    # create central logging object
    centrallogger.Centrallogger("HAUSARBEIT")

    # load .csv files to dataframes
    logger.info("Create training table")
    train_data = pd.read_csv("./Data/train.csv")
    train_data.name = "train.csv"

    logger.info("Create ideal table")
    ideal_data = pd.read_csv("./Data/ideal.csv")
    ideal_data.name = "ideal.csv"

    logger.info("Create test table")
    test_data = pd.read_csv("./Data/test.csv")
    test_data.name = "test.csv"

    # create database and insert dataframes
    database = Database()
    database.create_connection('hausarbeit')
    database.create_table_from_dataframe(train_data, train_data.name)
    database.create_table_from_dataframe(ideal_data, ideal_data.name)
    database.create_table_from_dataframe(test_data, test_data.name)

    # create plots
    # train_visualization = visualization.Visualization(train_data, train_data.name)
    # train_visualization.create_plot_from_dataframe()
    # ideal_visualization = visualization.Visualization(ideal_data, ideal_data.name)
    # ideal_visualization.create_plot_from_dataframe()

    test_result = least_square_calculation(train_data, ideal_data)
    print("testresult: " + str(test_result))

    print("### Finished script ###")


def least_square_calculation(train_data, ideal_data):
    result_dict_list = []

    # get number of rows in train_data
    rows_train_data = len(train_data.index)
    print("rows = " + str(rows_train_data))

    # get number of columns in train_data
    columns_train_data = len(train_data.columns) - 1
    print("columns_train_data = " + str(columns_train_data))

    # get number of columns in ideal_data
    columns_ideal_data = len(ideal_data.columns) - 1
    # columns_ideal_data = 10
    print("columns_ideal_data = " + str(columns_ideal_data))

    # 4 columns in train_data
    for column_train in range(1, columns_train_data + 1, 1):
        sum_array = 0.0
        result_dict = {"train_data_y": 0, "ideal_data_y": 0, "minimal_deviation_value": 0.0, "minimal_deviation_index": 0 }

        result_dict["train_data_y"] = column_train
        print("### train-function: y" + str(column_train) + " ###")
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
            index = 0
            new_sum_array = np.delete(sum_array, index)

        print("sum_array: " + str(new_sum_array))
        minimal_deviation = np.min(new_sum_array)
        result_dict["minimal_deviation_value"] = minimal_deviation
        print("minimum deviation: " + str(minimal_deviation))

        minimal_deviation_index = np.argmin(new_sum_array)
        result_dict["minimal_deviation_index"] = minimal_deviation_index
        result_dict["ideal_data_y"] = minimal_deviation_index + 1
        print("minimum deviation index: " + str(minimal_deviation_index))
        print("##### result_dict: " + str(result_dict))
        print("")

        result_dict_list.append(result_dict)
    return result_dict_list


if __name__ == "__main__":
    main()

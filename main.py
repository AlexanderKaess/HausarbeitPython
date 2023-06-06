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
    print(test_result)

    print("### Finished script ###")


def least_square_calculation(train_data, ideal_data):
    result = 0.0

    # get number of rows in train_data
    rows_train_data = len(train_data.index)
    print("rows = " + str(rows_train_data))

    # get number of columns in train_data
    columns_train_data = len(train_data.columns)-1
    print("columns_train_data = " + str(columns_train_data))

    # get number of columns in ideal_data
    # columns_ideal_data = len(ideal_data.columns)-1
    columns_ideal_data = 10
    print("columns_ideal_data = " + str(columns_ideal_data))

    # 4 columns in train_data
    for column_train in range(1, columns_train_data, 1):
        print("train: " + str(column_train))
        # 50 columns in ideal_data
        for column_ideal in range(1, columns_ideal_data, 1):
            print("ideal: " + str(column_ideal))
            # create array from y column values
            train_y_array = np.array(train_data["y" + str(column_train)])
            ideal_y_array = np.array(ideal_data["y" + str(column_ideal)])

            # 400 rows to subtract
            for row in range(1, rows_train_data, 1):
                # calculate least square deviation
                print(str(row))
                result = np.square(np.subtract(train_y_array[row], ideal_y_array[row]))
                print(result)

    # numpy.org/doc/
    # numpy.sqrt(x) = Quadratwurzel der Elemente von array x
    # numpy.square(x) = Quadrat der Elemente von array x
    # numpy.minimum(x1, x2) = Minimum der Elemente von array x1 und array x2
    # numpy.std(x) = Berechnet Standardabweichung von array x
    # a = np.array([1,2,3,4,5],[6,7,8,9,10])
    # get a specific element a[1,3] --> 9
    # get a specific row a[0,:] --> 1,2,3,4,5
    # get a specific column a[:,2] --> 3,8


    return result


if __name__ == "__main__":
    main()

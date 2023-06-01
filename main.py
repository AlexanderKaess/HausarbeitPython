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
    train_visualization = visualization.Visualization(train_data, train_data.name)
    train_visualization.create_plot_from_dataframe()
    ideal_visualization = visualization.Visualization(ideal_data, ideal_data.name)
    ideal_visualization.create_plot_from_dataframe()

    test = least_square_calculation(train_data, ideal_data)
    print(train_data)
    print(test)

    print("### Finished script ###")


def least_square_calculation(train_data, ideal_data):
    result = 0.0
    # get y values of each column from train and ideal

    # create array from y column values
    train_y_array = np.array(train_data.y1)
    print(train_y_array)
    ideal_y_array = np.array(ideal_data.y1)

    # calculate least square deviation
    result = np.square(np.subtract(train_y_array, ideal_y_array))

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

import logging
import pandas as pd

import centrallogger
import visualization
from database import Database
from calculation import Calculation

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
    train_visualization = visualization.Visualization(train_data)
    train_visualization.create_plot_from_dataframe()

    # calcualtion of best fits from train data to ideal data
    best_fits = Calculation()
    best_fits_result = best_fits.least_square_calculation(train_data, ideal_data)
    print("")
    print("calcresult: " + str(best_fits_result))

    logger.info("Create calculation result table")
    best_fits_data = pd.DataFrame(best_fits_result)
    best_fits_data.name = "best_fits_result"
    database.create_table_from_dataframe(best_fits_data, best_fits_data.name)

    # get the lines from ideal_data with line numbers from best_fits

    best_fits_visualization = visualization.Visualization(train_data, train_data)
    best_fits_visualization.create_plot_from_selection()

    print("### Finished script ###")


if __name__ == "__main__":
    main()

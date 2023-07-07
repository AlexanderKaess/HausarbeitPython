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

    logger.info("Create sorted test table")
    test_data = pd.read_csv("./Data/test.csv")
    test_data.name = "test.csv"
    sorted_test_data = test_data.sort_values(by="x", ignore_index=True)
    sorted_test_data.name = "sorted_test.csv"

    # create database and insert dataframes
    database = Database()
    database.create_connection('hausarbeit')
    database.create_table_from_dataframe(train_data, train_data.name)
    database.create_table_from_dataframe(ideal_data, ideal_data.name)
    database.create_table_from_dataframe(test_data, test_data.name)
    database.create_table_from_dataframe(sorted_test_data, sorted_test_data.name)

    # create visualization for train_data
    train_visualization = visualization.Visualization(train_data)
    train_visualization.create_plot_from_dataframe()

    # calcualtion of best fits from train data to ideal data
    calculation = Calculation()
    calculation_result = calculation.least_square_calculation(train_data, ideal_data)
    print("")
    print("calcresult: " + str(calculation_result))

    logger.info("Create calculation result table")
    calculation_data = pd.DataFrame(calculation_result)
    calculation_data.name = "best_fits_result"
    database.create_table_from_dataframe(calculation_data, calculation_data.name)

    # get the lines for best_fits
    best_fits_data = database.create_table_bestfits(ideal_data, calculation_data)
    best_fits_data.name = "bestfits"
    database.create_table_from_dataframe(best_fits_data, best_fits_data.name)

    # visualize the train and best_fits lines in one plot
    best_fits_visualization = visualization.Visualization(train_data, best_fits_data)
    best_fits_visualization.create_plot_from_selection()

    validation_result = calculation.validation_calculation(train_data, best_fits_data, sorted_test_data)
    print("validation_result: " + str(validation_result))

    print("### Finished script ###")


if __name__ == "__main__":
    main()

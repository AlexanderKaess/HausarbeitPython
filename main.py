import logging

import pandas as pd
import numpy as np
import seaborn as sb

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

    logger.info("Create ideal table")
    ideal_data = pd.read_csv("./Data/ideal.csv")

    logger.info("Create test table")
    test_data = pd.read_csv("./Data/test.csv")

    # create database and insert dataframes
    database = Database()
    database.create_connection('hausarbeit')
    database.create_table_from_dataframe(train_data, "train_data")
    database.create_table_from_dataframe(ideal_data, "ideal_data")

    train_visualization = visualization.Visualization()
    train_visualization.create_plot_from_dataframe(train_data)
    #ideal_visualitzation = visualization.Visualization()
    #ideal_visualitzation.create_alotplot_from_dataframe(ideal_data)

    print("### Finished script ###")


if __name__ == "__main__":
    main()

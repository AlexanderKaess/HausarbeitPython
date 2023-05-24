import os
import logging
import pandas as pd
import numpy as np
import seaborn as sb
import datetime as dt

from database import Database


def main():
    # create logger, has to be moved to own file
    today = dt.datetime.today()
    log_file_name = f"{today.year:02d}-{today.month:02d}-{today.day:02d}.log"
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("HAUSARBEIT")
    file_handler = logging.FileHandler("./Logging/" + log_file_name)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.info("### Starting script for record comparison and validation ###")

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

    logger.info("### Finished script ###")


if __name__ == "__main__":
    main()

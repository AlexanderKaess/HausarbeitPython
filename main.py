import os
import logging
import pandas as pd
import numpy as np
import seaborn as sb
import datetime as dt

from database import Database

def get_data_file_content(file_name):
    """
    This function open its input-file in read-mode and return its content
    :param file_name: the name of the file with path as string
    :return: data_file_content: content of the input-file as string
    """
    data_file_content = ""
    if os.path.isfile(file_name):
        with open(file_name, "r") as data_file:
            data_file_content = data_file.read()

    return data_file_content


def main():
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

    print("Panadas-Dataframe:")

    print("training table:")
    train_data = pd.read_csv("./Data/train.csv")
    print(train_data)

    print("ideal table:")
    ideal_data = pd.read_csv("./Data/ideal.csv")
    print(ideal_data)

    print("test table:")
    test_data = pd.read_csv("./Data/test.csv")
    print(test_data)

    database = Database()
    database.create_connection('hausarbeit')

    logger.info("### Finished script ###")


if __name__ == "__main__":
    main()

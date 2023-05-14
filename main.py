import os
import logging
import pandas as pd
import numpy as np
import seaborn as sb

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
    logging.basicConfig(level=logging.INFO,
                        filename="./Logging/info.log",
                        filemode="w",
                        format="%(asctime)s - %(levelname)s - %(message)s")
    logging.info("Starting script for record comparison and validation")

    #print(get_data_file_content("./Data/test.csv"))

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

    logging.info("Finished script")


if __name__ == "__main__":
    main()

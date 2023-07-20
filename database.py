import logging
import sqlalchemy as db
import pandas as pd
import numpy as np
import os

logger = logging.getLogger("HAUSARBEIT")


class Database:
    """
    A class to represent a Database and methods to interact with the database.

    Methods
    -------
    create_connection:
        Creates a connection to a database
    create_table_from_dataframe:
        Creates a database table from a dataframe
    create_table_bestfits:
        Creates the table best_fits from ideal_data and best_fits_result
    """
    def __init__(self):
        logger.info("Database created object")
        self.database_name = None
        self.connection_string = ""
        self.meta_data = None

    def create_connection(self, database_name):
        """
        Creates a connection to a database
                Parameters:
                        database_name (string): a string with the name of the database
        """
        self.database_name = database_name
        my_password = os.environ['MY_SQL_PASSWORD']
        my_username = "root"
        self.connection_string = "mysql+pymysql://" + my_username + ":" + my_password + "@localhost/" + database_name
        logger.info("Connection string created")

        # create engine-object
        self.engine = db.create_engine(self.connection_string)
        logger.info("Engine object created")

        # create databank connection object
        connection = self.engine.connect()
        logger.info("Databank connection object created")

        # create meta data object
        self.meta_data = db.MetaData()
        logger.info("Meta data object created")

    def create_table_from_dataframe(self, dataframe_object, table_name):
        """
        Creates a database table from a dataframe
                Parameters:
                        dataframe_object (dataframe): a pandas dataframe
                        table_name (string): name of the table
        """
        if not isinstance(dataframe_object, pd.DataFrame):
            logger.error("Object is not a dataframe")
            return

        logger.info("Create table from dataframe: " + table_name)
        dataframe_object.to_sql(table_name, con=self.engine, schema="hausarbeit", if_exists="replace", index=False)

    def create_table_bestfits(self, ideal_data, best_fits_result):
        """
        Creates the table best_fits from ideal_data and best_fits_result
                Parameters:
                        ideal_data (dataframe): a pandas dataframe
                        best_fits_result (dataframe): a pandas dataframe
                Returns:
                        result_dict_list (list): a list of dictionaries with results of calculation
        """
        logger.info("Create table for bestfits")
        result_data = pd.DataFrame()

        # 400 values from -20.0 to 19.9, round to 0.1
        result_data["x"] = np.round(np.linspace(-20, 20, 400, endpoint=False), decimals=1)

        # get the x value from result_data table, for testing only
        for r in result_data.index:
            value = result_data.loc[r, "x"]
            logger.debug("x_value: " + str(value))

        # get the values from column ideal_data_y in best_fits_result
        best_ideal_functions = best_fits_result["ideal_data_y"].values
        logger.debug("best_ideal_functions: " + str(best_ideal_functions))

        # get the column values from best_ideal_functions and put them in result_data table
        for bf in best_ideal_functions:
            result_column = "y" + str(bf)
            data = ideal_data[result_column]
            result_data[result_column] = data.values
        return result_data

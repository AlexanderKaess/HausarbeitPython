import logging
import sqlalchemy as db
import pandas as pd
import os

logger = logging.getLogger("HAUSARBEIT")


class Database:
    def __init__(self):
        logger.info("Database created object")
        self.database_name = None
        self.connection_string = ""
        self.meta_data = None

    def create_connection(self, database_name):
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

    def create_table(self, table_name):
        logger.info("Create table: " + table_name)
        table = db.Table(
            table_name,
            self.meta_data,
            db.Column("x_test_function", db.Integer, primary_key=True, autoincrement=False, nullable=False),
            db.Column("y_test_function", db.Integer, nullable=False),
            db.Column("delta_y", db.Integer, nullable=False),
            db.Column(table_name, db.Integer, nullable=False)
        )
        self.meta_data.create_all(self.engine)

    def create_table_from_dataframe(self, dataframe_object, table_name):
        if not isinstance(dataframe_object, pd.DataFrame):
            logger.error("Object is not a dataframe")
            return

        logger.info("Create table from dataframe: " + table_name)
        dataframe_object.to_sql(table_name,
                                con=self.engine,
                                schema="hausarbeit",
                                if_exists="replace",
                                index=False)

    def create_table_bestfits(self, ideal_data, calculation_data):
        #data = pd.Series()
        result_data = pd.DataFrame()
        best_ideal_functions = calculation_data["ideal_data_y"].values
        for bf in best_ideal_functions:
            result_column = "y" + str(bf)
            print("ideal-data: " + result_column)
            data = ideal_data[result_column]
            print("+++++")
            print(data)
            ## add a Series to a Pandas Dataframe
            result_data.append({data})
        print(result_data)
        return result_data

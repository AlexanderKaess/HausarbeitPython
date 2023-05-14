import sqlalchemy as db
import pymysql
import os


class Database:
    def __init__(self):
        print("Database created object")
        self.database_name = None
        self.connection_string = ""
        self.meta_data = None

    def create_connection(self, database_name):
        self.database_name = database_name
        my_password = os.environ['MY_SQL_PASSWORD']
        my_username = "root"
        self.connection_string = "mysql+pymysql://" + my_username + ":" + my_password + "@localhost/" + database_name
        print("Connection string created")

        # create engine-object
        engine = db.create_engine(self.connection_string)
        print("Engine object created")

        # create databank connection object
        connection = engine.connect()
        print("Databank connection object created")

        # create meta data object
        self.meta_data = db.MetaData()
        print("Meta data object created")

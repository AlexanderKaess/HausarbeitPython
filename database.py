import sqlalchemy as db
import os


class Database:
    def __init__(self):
        self.database_name = None
        self.connection_string = ""
        self.meta_data = None

    def create_connection(self, database_name):
        self.database_name = database_name
        my_password = os.getenv('MYSQLPASSWORD')
        my_username = "root"
        self.connection_string = "mysql+pymysql://" + my_username + ":" + my_password + "@localhost/hausarbeit"

        #create engine-object
        engine = db.create_engine(self.connection_string)

        #create databank connection object
        connection = engine.connect()

        #create meta data object
        self.meta_data = db.MetaData()



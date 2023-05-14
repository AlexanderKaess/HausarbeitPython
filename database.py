import sqlalchemy as db
import os
import logging

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
            db.Column("id",db.Integer,primary_key=True,autoincrement=True,nullable=False),
            db.Column("name",db.String(50),nullable=False)
        )
        self.meta_data.create_all(self.engine)

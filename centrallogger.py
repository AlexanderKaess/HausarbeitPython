import logging
import datetime as dt


class Centrallogger(logging.Logger):
    """
    A class to represent a Centrallogger object.
    This class is derived from logging.Logger
    """
    def __init__(self, logger_name):
        super().__init__(logger_name)

        # get the date of today
        today = dt.datetime.today()
        log_file_name = f"{today.year:02d}-{today.month:02d}-{today.day:02d}.log"

        # set log level for login events to INFO
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler("./Logging/" + log_file_name, mode="w")
        # format of the logging entry
        formatter = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

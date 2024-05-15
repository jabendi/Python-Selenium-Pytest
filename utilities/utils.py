import inspect
import logging


class Utils:
    @staticmethod
    def custom_logger():
        # Set class/method name from where it's called
        logger_name = inspect.stack()[1][3]
        # create logger
        logger = logging.getLogger("my_logger")
        logger.setLevel(logging.DEBUG)
        # create console handler or file handler and set the log level.
        file_handler = logging.FileHandler(filename=r'logs\collectedlogs.log')
        # create formatter - how you want your logs to be formatted.
        my_formatter = logging.Formatter("%(asctime)s) - %(levelname)s - %(name)s : %(message)s",
                                         datefmt='%d/%m/%Y %I:%M:%S %p')
        #  add formatter to file handler.
        file_handler.setFormatter(my_formatter)
        # add console handler to logger.
        logger.addHandler(file_handler)
        return logger

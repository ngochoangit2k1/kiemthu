import logging.handlers
import logging


class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename="Logs/loginNotificationLog.log", format='%(asctime)s - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S', filemode='w')
        rotate_file = logging.handlers.RotatingFileHandler(
            "Logs/loginNotificationLog.log", maxBytes=1024 * 1024 * 20, backupCount=3
        )
        logger = logging.getLogger()
        logger.addHandler(rotate_file)
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def logout():
        logging.basicConfig(filename="Logs/logoutNotificationLog.log", format='%(asctime)s - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S', filemode='w')
        rotate_file = logging.handlers.RotatingFileHandler(
            "Logs/registerNotificationLog.log", maxBytes=1024 * 1024 * 20, backupCount=3
        )
        logger = logging.getLogger()
        logger.addHandler(rotate_file)
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def register():
        logging.basicConfig(filename="Logs/registerNotificationLog.log", format='%(asctime)s - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S', filemode='w')
        rotate_file = logging.handlers.RotatingFileHandler(
            "Logs/registerNotificationLog.log", maxBytes=1024 * 1024 * 20, backupCount=3
        )
        logger = logging.getLogger()
        logger.addHandler(rotate_file)
        logger.setLevel(logging.INFO)
        return logger


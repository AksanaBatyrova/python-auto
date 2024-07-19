"""Logger"""

import logging


def setup_logger(name, log_file, level=logging.INFO):
    """Function to set up a logger"""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler(log_file)

    c_format = logging.Formatter('%(name)s :: %(levelname)s :: %(message)s')
    f_format = logging.Formatter(
        '%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s')

    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger

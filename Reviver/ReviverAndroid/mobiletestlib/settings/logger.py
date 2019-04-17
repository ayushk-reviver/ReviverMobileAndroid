"""

.. module :: LoggerSettings
    :synopsis: Settings class for the Virtual device Modules
.. module author:: Ramnik Kaur

"""

import logging


class LoggerSettings(object):

    """
    Logger Levels :
            CRITICAL
            ERROR
            WARNING
            INFO
            DEBUG
            NOTSET

    """

    LOGGER_LEVEL = logging.INFO
    LOG_FILE_PATH = '.'
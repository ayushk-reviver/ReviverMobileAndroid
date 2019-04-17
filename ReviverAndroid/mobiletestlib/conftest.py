import logging

import pytest
from apitestlib.test_settings import Settings
from mobiletestlib.settings.logger import LoggerSettings


def pytest_addoption(parser):
    parser.addoption("--service", default='ss', action="store", dest="service", help="service - ss, ds")
    parser.addoption("--env", default='qa', action="store", dest="env", help="Env: qa, at")
    parser.addoption("--log_path", default='.', action="store", dest="log_path", help="Path to store Log File")
    parser.addoption("--log_level", default='CRITICAL', action="store", dest="log_level", help="INFO/DEBUG/WARNING/ERROR/CRITICAL")
    return parser


def pytest_configure(config):
    mapping = {"CRITICAL": logging.CRITICAL, "ERROR": logging.ERROR, "WARNING": logging.WARNING,
               "INFO": logging.INFO, "DEBUG": logging.DEBUG}
    LoggerSettings.LOGGER_LEVEL = mapping[config.getoption("log_level")]
    LoggerSettings.LOG_FILE_PATH = config.getoption("log_path")
    Settings.SERVICE = config.getoption("service")
    Settings.ENV = config.getoption("env")
    return config

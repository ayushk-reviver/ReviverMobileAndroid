import pytest
from mobiletestlib.core.base import AppiumBaseClass



@pytest.fixture(scope="function")
def invokeApp():
    base= AppiumBaseClass()
    driver=base.launchApp()
    yield driver
    base.tearDown(driver)

@pytest.fixture(scope="function")
def invokeFreshApp():
    base= AppiumBaseClass()
    driver=base.launchFreshApp()
    yield driver
    base.tearDown(driver)

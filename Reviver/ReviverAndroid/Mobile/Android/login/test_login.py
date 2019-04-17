import pytest

from Mobile.Android.login.locators import AndLocators
from Mobile.Android.login.page import LoginPage
from Mobile.Android.login.login_TestData import loginTestdata as testdata
from mobiletestlib.core.base import AppiumBaseClass
from mobiletestlib.core.assertions import AppiumAssertions
from Mobile.Android.login.labels import loginLabels


class TestLogin(object):

    locators_login = AndLocators()
    pageFn = LoginPage()
    data=testdata()
    base=AppiumBaseClass()
    assertions=AppiumAssertions()
    labels=loginLabels()



    @pytest.mark.acceptance
    def test_C8275_Verify_User_Can_Enter_Valid_Password(self,invokeFreshApp):
        print(" ")
        print("1) Tap on Rconnect App Icon on Android")
        driver = invokeFreshApp
        self.pageFn.handleEnvSelection(driver)
        #self.pageFn.logoutLoggedInUser(driver)
        print("2) Enter Email ID")
        print("3) Type password")
        print("4) Tap on Signin")
        self.pageFn.loginIntoApp(self.data.username, self.data.password, driver)
        self.assertions.waitForSomeTimeInSeconds(5)
        self.pageFn.handleDeviceAccessPopup_Allow(driver)
        self.assertions.touchByBounds(driver, self.locators_login.BOUNDS_BURGERICON['x'],
                                      self.locators_login.BOUNDS_BURGERICON['y'])
        self.assertions.waitTillElementVisibleByXpath(driver, self.locators_login.LOC_NAVIGATOR_USERNAME)
        print("Logged in Username : " + self.data.username)
        print("Username after app login : " + self.assertions.getTextFromElementByXpath(driver,
                                                                                                 self.locators_login.LOC_NAVIGATOR_USERNAME))
        assert self.assertions.getTextFromElementByXpath(driver,
                                                         self.locators_login.LOC_NAVIGATOR_USERNAME) == self.data.username
        print("Testing test_C8275_Verify_User_Can_Enter_Valid_Password Completed")

    @pytest.mark.acceptance
    def test_C8276_Verify_User_Can_Enter_Invalid_Password(self,invokeApp):
        print(" ")
        print("1) Tap on Rconnect App Icon on Android")
        driver=invokeApp
        self.pageFn.handleEnvSelection(driver)
        self.pageFn.logoutLoggedInUser(driver)
        print("2) Enter Email ID ,"
              "3) Tap on password ,"
              "4) Type invalid password ,"
              "5) Tap on Signin")
        self.pageFn.loginIntoApp(self.data.username, self.data.invalidPassword, driver)
        self.assertions.waitForSomeTimeInSeconds(2)
        print("Verify error message is displayed and user is not signed in")
        print("Error message displayed under Username Field : "+ self.assertions.getTextFromElementByXpath(driver,self.locators_login.LOC_EMAIL_ERROR))
        print("Error message displayed under Password Field : " + self.assertions.getTextFromElementByXpath(driver,self.locators_login.LOC_PASSWORD_ERROR))
        assert self.labels.LBL_ERROR_MESSAGE==self.assertions.getTextFromElementByXpath(driver,self.locators_login.LOC_PASSWORD_ERROR)






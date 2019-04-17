from appium import webdriver
from mobiletestlib.core.base import AppiumBaseClass
from mobiletestlib.core.assertions import AppiumAssertions
from Mobile.Android.login.locators import AndLocators
from Mobile.Android.login.login_TestData import loginTestdata

class LoginPage(object):
    appsettings = AppiumBaseClass()
    assertions=AppiumAssertions()
    locator=AndLocators()
    data=loginTestdata()

    # def launchApp(self):
    #     driver=self.appsettings.launchApp()
    #     return driver

    def handleEnvSelection(self,tester):
        if(self.appsettings.getEnv()=="QA"):
            self.assertions.waitTillElementVisibleByXpathThanClick(tester,self.locator.LOC_ENVIRONMENT_QA)

    def logoutLoggedInUser(self,driver):
        self.assertions.waitForSomeTimeInSeconds(10)
        self.assertions.touchByBounds(driver, self.locator.BOUNDS_BURGERICON['x'], self.locator.BOUNDS_BURGERICON['y'])
        self.assertions.waitForSomeTimeInSeconds(2)
        self.assertions.waitTillElementVisibleByXpathThanClick(driver, self.locator.LOC_NM_ACCOUNTSETTINGS)
        self.assertions.waitTillElementVisibleByXpathThanClick(driver,self.locator.LOC_AP_SIGNOUTBUTTON)


    def loginIntoApp(self,username,password,driver):
        # self.launchApp()
        # self.handleEnvSelection()
        self.assertions.waitForSomeTimeInSeconds(10)
        self.assertions.touchByBounds(driver,self.locator.BOUNDS_SIGNIN['x'],self.locator.BOUNDS_SIGNIN['y'])
        self.assertions.waitTillElementVisibleByXpath(driver,self.locator.LOC_EMAIL_TEXTBOX)
        self.assertions.sendTextInFieldByXpath(driver,username,self.locator.LOC_EMAIL_TEXTBOX)
        self.assertions.sendTextInFieldByXpath(driver,password, self.locator.LOC_PASSWORD_TEXTBOX)
        self.assertions.tapOnElementByXpath(driver,self.locator.LOC_SIGNIN_BUTTON)
       # self.assertions.waitTillElementVisibleByXpathThanClick(self.driver,self.locator.LOC_SIGNIN)


    def handleDeviceAccessPopup_Allow(self,driver):
        self.assertions.tapOnElementByXpath(driver,self.locator.LOC_HOMEPAGE_DEVICEPOPUP_ALLOW)
        self.assertions.waitForSomeTimeInSeconds(5)
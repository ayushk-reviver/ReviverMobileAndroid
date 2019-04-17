
from appium import webdriver
from mobiletestlib.settings.android import BaseAndroidSettings
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from appium.webdriver.common.touch_action import TouchAction


class AppiumBaseClass(object):
    Andsetting=BaseAndroidSettings()

    def launchApp(self):
        driver=webdriver.Remote(self.Andsetting.hub,self.Andsetting.desired_caps)
        return driver

    def launchFreshApp(self):
        driver=webdriver.Remote(self.Andsetting.hub,self.Andsetting.desired_caps2)
        return driver

    def getEnv(self):
        return self.Andsetting.env

    def tearDown(self,driver):
        driver.quit()
# '''
# Created on Mar 18, 2019
# @author: rkaur
# '''
#
# import os
# import re
# import time
# import timeit
# from datetime import datetime
#
# #import pytz
# #from mobiletestlib.core.base import adb_commands
# #from mobiletestlib.core.base.adb_commands import AndroidDebugBridge
# #from pytz import timezone
# from mobiletestlib.settings.android import BaseAndroidSettings
# from mobiletestlib.core.adb_commands import AndroidDebugBridge
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from appium import webdriver
#
#
#
# class AppiumBaseClass(object):
#     settings = BaseAndroidSettings()
#     #android_settings = AndroidSettings()
#     #ios_settings = iOSSettings()
#     #urls = URLs()
#     #adb_commands = AndroidDebugBridge()
#     hub = ""
#     LOC_SEARCH_PROGRESS_SPINNER = "tv.fan.mobile:id/progressBar"
#     BY_NAME = "name"
#     BY_CSSLOCATOR = "css_locator"
#     BY_ID = "id"
#     userSafariDefaultDownloadDir = "~/Downloads"
#     repeatTimes = 15
#     android_app = ["AndroidApp", "AndroidAppDebug", "AndroidAppDist", "AndroidApp_TiVo"]
#     ios_app = ["iosApp", "ios10", "ios9"]
#
#     """
#     Setup mobile device platform type
#     """
#     print
#     "\nplatform " + settings.platform
#     if "." in settings.devicename:
#         if "Android" in settings.platform:
#             print
#             "connecting android device through ip address " + settings.devicename
#
#     if (settings.platform == "AndroidChrome"):
#         desired_caps = {}
#         desired_caps['appium-version'] = '1.0'
#         desired_caps['platformName'] = 'Android'
#         desired_caps['platformVersion'] = '4.4.2'
#         desired_caps['deviceName'] = settings.devicename
#         desired_caps['browserName'] = 'Chrome'
#         # desired_caps['app']= 'Chrome'
#         desired_caps['sessionOverride'] = True
#     elif (settings.platform == "iOSSafari"):
#         desired_caps = {}
#         desired_caps['appium-version'] = '1.0'
#         desired_caps['platformName'] = 'iOS'
#         desired_caps['platformVersion'] = '8.4'
#         desired_caps['udid'] = '942decb5aacda5c969ac5f79360d9cae25b72b05'
#         desired_caps['deviceName'] = settings.devicename
#         desired_caps['browserName'] = 'safari'
#         desired_caps['sessionOverride'] = True
#         # desired_caps['autoAcceptAlerts'] = True
#     elif (settings.platform == "AndroidApp"):
#         desired_caps = {}
#         #desired_caps['appium-version'] = '1.1'
#         desired_caps['platformName'] = 'Android'
#         #desired_caps['platformVersion'] = '5.1'
#         desired_caps['deviceName'] = settings.devicename
#         #desired_caps['app'] = os.path.abspath(android_settings.androidbuild)
#         desired_caps['appPackage'] = 'com.reviverauto.rplate'
#         desired_caps['appActivity'] = 'com.reviverauto.rplate.SplashActivity'
#         desired_caps['newCommandTimeout'] = '999'
#         desired_caps['noReset'] = True
#         # desired_caps['fullReset'] = True
#         desired_caps['sessionOverride'] = True
#     elif (settings.platform == "AndroidAppDebug"):
#         desired_caps = {}
#         desired_caps['appium-version'] = '1.0'
#         desired_caps['platformName'] = 'Android'
#         desired_caps['platformVersion'] = '5.1'
#         desired_caps['deviceName'] = settings.devicename
#         desired_caps['app'] = os.path.abspath(android_settings.androiddebugbuild)
#         desired_caps['appPackage'] = 'tv.fan.mobile.debug'
#         desired_caps['appActivity'] = 'tv.fan.mobile.activities.SplashScreen'
#         desired_caps['newCommandTimeout'] = '999'
#         desired_caps['noReset'] = False
#         # desired_caps['fullReset'] = True
#         desired_caps['sessionOverride'] = True
#     elif (settings.platform == "AndroidAppDist"):
#         desired_caps = {}
#         desired_caps['appium-version'] = '1.0'
#         desired_caps['platformName'] = 'Android'
#         desired_caps['platformVersion'] = '5.1'
#         desired_caps['deviceName'] = settings.devicename
#         desired_caps['app'] = os.path.abspath(android_settings.androiddistbuild)
#         desired_caps['appPackage'] = 'tv.fan.mobile'
#         desired_caps['appActivity'] = 'tv.fan.mobile.activities.SplashScreen'
#         desired_caps['newCommandTimeout'] = '999'
#         desired_caps['noReset'] = False
#         # desired_caps['fullReset'] = True
#         desired_caps['sessionOverride'] = True
#
#
#     elif (settings.platform == "iosApp"):
#         desired_caps = {}
#         desired_caps['appium-version'] = '1.0'
#         desired_caps['platformName'] = 'iOS'
#         desired_caps['bundleId'] = 'com.fanhattan.iphoneapp'
#         desired_caps['app'] = os.path.abspath(ios_settings.iosbuild)
#         desired_caps['deviceName'] = settings.devicename
#         desired_caps['sessionOverride'] = True
#         # desired_caps['autoAcceptAlerts'] = True
#         if settings.devicename == "iPhone6SPlus":
#             desired_caps['platformVersion'] = '9.1'
#             desired_caps['udid'] = '59ff51b9704d77127a940860491748977dd1b2e2'
#         elif settings.devicename == "iOS_Team_iPhone_6S":
#             desired_caps['platformVersion'] = '9.1'
#             desired_caps['udid'] = 'd3c37c142388b1ed105486e7ea6c71adf36b5ff6'
#         elif settings.devicename == "iPhone":
#             desired_caps['platformVersion'] = '9.1'
#             desired_caps['udid'] = '5505236d34a45bfc712e24fbc31e749c75e4994e'
#         elif settings.devicename == "ipad3":
#             desired_caps['platformVersion'] = '9.1'
#             desired_caps['udid'] = '5c21e0e075172a6b082e14b792b41a70cdaf0fae'
#         elif settings.devicename == "ipad3_1":
#             desired_caps['platformVersion'] = '9.1'
#             desired_caps['udid'] = '8cbffb6ef974f3c054f64cd85a85180ebd132443'
#         elif settings.devicename == "QAiPhone6":
#             desired_caps['platformVersion'] = '9.1'
#             desired_caps['udid'] = '687c37f039e719e68443bee3acb571207fdbe6f1'
#         elif settings.devicename == "QAiPhone":
#             desired_caps['platformVersion'] = '9.1'
#             desired_caps['udid'] = 'c1b0beffdecd84686276096faa9eb3eeb9478835'
#         elif settings.devicename == "iPhone6automation":
#             desired_caps['platformVersion'] = '8.3'
#             desired_caps['udid'] = '1f0f28e4848b56526154fec95b40197d2a64edb5'
#         elif settings.devicename == "iOS_Team_iPhone6_Plus":
#             desired_caps['platformVersion'] = '8.1'
#             desired_caps['udid'] = 'c75009ad6f28b01525d5eaf3971e320e5f74097d'
#         elif settings.devicename == "iOS_Team_iPhone_6":
#             desired_caps['platformVersion'] = '8.1'
#             desired_caps['udid'] = '55524a6305cb5700eac7c6df15a6e0914fb6c232'
#         elif settings.devicename == "iPad-mini3automation":
#             desired_caps['platformVersion'] = '8.4'
#             desired_caps['udid'] = 'b5df36211e58b401c90a4a7c6ee8c8d363a4914c'
#         elif settings.devicename == "Gaurav's IPhone":
#             desired_caps['platformVersion'] = '8.0'
#             desired_caps['udid'] = '880cb440575a656c2d3b16e8feeb1bc5edfbf493'
#         else:
#             desired_caps['platformVersion'] = '8.4'
#             desired_caps['udid'] = '942decb5aacda5c969ac5f79360d9cae25b72b05'
#
#     elif (settings.platform == "ios10" or settings.platform == "ios9"):
#         desired_caps = {}
#         if settings.devicename == "iPhone5s":
#             udid = "942decb5aacda5c969ac5f79360d9cae25b72b05"
#         elif settings.devicename == "QAiPhone1":
#             udid = "7b97ea12fdeddb793ace47af1dc675dfa7786384"
#         elif settings.devicename == "QAiPhone6":
#             udid = "687c37f039e719e68443bee3acb571207fdbe6f1"
#         elif settings.devicename == "iPhone 7":
#             udid = "4d5382437e4488df0f044bc62734f35d1f790d80"
#         elif settings.devicename == "QAiPhone":
#             udid = 'c1b0beffdecd84686276096faa9eb3eeb9478835'
#         elif settings.devicename == "iPhone6SPlus":
#             udid = '59ff51b9704d77127a940860491748977dd1b2e2'
#         desired_caps['platformName'] = 'iOS'
#         desired_caps['platformVersion'] = "10.0"
#         desired_caps['deviceName'] = settings.devicename
#         desired_caps['udid'] = udid
#         desired_caps['automationName'] = 'XCUITest'
#         desired_caps['realDeviceLogger'] = 'idevicesyslog'
#         desired_caps['bundleId'] = 'com.fanhattan.iphoneapp'
#         desired_caps['app'] = os.path.abspath(ios_settings.iosbuild)
#         desired_caps['noReset'] = True
#         desired_caps['fullReset'] = False
#
#     if settings.hub == "":
#         hub = "http://127.0.0.1:4723/wd/hub"
#     else:
#         hub = settings.hub
#     time.sleep(10)
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def setup(self):
#         """
#         setup webdriver
#         :param none
#         """
#         if (self.settings.platform == "AndroidApp"):
#             self.driver.orientation = 'PORTRAIT'
#
#         if (self.settings.platform == "AndroidChrome"):
#             self.driver.get(self.urls.HOME_URL)
#             time.sleep(5)
#             title = self.driver.title
#
#         if (self.settings.platform == "AndroidApp"):
#             driver=webdriver.Remote(self.hub,self.desired_caps)
#             self.driver.get(self.urls.HOME_URL)
#             time.sleep(5)
#             title = self.driver.title
#
#     def teardown(self):
#         """
#         teardown webdriver
#         :param none
#         """
#         self.driver.quit()
#
#     def pause(self, timeInSeconds):
#         """
#         sleep
#         :param timeInSeconds
#         """
#         time.sleep(timeInSeconds)
#
#     def waitSetUp(self):
#         """
#         wait webdriver
#         :param none
#         """
#         wait = self.driver.implicitly_wait(10)
#
#     def mouseHoverJS(self, element):
#         """
#         Calls mouse hover event using Java Script
#         :param element - Web Element
#         """
#         self.driver.execute_async_script(self.driver, "doFireEvent", element, "mouseover")
#
#     def mouseDownJS(self, element):
#         """
#         Calls mouse down event using Java Script
#         :param element - Web Element
#         """
#         self.driver.execute_async_script(self.driver, "doFireEvent", element, "mousedown")
#
#     def mouseUpJS(self, element):
#         """
#         Calls mouse up event using Java Script
#         :param element - Web Element
#         """
#         self.driver.execute_async_script(self.driver, "doFireEvent", element, "mouseup")
#
#     def mouseHover(self, element):
#         """
#         Calls mouse hover using actions
#         :param element - Web Element
#         """
#         actionChains = ActionChains(self.driver)
#         actionChains.move_to_element(element)
#         actionChains.perform()
#
#     def mouseHoverByCss(self, locator):
#         """
#         Calls mouse hover by Css
#         :param element - Web Element
#         """
#         element = self.driver.find_element_by_css_selector(locator)
#         self.mouseHover(element)
#
#     def mouseHoverById(self, id):
#         """
#         Calls mouse hover by Id
#         :param element - Web Element
#         """
#         element = self.driver.find_element_by_id(id)
#         self.mouseHover(element)
#
#     def typeTextByLocator(self, text, locator):
#         """
#         Type Text by locator
#         :param element - text, locator
#         """
#         if (text != "none"):
#             element = self.driver.find_element_by_css_selector(locator)
#             element.click()
#             element.clear()
#             element.send_keys(text)
#
#     def typeText(self, text, byCriteria, value):
#         """
#         Type Text by Criteria
#         :param element - text, locator
#         """
#         print
#         "Type Text " + re.sub('\W+', '', text)
#         if (text != "none"):
#             if byCriteria == "By.NAME":
#                 byCriteria = "By.XPATH"
#                 if Settings.platform in self.android_app:
#                     value = "//*[@text=\'" + value + "\']"
#                 elif Settings.platform in self.ios_app:
#                     value = "//*[@name=\'" + value + "\']"
#             element = self.driver.find_element(by=byCriteria, value=value)
#             element.click()
#             element.clear()
#             element.send_keys(text)
#
#     def typeTextById(self, text, elementId):
#         """
#         Type Text by id
#         :param element - text, id
#         """
#         print
#         "Type Text " + re.sub('\W+', '', text)
#         if (text != "none"):
#             element = self.driver.find_element_by_id(elementId)
#             element.click()
#             element.clear()
#             element.send_keys(text)
#
#     def typeTextByIdText(self, text, elementtext, elementId):
#         """
#         Type Text by id Text
#         :param element - text, text, id
#         """
#         if (text != "none"):
#             webElements = []
#             webElements = self.driver.find_elements_by_id(elementId)
#             for element in webElements:
#                 textActual = element.text
#                 if (textActual == text):
#                     element.click()
#                     element.clear()
#                     element.send_keys(text)
#                     return
#
#     def typeTextByName(self, text, elementName):
#         """
#         Type Text by name
#         :param element - text, name
#         """
#         print
#         "Type Text " + re.sub('\W+', '', text)
#         if (text != "none"):
#             if Settings.platform in self.android_app:
#                 ele_xpath = "//*[@text=\'" + elementName + "\']"
#             elif Settings.platform in self.ios_app:
#                 ele_xpath = "//*[@name=\'" + elementName + "\']"
#             element = self.driver.find_element_by_xpath(ele_xpath)
#             element.click()
#             element.clear()
#             element.send_keys(text)
#
#     def typeTextByXpath(self, text, elementxpath):
#         """
#         Type Text by xpath
#         :param element - text, xpath
#         """
#         print
#         "Type Text " + re.sub('\W+', '', text) + " " + elementxpath
#         if (text != "none"):
#             element = self.driver.find_element_by_xpath(elementxpath)
#             print
#             text
#             element.click()
#             element.clear()
#             element.send_keys(text)
#
#     def typeTextByClassName(self, text, elementClass):
#         """
#         Type Text by xoath
#         :param element - text, xpath
#         """
#         print
#         "Type Text " + re.sub('\W+', '', text)
#         if (text != "none"):
#             element = self.driver.find_element_by_class_name(elementClass)
#             element.click()
#             element.clear()
#             element.send_keys(text)
#
#     def page_source(self):
#         return self.driver.page_source()
#
#     '''
#     Type Text
#     @param element - text, id
#     '''
#
#     def search(self, text, locator):
#         if (text != "none"):
#             element = self.driver.find_element_by_css_selector(locator)
#             element.click()
#             element.clear()
#             element.send_keys(text, Keys.RETURN)
#
#     def clickElementByLocator(self, css_selector):
#         """
#         Click Element by locator
#         :param element - text, locator
#         """
#         print
#         "click on css " + re.sub('\W+', '', css_selector)
#         try:
#             self.driver.find_element_by_css_selector(css_selector).click()
#         except NoSuchElementException:
#             raise NoSuchElementException("Element not found : ByCssSelector - %s" % css_selector)
#
#     def clickElementById(self, id):
#         """
#         Click Element by id
#         :param element - id
#         """
#         print
#         "click on id " + re.sub('\W+', '', id)
#         try:
#             self.driver.find_element_by_id(id).click()
#         except NoSuchElementException:
#             raise NoSuchElementException("Element not found : ById - %s" % id)
#
#     def clickElementByName(self, name):
#         """
#         Click Element by name
#         :param element - name
#         """
#         print
#         "click on Element name " + re.sub('\W+', '', name)
#         if Settings.platform in self.android_app:
#             ele_xpath = "//*[@text=\'" + name + "\']"
#         elif Settings.platform in self.ios_app:
#             ele_xpath = "//*[@name=\'" + name + "\']"
#         try:
#             self.wait_for_element_by_xpath(ele_xpath)
#             self.driver.find_element_by_xpath(ele_xpath).click()
#         except NoSuchElementException:
#             raise NoSuchElementException("Element not found : ByName - %s" % name)
#
#     def clickElementByLinkText(self, text):
#         """
#         Click button by text
#         :param element - link-text
#         """
#         print
#         "click on Link text " + re.sub('\W+', '', text)
#         if (text != "none"):
#             try:
#                 self.driver.find_element_by_link_text(text).click()
#             except NoSuchElementException:
#                 raise NoSuchElementException("Element not found : ByLinkText - %s" % text)
#
#     def clickElementByXPATH(self, path):
#         """
#         Click button by xpath
#         :param element - xpath
#         """
#         print
#         "click on xpath " + re.sub('\W+', '', path)
#
#         if (path != "none"):
#             try:
#                 self.driver.find_element_by_xpath(path).click()
#             except NoSuchElementException:
#                 raise NoSuchElementException("Element not found : ByXPATH - %s" % path)
#
#     def openURL(self, url):
#         """
#         Open URL
#         :param- URL
#         """
#         if (url != "none"):
#             self.driver.get(url)
#             # self.close_alert()
#
#     def close_alert(self):
#         """
#         lose alert if present when open URL
#         :param - none
#         """
#         try:
#             alert = self.driver.switch_to_alert()
#             alert.accept()
#         except:
#             pass
#
#     def clickButtonByText(self, textExpected, locator):
#         """
#         clicks certain element. It can be button, radio button and so on.
#         :param- text, locator
#         """
#         if (textExpected != "none"):
#             webElements = []
#             webElements = self.driver.find_elements_by_css_selector(locator)
#             # print webElements
#             # print len(webElements)
#             for element in webElements:
#                 textActual = element.text
#                 # print textActual
#                 # print textExpected
#                 if (textActual == textExpected):
#                     # if(textActual.equals(textExpected)):
#
#                     element.click()
#                     return
#
#     def clickButtonByTextById(self, textExpected, id):
#         """
#         clicks certain element. It can be button, radio button and so on.
#         :param- text, id
#         """
#         if (textExpected != "none"):
#             webElements = []
#             webElements = self.driver.find_elements_by_id(id)
#             # print webElements
#             # print len(webElements)
#             for element in webElements:
#                 textActual = element.text
#                 # print textActual
#                 # print textExpected
#                 if (textActual == textExpected):
#                     # if(textActual.equals(textExpected)):
#
#                     element.click()
#                     print
#                     "Clicked on \"" + textExpected + "\""
#                     return
#
#     def clickButtonBySubstringById(self, textExpected, id):
#         """
#         Click the element in the given text is a substring of the element text
#         :param- text, id
#         """
#         if (textExpected != "none"):
#             webElements = []
#             webElements = self.driver.find_elements_by_id(id)
#             # print webElements
#             # print len(webElements)
#             for element in webElements:
#                 textActual = element.text
#                 # print textActual
#                 # print textExpected
#                 if (textExpected in textActual):
#                     # if(textActual.equals(textExpected)):
#                     print
#                     "Clicked on " + textExpected
#                     element.click()
#                     return
#
#     def clickTextByXPATH(self, textExpected, XPATH):
#         """
#         Click the element text by xpath
#         :param- text, xpath
#         """
#         if (textExpected != "none"):
#             webElements = []
#             webElements = self.driver.find_elements_by_xpath(XPATH)
#             for element in webElements:
#                 textActual = element.text
#                 if (textActual == textExpected):
#                     element.click()
#                     print
#                     "click on xpath" + re.sub('\W+', '', textExpected)
#                     return
#
#     def findElementWithText(self, textExpected, locator):
#         """
#         Find a certain element. It can be button, radio button and so on.
#         :param- text, locator
#         """
#         if (textExpected != "none"):
#             webElements = []
#             webElements = self.driver.find_elements_by_css_selector(locator)
#             # print webElements
#             # print len(webElements)
#             for element in webElements:
#                 textActual = element.text
#                 # print textActual
#                 # print textExpected
#                 if (textActual == textExpected):
#                     # if(textActual.equals(textExpected)):
#                     print
#                     element
#                     return element
#
#     def findElementByXPATH(self, xpath):
#         """
#         Find a certain element. It can be button, radio button and so on.
#         :param- text, xpath
#         """
#         webElements = self.driver.find_element_by_xpath(xpath)
#         return webElements
#
#     def findElementByIdWithText(self, textExpected, locator):
#         """
#         Find a certain element. It can be button, radio button and so on.
#         :param- text, locator
#         """
#         if (textExpected != "none"):
#             webElements = []
#             webElements = self.driver.find_elements_by_id(locator)
#             # print webElements
#             # print len(webElements)
#             for element in webElements:
#                 textActual = element.text
#                 # print textActual
#                 # print textExpected
#                 if (textActual == textExpected):
#                     # if(textActual.equals(textExpected)):
#                     print
#                     element
#                     return element
#
#     def doubleClickElement(self, webElement):
#         """
#         Double click on element
#         :param - element
#         """
#         webElement.click();
#         actionChains = ActionChains(self.driver)
#         actionChains.doubleClick(webElement).build()
#         actionChains.perform()
#
#     def doubleClickElementById(self, elementId):
#         """
#         Double click element by Id
#         :param - elementId
#         """
#         self.doubleClickElement(self.driver.find_element_by_id(elementId))
#
#     def doubleClickElementByCss(self, locator):
#         """
#         Double click element by Id
#         :param - locator
#         """
#         self.doubleClickElement(self.driver.find_element_by_css_selector(locator))
#
#     def selectCheckBox(self, locator):
#         """
#         Checkbox - check/uncheck
#         :param - locator
#         """
#         print
#         "click on checkbox " + re.sub('\W+', '', locator)
#         checkBox = self.driver.find_element_by_css_selector(locator)
#         checkBox.click()
#
#     def selectCheckBoxById(self, elementId):
#         """
#         Checkbox - check/uncheck by Id
#         :param - locator
#         """
#         checkBox = self.driver.find_element_by_id(elementId)
#         checkBox.click();
#
#     def verifyElementText(self, expectedText, locator):
#         """
#        Verify element text
#        :par
#        """
#         if (expectedText != "none"):
#             element = self.driver.find_element_by_css_selector(locator)
#             actualText = element.text
#             if (expectedText != actualText):
#                 self.assert_false((expectedText != actualText), " element does not contain correct text")
#         self.pause(2)
#
#     def getElementText(self, locator):
#         """
#         get element text
#         :param -  locator
#        """
#         element = self.driver.find_element_by_css_selector(locator)
#         actualText = element.text
#         return actualText
#
#     def getElementTextById(self, id):
#         """
#         get element id
#        :param -  id
#        """
#         try:
#             element = self.driver.find_element_by_id(id)
#             actualText = element.text
#             return actualText
#         except NoSuchElementException:
#             raise NoSuchElementException("Element not found : By ID - %s" % id)
#
#     def getElementTextByXPATH(self, XPATH):
#         """
#         get element xpath
#        :param -  xpath
#        """
#         try:
#             element = self.driver.find_element_by_xpath(XPATH)
#             actualText = element.text
#             return actualText
#         except NoSuchElementException:
#             raise NoSuchElementException("Element not found : By XPATH - %s" % XPATH)
#
#     def getAttrribute(self, locator, attribute):
#         """
#        Verify element attribute by locator
#        :param - locator, attribute
#        """
#         try:
#             element = self.driver.find_element_by_css_selector(locator)
#             elementAttribute = element.get_attribute(attribute)
#             return elementAttribute
#         except:
#             return "Attribute not found"
#
#     def getAttrributeXpath(self, xpath, attribute):
#         """
#        Verify element attribute by xpath
#        :param - xpath, attribute
#        """
#         try:
#             element = self.driver.find_element_by_xpath(xpath)
#             elementAttribute = element.get_attribute(attribute)
#             return elementAttribute
#         except:
#             return "Attribute not found"
#
#     def selectDropDownItem(self, item, locator):
#         """
#        Select Drop Down Item
#        :param - item, locator
#        """
#         if (item != "none"):
#             oSingleSelection = Select(self.driver.find_element_by_css_selector(locator))
#             oSingleSelection.select_by_visible_text(item)
#
#     def getSelectedDropDownItem(self, locator):
#         """
#        get Selected Drop Down Item
#        :param - locator
#        """
#         try:
#             oSingleSelection = Select(self.driver.find_element_by_css_selector(locator))
#             return oSingleSelection.first_selected_option.text
#         except:
#             return "selected drop down item not found"
#
#     def upload(self, locator, fileLocation):
#         """
#        upload a file
#        :param - locator, filelocation
#        """
#         self.driver.find_element_by_css_selector(locator).send_keys(fileLocation)
#         self.pause(1)
#
#     def selectValueInList(self, locator, value):
#         """
#        select a item in a list
#        :param - locator, value
#        """
#         webElement = self.driver.find_element_by_css_selector(locator)
#         # print webElement
#         webElementsList = webElement.find_elements_by_tag_name("option")
#         # print len(webElementsList)
#         for element in webElementsList:
#             if (element.text == value):
#                 # print element.text
#                 element.click()
#                 break
#
#     def refresh(self):
#         """
#        refresh page
#        :param - none
#        """
#         self.driver.refresh()
#
#     def take_screenshot(self, filename, save_location):
#         """
#         Save a screenshot of the current page.
#         :param filename The name of the file to save
#         :param save_location Where to save the screenshot
#         """
#         time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
#         self.driver.get_screenshot_as_file(save_location + '//' + time + '_' + filename + '.png')
#
#     def scrollElementByIdText(self, tap_element_text, tap_element_id, drag_element_text, drag_element_id):
#         """
#         Scroll element by text
#         :param element - tap element text, id, drag element text, id
#         """
#         element_to_tap = self.findElementByIdWithText(tap_element_text, tap_element_id)
#         element_to_drag_to = self.findElementByIdWithText(drag_element_text, drag_element_id)
#         self.driver.scroll(element_to_tap, element_to_drag_to)
#
#     def scrollElementByName(self, tap_element_name, drag_element_name):
#         """
#         Scroll element by name
#         :param element - tap element name, drag  element name
#         """
#         if Settings.platform in self.android_app:
#             tap_element_xpath = "//*[@text=\'" + tap_element_name + "\']"
#             drag_element_xpath = "//*[@text=\'" + drag_element_name + "\']"
#         elif Settings.platform in self.ios_app:
#             tap_element_xpath = "//*[@name=\'" + tap_element_name + "\']"
#             drag_element_xpath = "//*[@name=\'" + drag_element_name + "\']"
#         element_to_tap = self.driver.find_element_by_xpath(tap_element_xpath)
#         element_to_drag_to = self.driver.find_element_by_xpath(drag_element_xpath)
#         self.driver.scroll(element_to_tap, element_to_drag_to)
#
#     def scrollElementById(self, tap_element_id, drag_element_id):
#         """
#         Scroll element by id
#         :param element - tap element id, drag element id
#         """
#         element_to_tap = self.driver.find_element_by_id(tap_element_id)
#         element_to_drag_to = self.driver.find_element_by_id(drag_element_id)
#         self.driver.scroll(element_to_tap, element_to_drag_to)
#
#     def scroll(self, start_x, start_y, end_x, end_y, duration):
#         """
#         Scroll x,y
#         :param start x , start y, end x, end y, duration
#         """
#         self.driver.swipe(start_x, start_y, end_x, end_y, duration)
#
#     def scrollListByIdSubstring(self, direction, list_id, target_substring, target_id):
#         """
#         This finds an element with the given list_id then scrolls across it's midpoint in the direction given
#         It stops scrolling when it finds target_substring in a target_id
#         Acceptable directions are: Up, Down, Right, Left
#         Returns True if it finds the target is found, Returns False if it's not found
#         :author: bwolf
#         :param direction, list id, target substring, target id
#         """
#         element = self.driver.find_element_by_id(list_id)
#         x = element.location['x']
#         y = element.location['y']
#         height = element.size['height']
#         width = element.size['width']
#         x_offset = x + (width / 2)
#         y_offset = y + (height / 2)
#         x_start = x_offset
#         x_end = x_offset
#         y_start = y_offset
#         y_end = y_offset
#         if (direction == "Up"):
#             scroll_delta = height * .40
#             y_start = y_offset - scroll_delta
#             y_end = y_offset + scroll_delta
#         elif (direction == "Down"):
#             scroll_delta = height * .40
#             y_start = y_offset + scroll_delta
#             y_end = y_offset - scroll_delta
#         elif (direction == "Right"):
#             scroll_delta = width * .40
#             x_start = x_offset + scroll_delta
#             x_end = x_offset - scroll_delta
#         elif (direction == "Left"):
#             scroll_delta = width * .40
#             x_start = x_offset - scroll_delta
#             x_end = x_offset + scroll_delta
#         else:
#             print
#             "Direction value not supported"
#             return False
#         for i in range(self.repeatTimes):
#             if (self.isElementDisplayedByIdSubstring(target_substring, target_id)):
#                 print
#                 "Element by Text:" + str(target_substring) + " found"
#                 return True
#             else:
#                 self.scroll(x_start, y_start, x_end, y_end, 800)
#         print
#         "Element by id:" + target_substring + " not displayed"
#         return False
#
#     def scrollListById(self, direction, ele_id, locator, delta_factor=0.40, scroll_duration=800):
#         """
#         This finds an element with the given list_id then scrolls across it's midpoint in the direction given
#         Acceptable directions are: Up, Down, Right, Left
#         :author: sokumar
#         :param direction, id, locator, delta factor, duration
#
#         """
#         if locator == "By.NAME":
#             locator = "By.XPATH"
#             if Settings.platform in self.android_app:
#                 ele_id = "//*[@text=\'" + locator + "\']"
#             elif Settings.platform in self.ios_app:
#                 ele_id = "//*[@name=\'" + locator + "\']"
#         element = self.driver.find_element(locator, ele_id)
#         # element = self.driver.find_element_by_id(ele_id)
#         x = element.location['x']
#         y = element.location['y']
#         height = element.size['height']
#         width = element.size['width']
#         x_offset = x + (width / 2)
#         y_offset = y + (height / 2)
#         x_start = x_offset
#         x_end = x_offset
#         y_start = y_offset
#         y_end = y_offset
#         if (direction == "Down"):
#             scroll_delta = height * delta_factor
#             y_start = y_offset - scroll_delta
#             y_end = y_offset + scroll_delta
#         elif (direction == "Up"):
#             scroll_delta = height * delta_factor
#             y_start = y_offset + scroll_delta
#             y_end = y_offset - scroll_delta
#         elif (direction == "Left"):
#             scroll_delta = width * delta_factor
#             x_start = x_offset + scroll_delta
#             x_end = x_offset - scroll_delta
#         elif (direction == "Right"):
#             scroll_delta = width * delta_factor
#             x_start = x_offset - scroll_delta
#             x_end = x_offset + scroll_delta
#         else:
#             print
#             "Direction value not supported"
#             return False
#         self.scroll(x_start, y_start, x_end, y_end, scroll_duration)
#         print
#         "Scrolled " + direction
#
#     def scrollDownElementByIdText(self, element_text, element_id, x_offset=0, y_offset=0, scroll_delta=0):
#         """
#         Scroll element by id Text
#         :param element text, id, x, y, delta
#         """
#         'this sets the defaults to the midpoint of the screen, and 1/3 screen scroll if no offsets are specified'
#         if (x_offset == 0 and y_offset == 0 and scroll_delta == 0):
#             x_offset = self.getScreenWidth() / 2
#             y_offset = self.getScreenHeight() / 2
#             scroll_delta = self.getScreenHeight() / 3
#         'finds the scroll start and end points'
#         scroll_delta = scroll_delta / 2
#         y_start = y_offset + scroll_delta
#         y_end = y_offset - scroll_delta
#         i = 0
#         for i in range(self.repeatTimes):
#             if (self.isElementDisplayedByIdText(element_text, element_id)):
#                 print
#                 "Element by Text:" + str(element_text) + " found"
#                 return True
#             else:
#                 self.scroll(x_offset, y_start, x_offset, y_end, 800)
#         print
#         "Element by id:" + element_text + " not displayed"
#         return False
#
#     def scrollDownElementById(self, element_id, x_offset=0, y_offset=0, scroll_delta=0, repeat_times=15):
#         """
#         Scroll element by id
#         :param element text, id, x, y, delta, repeat
#         """
#         if (x_offset == 0 and y_offset == 0 and scroll_delta == 0):
#             x_offset = self.getScreenWidth() / 2
#             y_offset = self.getScreenHeight() / 2
#             scroll_delta = self.getScreenHeight() / 3
#         if repeat_times == 0:
#             repeat_times = self.repeatTimes
#         'finds the scroll start and end points'
#         scroll_delta = scroll_delta / 2
#         y_start = y_offset + scroll_delta
#         y_end = y_offset - scroll_delta
#         for i in range(repeat_times):
#             if (self.isElementPresentById(element_id)):
#                 print
#                 "Element by Text:" + str(element_id) + " found"
#                 return True
#             else:
#                 self.scroll(x_offset, y_start, x_offset, y_end, 800)
#         print
#         "Element by id:" + element_id + " not displayed"
#         return False
#
#     def scrollDownElementByIdSubstring(self, element_text, element_id, x_offset=0, y_offset=0, scroll_delta=0,
#                                        repeat_times=15):
#         """
#         Scrolls down until a element with a given ID is displayed with a given substring in its text
#         :author: bwolf
#         :param x_offset determines the line with the scroll will register
#         :param y_offset is the midpoint of the scroll
#         :param scroll_delta is how long (in pixels) the scroll will move
#         """
#         'this sets the defaults to the midpoint of the screen, and 1/3 screen scroll if no offsets are specified'
#         if (x_offset == 0 and y_offset == 0 and scroll_delta == 0):
#             x_offset = self.getScreenWidth() / 2
#             y_offset = self.getScreenHeight() / 2
#             scroll_delta = self.getScreenHeight() / 3
#         if repeat_times == 0:
#             repeat_times = self.repeatTimes
#         'finds the scroll start and end points'
#         scroll_delta = scroll_delta / 2
#         y_start = y_offset + scroll_delta
#         y_end = y_offset - scroll_delta
#         for i in range(repeat_times):
#             if (self.isSubstringPresentById(element_text, element_id)):
#                 print
#                 "Element by Text:" + str(element_text) + " found"
#                 return True
#             else:
#                 self.scroll(x_offset, y_start, x_offset, y_end, 800)
#         print
#         "Element by id:" + element_text + " not displayed"
#         return False
#
#     def scrollRightElementByIdSubstring(self, element_text, element_id, x_offset=0, y_offset=0, scroll_delta=0):
#         """
#         Scrolls down until a element with a given ID is displayed with a given substring in its text
#         :author: bwolf
#         :param x_offset determines the line with the scroll will register
#         :param y_offset is the midpoint of the scroll
#         :param scroll_delta is how long (in pixels) the scroll will move
#         """
#         'this sets the defaults to the midpoint of the screen, and 1/3 screen scroll if no offsets are specified'
#         if (x_offset == 0 and y_offset == 0 and scroll_delta == 0):
#             x_offset = self.getScreenWidth() / 2
#             y_offset = self.getScreenHeight() / 2
#             scroll_delta = self.getScreenWidth() / 3
#         'finds the scroll start and end points'
#         scroll_delta = scroll_delta / 2
#         x_start = x_offset + scroll_delta
#         x_end = x_offset - scroll_delta
#         for i in range(self.repeatTimes):
#             if (self.isElementDisplayedByIdSubstring(element_text, element_id)):
#                 print
#                 "Element by Text:" + str(element_text) + " found"
#                 return True
#             else:
#                 self.scroll(x_start, y_offset, x_end, y_offset, 800)
#         print
#         "Element by id:" + element_text + " not displayed"
#         return False
#
#     def scrollUpElementByIdSubstring(self, element_text, element_id, x_offset=0, y_offset=0, scroll_delta=0):
#         """
#         Scrolls down until a element with a given ID is displayed with a given substring in its text
#         :author: bwolf
#         :param x_offset determines the line with the scroll will register
#         :param y_offset is the midpoint of the scroll
#         :param scroll_delta is how long (in pixels) the scroll will move
#         """
#         'this sets the defaults to the midpoint of the screen, and 1/3 screen scroll if no offsets are specified'
#         if (x_offset == 0 and y_offset == 0 and scroll_delta == 0):
#             x_offset = self.getScreenWidth() / 2
#             y_offset = self.getScreenHeight() / 2
#             scroll_delta = self.getScreenHeight() / 3
#         'finds the scroll start and end points'
#         scroll_delta = scroll_delta / 2
#         y_start = y_offset - scroll_delta
#         y_end = y_offset + scroll_delta
#         i = 0
#         for i in range(self.repeatTimes):
#             if (self.isElementDisplayedByIdSubstring(element_text, element_id)):
#                 print
#                 "Element by Text:" + str(element_text) + " found"
#                 return True
#             else:
#                 self.scroll(x_offset, y_start, x_offset, y_end, 800)
#         print
#         "Element by id:" + element_text + " not displayed"
#         return False
#
#     def scrollUpElementByIdUnicodeSubstring(self, element_text, element_id, x_offset=0, y_offset=0, scroll_delta=0):
#         """
#         Scrolls down until a element with a given ID is displayed with a given substring in its text
#         :author: bwolf
#         :param x_offset determines the line with the scroll will register
#         :param y_offset is the midpoint of the scroll
#         :param scroll_delta is how long (in pixels) the scroll will move
#         """
#         'this sets the defaults to the midpoint of the screen, and 1/3 screen scroll if no offsets are specified'
#         if (x_offset == 0 and y_offset == 0 and scroll_delta == 0):
#             x_offset = self.getScreenWidth() / 2
#             y_offset = self.getScreenHeight() / 2
#             scroll_delta = self.getScreenHeight() / 3
#         'finds the scroll start and end points'
#         scroll_delta = scroll_delta / 2
#         y_start = y_offset - scroll_delta
#         y_end = y_offset + scroll_delta
#         i = 0
#         for i in range(self.repeatTimes):
#             if (self.isUnicodeSubstringPresentById(element_text, element_id)):
#                 print
#                 "Element by Text:" + str(element_text) + " found"
#                 return True
#             else:
#                 self.scroll(x_offset, y_start, x_offset, y_end, 800)
#         print
#         "Element by id:" + element_text + " not displayed"
#         return False
#
#     def scrollUpElementByIdText(self, element_text, element_id, x_offset=0, y_offset=0, scroll_delta=0):
#         """
#         Scroll element by id text
#         :param element text, id, x, y, delta
#         """
#         'this sets the defaults to the midpoint of the screen, and 1/3 screen scroll if no offsets are specified'
#         if (x_offset == 0 and y_offset == 0 and scroll_delta == 0):
#             x_offset = self.getScreenWidth() / 2
#             y_offset = self.getScreenHeight() / 2
#             scroll_delta = self.getScreenHeight() / 3
#         'finds the scroll start and end points'
#         scroll_delta = scroll_delta / 2
#         y_start = y_offset - scroll_delta
#         y_end = y_offset + scroll_delta
#         i = 0
#         for i in range(self.repeatTimes):
#             if (self.isElementDisplayedByIdText(element_text, element_id)):
#                 print
#                 "Element by Text:" + str(element_text) + " found"
#                 return True
#             else:
#                 self.scroll(x_offset, y_start, x_offset, y_end, 800)
#         print
#         "Element by id:" + element_text + " not displayed"
#         return False
#
#     def scrollDownElementByXPATH(self, xpath, x_offset=0, y_offset=0, scroll_delta=0):
#         """
#         Scroll element by xpath
#         :param element text, xpath, x, y, delta
#         """
#         'this sets the defaults to the midpoint of the screen, and 1/3 screen scroll if no offsets are specified'
#         if (x_offset == 0 and y_offset == 0 and scroll_delta == 0):
#             x_offset = self.getScreenWidth() / 2
#             y_offset = self.getScreenHeight() / 2
#             scroll_delta = self.getScreenHeight() / 3
#         'finds the scroll start and end points'
#         scroll_delta = scroll_delta / 2
#         y_start = y_offset + scroll_delta
#         y_end = y_offset - scroll_delta
#         i = 0
#         for i in range(self.repeatTimes):
#             if (self.isElementDisplayedByXpath(xpath)):
#                 print
#                 "Element by Xpath found"
#                 return True
#             else:
#                 self.scroll(x_offset, y_start, x_offset, y_end, 800)
#         print
#         "Element by Xpath not displayed"
#         return False
#
#     def scrollDownElementByName(self, name, x_offset=0, y_offset=0, scroll_delta=0):
#         """
#         Scroll element by name
#         :param element text, name
#         """
#         'this sets the defaults to the midpoint of the screen, and 1/3 screen scroll if no offsets are specified'
#         if (x_offset == 0 and y_offset == 0 and scroll_delta == 0):
#             x_offset = self.getScreenWidth() / 2
#             y_offset = self.getScreenHeight() / 2
#             scroll_delta = self.getScreenHeight() / 3
#         'finds the scroll start and end points'
#         scroll_delta = scroll_delta / 2
#         y_start = y_offset + scroll_delta
#         y_end = y_offset - scroll_delta
#         start_time = timeit.default_timer()
#         while (True):
#             if (self.isElementDisplayedByName(name)):
#                 print
#                 "Element by Text:" + str(name) + " found"
#                 return True
#             else:
#                 'self.driver.execute_script("mobile: scroll", {"direction": "down"})'
#                 self.scroll(x_offset, y_start, x_offset, y_end, 800)
#             if int(timeit.default_timer() - start_time) > 60:
#                 break
#         print
#         "Element by id:" + name + " not displayed"
#         return False
#
#     #     def scrollDownElementByName_backup(self, name, x_offset = 0, y_offset = 0, scroll_delta = 0, move_to_focus=False):
#     #         """
#     #         Scroll element by name
#     #         :param element text, name, x, y, delta, move to focus
#     #         """
#     #         'this sets the defaults to the midpoint of the screen, and 1/3 screen scroll if no offsets are specified'
#     #         if(x_offset == 0 and y_offset == 0 and scroll_delta == 0):
#     #             x_offset = self.getScreenWidth() /2
#     #             y_offset = self.getScreenHeight() /2
#     #             scroll_delta = self.getScreenHeight() /3
#     #         'finds the scroll start and end points'
#     #         scroll_delta = scroll_delta/2
#     #         y_start = y_offset + scroll_delta
#     #         y_end =  y_offset - scroll_delta
#     #         i = 0
#     #         for i in range(self.repeatTimes):
#     #             if(self.isElementDisplayedByName(name)):
#     #                 print "Element by Name:" + str(name) + " found"
#     #                 if move_to_focus:
#     #                     self.scroll(x_offset, y_start, x_offset, y_end, 800)  # To make sure the element is in focus
#     #                 return True
#     #             else:
#     #                 self.scroll(x_offset, y_start, x_offset, y_end, 800)
#     #         print "Element by id:" + name + " not displayed"
#     #         return False
#
#     def scrollUpElementByName(self, name, x_offset=0, y_offset=0, scroll_delta=0):
#         """
#         Scroll element by name
#         :param element text, name, x, y, delta
#         """
#         'this sets the defaults to the midpoint of the screen, and 1/3 screen scroll if no offsets are specified'
#         if (x_offset == 0 and y_offset == 0 and scroll_delta == 0):
#             x_offset = self.getScreenWidth() / 2
#             y_offset = self.getScreenHeight() / 2
#             scroll_delta = self.getScreenHeight() / 3
#         'finds the scroll start and end points'
#         scroll_delta = scroll_delta / 2
#         y_start = y_offset - scroll_delta
#         y_end = y_offset + scroll_delta
#         i = 0
#         for i in range(self.repeatTimes):
#             if (self.isElementDisplayedByName(name)):
#                 print
#                 "Element by Text:" + str(name) + " found"
#                 return True
#             else:
#                 self.scroll(x_offset, y_start, x_offset, y_end, 800)
#         print
#         "Element by id:" + name + " not displayed"
#         return False
#
#     def isTextPresentByLocator(self, expectedText, locator):
#         """
#         Verify text by locator
#         :param  text, locator
#         """
#         elementsFound = self.driver.find_elements_by_css_selector(locator)
#         for element in elementsFound:
#             actualText = element.text
#             if (actualText == expectedText):
#                 return True
#         try:
#             return (expectedText in self.driver.find_elements_by_css_selector(locator).text)
#         except:
#             print
#             "Text " + str(expectedText) + " not present"
#             return False
#
#     def isTextPresentById(self, expectedText, id):
#         """
#         Verify text by id
#         :param  text, id
#         """
#         elementsFound = self.driver.find_elements_by_id(id)
#         if len(elementsFound) == 0:
#             print
#             "Web Element " + id + " not found"
#
#         for element in elementsFound:
#             actualText = element.text
#             if ((type(actualText) is unicode) and not (type(expectedText) is unicode)):
#                 actualText = actualText.replace(u'\xa0', u' ').encode('utf-8')
#             if (actualText == expectedText):
#                 return True
#         try:
#             return (expectedText in self.driver.find_elements_by_id(id).text)
#         except:
#             print
#             "Text " + str(expectedText) + " not present"
#             return False
#
#     def isSubstringPresentById(self, expectedText, id):
#         """
#         Verify sub text by id
#         :param  text, id
#         """
#         elementsFound = self.driver.find_elements_by_id(id)
#         for element in elementsFound:
#             expectedText = expectedText.strip(' \n')
#             actualText = str(element.text.encode('utf-8').strip(' \n'))
#             print
#             "Checking if text in element with id %r" % id
#             print
#             "Expected Text: %s" % (expectedText)
#             print
#             "Actual Text: %s" % (actualText)
#             if (expectedText in actualText):
#                 return True
#         try:
#             return (expectedText in self.driver.find_elements_by_id(id).text)
#         except:
#             print
#             "Substring " + str(expectedText) + " not present"
#             return False
#
#     def isUnicodeSubstringPresentById(self, expectedText, id):
#         """
#         Verify unicode by id
#         :param  text, id
#         """
#         elementsFound = self.driver.find_elements_by_id(id)
#         for element in elementsFound:
#             actualText = element.text
#             print
#             "Checking if text in element with id %r" % id
#             print
#             "Expected Text: %s" % (expectedText)
#             print
#             "Actual Text: %s" % (actualText)
#             if (expectedText in actualText):
#                 return True
#
#         print
#         "Substring " + expectedText + " not present"
#         return False
#
#     def isTextPresentByXPATH(self, expectedText, xpath):
#         """
#         Verify text by xpath
#         :param  text, xpath
#         """
#         elementsFound = self.driver.find_elements_by_xpath(xpath)
#         for element in elementsFound:
#             actualText = element.text
#             if (actualText == expectedText):
#                 return True
#         try:
#             return (expectedText in self.driver.find_elements_by_id(xpath).text)
#         except:
#             print
#             "Text " + str(expectedText) + " not present"
#             return False
#
#     def isSubstringPresentByXPATH(self, expectedText, xpath):
#         """
#         Verify sub text by xpath
#         :param  text, xpath
#         """
#         elementsFound = self.driver.find_elements_by_xpath(xpath)
#         for element in elementsFound:
#             actualText = element.text
#             if (expectedText in actualText):
#                 return True
#         try:
#             return (expectedText in self.driver.find_elements_by_id(xpath).text)
#         except:
#             print
#             "Text " + str(expectedText) + " not present"
#             return False
#
#     def isTextPresent(self, expectedText):
#         """
#         Verify text present
#         :param  text
#         """
#         try:
#             return (expectedText in self.driver.find_element_by_css_selector("html>body").text)
#         except:
#             print
#             "Text:" + str(expectedText) + " not present"
#             return False
#
#     def waitForTextPresentByLocatorWithMessage(self, tester, expectedText, locator, message, repeat=5, interval=5):
#         """
#         Wait for text present by locator
#         :param  text, locator, message
#         """
#
#         i = 0
#         for i in range(repeat):
#             i = i + 1
#             if (self.isTextPresentByLocator(expectedText, locator)):
#                 return
#             try:
#                 print
#                 "waiting....."
#                 self.pause(interval)
#             except:
#                 print
#                 "Text: " + str(expectedText) + " is not present"
#
#     def waitForTextPresentByLocator(self, tester, expectedText, locator):
#         """
#         Wait for text present by locator
#         :param  text, locator, message
#         """
#         self.waitForTextPresentByLocatorWithMessage(tester, expectedText, locator,
#                                                     "There is no '" + expectedText + "' text within locator")
#
#     def waitForTextPresent(self, tester, expectedText, repeat=5, interval=5):
#         """
#         Wait for text present
#         :param  text
#         """
#
#         i = 0
#         for i in range(repeat):
#             i = i + 1
#             if (self.isTextPresent(expectedText)):
#                 return
#             try:
#                 self.pause(interval)
#             except:
#                 print
#                 "Text " + str(expectedText) + "Not Present"
#
#     def isElementPresentByLocator(self, locator):
#         """
#         Verify Element present by locator
#         :param  locator
#         """
#         try:
#
#             self.driver.implicitly_wait(2)
#             self.driver.find_element_by_css_selector(locator)
#             print
#             "check if Element by css_selector is present: " + re.sub('\W+', '', locator)
#             return True
#         except:
#
#             print
#             "Element by css_selector: " + re.sub('\W+', '', locator) + " is not present"
#             return False
#
#     def isElementPresentByLinkText(self, link_text):
#         """
#         Verify Element present by link text
#         :param  link text
#         """
#         try:
#             self.driver.implicitly_wait(2)
#             self.driver.find_element_by_link_text(link_text)
#             print
#             "check if Element by link_text is present: " + str(link_text)
#             return True
#         except:
#
#             print
#             "Element by link_text: " + str(link_text) + " is not present"
#             return False
#
#     def isElementPresentByXPATH(self, xpath):
#         """
#         Verify Element present by xpath
#         :param  xpath
#         """
#         try:
#             self.driver.implicitly_wait(2)
#             self.driver.find_element_by_xpath(xpath)
#             print
#             "check if Element by xpath is present: " + re.sub('\W+', '', xpath)
#             return True
#         except:
#
#             print
#             "Element by xpath: " + re.sub('\W+', '', xpath) + " is not present"
#             return False
#
#     def isElementPresentById(self, id):
#         """
#         Verify Element present by id
#         :param  id
#         """
#         try:
#             self.driver.implicitly_wait(2)
#             self.driver.find_element_by_id(id)
#             print
#             "check if Element by id is present: " + re.sub('\W+', '', id)
#             return True
#         except:
#
#             print
#             "Element by id: " + re.sub('\W+', '', id) + " is not present"
#             return False
#
#     def isElementNotPresentByLocator(self, locator):
#         """
#         Verify Element present by locator
#         :param  locator
#         """
#         try:
#             self.driver.implicitly_wait(2)
#             self.driver.find_element_by_css_selector(locator)
#             print
#             "Element by css_selector: " + re.sub('\W+', '', locator) + " is present"
#             return False
#         except:
#             return True
#
#     def isElementNotPresentById(self, Id):
#         """
#         Verify Element not present by id
#         :param  id
#         """
#         try:
#             self.driver.implicitly_wait(2)
#             self.driver.find_element_by_id(Id)
#             print
#             "Element by ID: " + re.sub('\W+', '', Id) + " is present"
#             return False
#         except:
#             return True
#
#     def isElementNotPresentByXpath(self, xpath):
#         """
#         Verify Element not present by xpath
#         :param  xpath
#         """
#         try:
#             self.driver.implicitly_wait(2)
#             self.driver.find_element_by_xpath(xpath)
#             print
#             "Element by xpath: " + re.sub('\W+', '', xpath) + " is present"
#             return False
#         except:
#             return True
#
#     def isElementNotPresentByName(self, name):
#         """
#         Verify Element not present by name
#         :param  name
#         """
#         if Settings.platform in self.android_app:
#             ele_xpath = "//*[@text=\'" + name + "\']"
#         elif Settings.platform in self.ios_app:
#             ele_xpath = "//*[@name=\'" + name + "\']"
#         try:
#             self.driver.implicitly_wait(2)
#             self.driver.find_element_by_xpath(ele_xpath)
#             print
#             "Element by name: " + re.sub('\W+', '', name) + " is present"
#             return False
#         except:
#             print
#             "check if Element by name is NOT present: " + re.sub('\W+', '', name)
#             return True
#
#     def isElementPresent(self, byCriteria, value):
#         """
#         Verify Element present by criteria
#         :param  criteria, value
#         """
#         if byCriteria == "By.NAME":
#             byCriteria = "By.XPATH"
#             if Settings.platform in self.android_app:
#                 value = "//*[@text=\'" + value + "\']"
#             elif Settings.platform in self.ios_app:
#                 value = "//*[@name=\'" + value + "\']"
#         try:
#             self.driver.implicitly_wait(2)
#             self.driver.find_element(by=byCriteria, value=value)
#             return True
#
#         except:
#             print
#             "Element by criteria: " + str(byCriteria) + " is not present"
#
#             return False
#
#     def isElementPresentByName(self, name):
#         """
#         Verify Element present by name
#         :param  name
#         """
#         if Settings.platform in self.android_app:
#             ele_xpath = "//*[@text=\'" + name + "\']"
#         elif Settings.platform in self.ios_app:
#             ele_xpath = "//*[@name=\'" + name + "\']"
#         try:
#             self.driver.implicitly_wait(2)
#             self.driver.find_element_by_xpath(ele_xpath)
#             print
#             "check if Element by name is present: " + re.sub('\W+', '', name)
#             return True
#         except:
#             print
#             "Element by name:" + re.sub('\W+', '', name) + " not present"
#             return False
#
#     def isElementDisplayed(self, locator):
#         """
#         Verify Element not displayed by locator
#         :param  locator
#         """
#         try:
#             self.driver.implicitly_wait(2)
#             return self.driver.find_element_by_css_selector(locator).is_displayed()
#         except:
#             print
#             "Element by locator:" + re.sub('\W+', '', locator) + " not present"
#             return False
#
#     def isElementDisplayedById(self, id):
#         """
#         Verify Element not displayed by id
#         :param  id
#         """
#         try:
#             self.driver.implicitly_wait(2)
#             return self.driver.find_element_by_id(id).is_displayed()
#         except:
#             print
#             "Element by locator:" + re.sub('\W+', '', id) + " not displayed"
#             return False
#
#     def isElementDisplayedByName(self, name):
#         """
#         Verify Element not displayed by name
#         :param  name
#         """
#         if Settings.platform in self.android_app:
#             ele_xpath = "//*[@text=\'" + name + "\']"
#         elif Settings.platform in self.ios_app:
#             ele_xpath = "//*[@name=\'" + name + "\']"
#         try:
#             self.driver.implicitly_wait(2)
#             return self.driver.find_element_by_xpath(ele_xpath).is_displayed()
#         except:
#             print
#             "Element by locator:" + re.sub('\W+', '', str(name)) + " not present"
#             return False
#
#     def isElementDisplayedByXpath(self, xpath):
#         """
#         Verify Element not displayed by xpath
#         :param  xpath
#         """
#         try:
#             self.driver.implicitly_wait(2)
#             return self.driver.find_element_by_xpath(xpath).is_displayed()
#         except:
#             print
#             "Element by locator:" + re.sub('\W+', '', xpath) + " not present"
#             return False
#
#     def isElementDisplayedByIdText(self, text, id):
#         """
#         Verify Element not displayed by id Text
#         :param  text, id
#         """
#         webElements = []
#         webElements = self.driver.find_elements_by_id(id)
#
#         for element in webElements:
#             print
#             "ELEMENT : " + element.text
#             textActual = element.text
#             if ((type(textActual) is unicode) and not (type(text) is unicode)):
#                 textActual = textActual.replace(u'\xa0', u' ').encode('utf-8')
#             if (textActual == text):
#                 return element.is_displayed()
#         print
#         "Element by id:" + re.sub('\W+', '', id) + " " + re.sub('\W+', '', str(text)) + " not present"
#         return False
#
#     def isElementDisplayedByIdSubstring(self, text, id):
#         """
#         Verify given text is a substring of the element's text
#         :param  text, id
#         """
#         webElements = []
#         webElements = self.driver.find_elements_by_id(id)
#         for element in webElements:
#             textActual = element.text
#             if type(textActual) is unicode:
#                 textActual = textActual.replace(u'\xa0', u' ').encode('utf-8')
#             if (text in textActual):
#                 return element.is_displayed()
#         print
#         "Element by id:" + re.sub('\W+', '', id) + " " + re.sub('\W+', '', text) + " not present"
#         return False
#
#     def isElementEnabled(self, locator):
#         """
#         Verify if element is enabled by locator
#         :param  locator
#         """
#         try:
#             self.driver.implicitly_wait(2)
#             return self.driver.find_element_by_css_selector(locator).is_enabled()
#         except:
#             return False
#
#     def isElementEnabledbyName(self, name):
#         """
#         Verify if element is enabled by name
#         :param  name
#         """
#         if Settings.platform in self.android_app:
#             ele_xpath = "//*[@text=\'" + name + "\']"
#         elif Settings.platform in self.ios_app:
#             ele_xpath = "//*[@name=\'" + name + "\']"
#         try:
#             self.driver.implicitly_wait(2)
#             return self.driver.find_element_by_xpath(ele_xpath).is_enabled()
#         except:
#             return False
#
#     def isElementEnabledWithText(self, text, locator):
#         """
#         Verify if element is enabled by locator and text
#         :param  text, locator
#         """
#         try:
#             self.driver.implicitly_wait(2)
#             return self.findElementWithText(text, locator).is_enabled()
#         except:
#             return False
#
#     def waitForElementEnabledWithText(self, tester, text, locator, repeat=5, interval=5):
#         """
#         Wait for element is enabled by locator and text
#         :param  text, locator
#         """
#
#         i = 0
#         for i in range(repeat):
#             i = i + 1
#             if (self.isElementEnabledWithText(text, locator)):
#                 return
#             try:
#                 self.pause(interval)
#             except:
#                 print
#                 "Element not enabled"
#
#     def waitForElementPresentByLocatorWithMessage(self, tester, locator, message, repeat=5, interval=5):
#         """
#         Wait for element is enabled by locator
#         :param  locator, message
#         """
#
#         i = 0
#         for i in range(repeat):
#             i = i + 1
#             if (self.isElementPresentByLocator(locator)):
#                 return
#             try:
#                 'waiting...'
#                 self.pause(interval)
#             except:
#                 print
#                 "Element by locator:" + re.sub('\W+', '', locator) + " not present"
#
#     def waitForElementPresentByIdWithMessage(self, tester, id, message, repeat=5, interval=5):
#         """
#         Wait for element is present by id
#         :param  id
#         """
#
#         i = 0
#         for i in range(repeat):
#             i = i + 1
#             if (self.isElementPresentById(id)):
#                 return
#             try:
#                 'waiting...'
#                 self.pause(interval)
#             except:
#                 print
#                 "Element by locator:" + re.sub('\W+', '', id) + " not present"
#
#     def waitForElementPresentByLocator(self, tester, locator):
#         """
#         Wait for element is present by locator
#         :param  locator
#         """
#         self.waitForElementPresentByLocatorWithMessage(tester, locator,
#                                                        "Element by" + str(locator) + " not present on page!")
#
#     def waitForElementPresentById(self, tester, id):
#         """
#         Wait for element is present by id
#         :param  id
#         """
#         self.waitForElementPresentByIdWithMessage(tester, id, "Element by" + str(id) + " not present on page!")
#
#     def waitForElementDisplayedByLocatorWithMessage(self, tester, locator, message, repeat=5, interval=5):
#         """
#         Wait for element is present by locator
#         :param  locator
#         """
#
#         i = 0
#         for i in range(repeat):
#             i = i + 1
#             if (self.isElementDisplayed(locator)):
#                 return
#             try:
#                 self.pause(interval)
#             except:
#                 print
#                 "Element by locator:" + re.sub('\W+', '', locator) + " not displayed"
#         # tester.assertTrue((self.isElementPresentByLocator(locator)), message)
#
#     def waitForElementDisplayedByIdWithMessage(self, tester, id, message=None, repeat=5, interval=5):
#         """
#         Wait for element is present by id
#         :param  id
#         """
#
#         i = 0
#         for i in range(interval):
#             if (self.isElementDisplayedById(id)):
#                 print
#                 "Element by id:" + str(id) + "found"
#                 return True
#             else:
#                 self.pause(interval)
#         print
#         "Element by id:" + re.sub('\W+', '', id) + " not displayed" + message
#         return False
#
#     def waitForElementDisplayedByXpathWithMessage(self, tester, xpath, message=None, repeat=5, interval=5):
#         """
#         Wait for element is present by xpath
#         :param  xpath
#         """
#
#         i = 0
#         for i in range(repeat):
#             if (self.isElementDisplayedByXpath(xpath)):
#                 print
#                 "Element by xpath:" + re.sub('\W+', '', xpath) + "found"
#                 return True
#             else:
#                 self.pause(interval)
#         print
#         "Element by xpath:" + re.sub('\W+', '', xpath) + " not displayed" + message
#         return False
#
#     def waitForElementDisplayedByLocator(self, tester, locator):
#         """
#         Wait for element is displayed by locator
#         :param  locator
#         """
#         self.waitForElementDisplayedByLocatorWithMessage(tester, locator,
#                                                          "Element by" + str(locator) + " not present on page!")
#
#     def waitForElementPresentAndVisible(self, tester, locator):
#         """
#         Wait for element is present and visible
#         :param  id
#         """
#         self.waitForElementPresentByLocator(tester, locator)
#         self.waitForElementDisplayedByLocator(tester, locator)
#
#     def waitForElementEnabled(self, tester, locator):
#         """
#         Wait for element is enabled
#         :param  locator
#         """
#         self.waitForElementEnabledByLocatorWithMessage(tester, locator, "Element by" + str(locator) + " is not enabled")
#
#     def waitForElementEnabledByLocatorWithMessage(self, tester, locator, message, repeat=5, interval=5):
#         """
#         Wait for element is enabled
#         :param  locator
#         """
#
#         i = 0
#         for i in range(repeat):
#             i = i + 1
#             if (self.isElementEnabled(locator)):
#                 return
#             try:
#                 self.pause(interval)
#             except:
#                 print
#                 "Element by locator:" + re.sub('\W+', '', locator) + "not enabled"
#         tester.assertTrue((self.isElementEnabled(locator)), message)
#
#     def waitForTitle(self, tester, title):
#         """
#          Will wait for some time until the page title will be shown
#          :param title - page title
#         """
#         self.waitForTitleWithExtraTime(tester, title, 0)
#
#     def isTitlePresent(self, tester, title):
#         """
#          Is the specified title present on page
#          :param title - Page Title
#          :return - true if title present, else in other case
#         """
#         return tester.assertEquals(self.driver.title.strip(), title,
#                                    "Current title is equal '" + self.driver.title.strip() + "', but expected to be '" + title + "'")
#
#     def isTextNotPresentByCssSelector(self, expectedText, locator):
#         """
#         verify text is not present
#         :param  locator
#         """
#         elementsFound = self.driver.find_elements_by_css_selector(locator)
#         for element in elementsFound:
#             if (element.text == expectedText):
#                 return False
#         return True
#
#     def isTextNotPresentById(self, expectedText, locator):
#         """
#         verify text is not present
#         :param  locator
#         @author: sokumar
#         """
#         elementsFound = self.driver.find_elements_by_id(locator)
#         for element in elementsFound:
#             if (element.text == expectedText):
#                 return False
#         return True
#
#     def isTextNotPresent(self, expectedText):
#         """
#         verify text is not present
#         :param  text
#         """
#         try:
#             result = expectedText not in (self.driver.find_element_by_css_selector("html>body").text)
#             return result
#         except:
#             print
#             "Text:" + str(expectedText) + " is not present"
#         return False
#
#     def waitForElementPresentByLocatorWithMessage_OK(self, tester, locator, message, repeat=5, interval=5):
#         """
#         Wait for element
#         :param  locator
#         """
#
#         i = 0
#         for i in range(repeat):
#             i = i + 1
#             try:
#                 if (self.isElementPresentByLocator(locator)):
#                     return
#                 self.pause(interval)
#             except:
#                 pass
#                 print
#                 "Element not present"
#         tester.assertTrue((self.isElementPresentByLocator(locator)), message)
#
#     '''
#     Using Web Driver Wait
#     '''
#
#     def isElementPresentByLocator_OK(self, locator):
#         """
#         Verify element present
#         :param  locator
#         """
#         wait = WebDriverWait(self.driver, 10)
#
#         def present(element):
#             if element.is_displayed():
#                 return element
#             return False
#
#         element = wait.until(lambda d: present(d.find_element_by_css_selector(locator)))
#         if (element == False):
#
#             return False
#         else:
#             return True
#
#     def waitForElementPresentWithMessage(self, tester, byCriteria, value, message, repeat=5, interval=5):
#         """
#         Wait for element present
#         :param  criteria, value
#         """
#
#         i = 0
#         for i in range(repeat):
#             i = i + 1
#             if (self.isElementPresent(byCriteria, value)):
#                 return
#             try:
#                 self.pause(interval)
#             except:
#                 print
#                 "Element by criteria:" + str(byCriteria) + " not present"
#
#     def waitForElementPresentByNameWithMessage(self, tester, name, message, repeat=5, interval=5):
#         """
#         Wait for element present by name
#         :param  name
#         """
#         i = 0
#         for i in range(repeat):
#             i = i + 1
#             if (self.isElementPresentByName(name)):
#                 return
#             try:
#                 self.pause(interval)
#             except:
#                 print
#                 "Element by name:" + str(name) + " not present"
#
#     def waitAndAssertTextPresentOnPage(self, tester, expectedText):
#         """
#         Wait and assert for text present
#         :param  text
#         """
#         self.waitForTextPresent(tester, expectedText)
#         tester.assertTrue((self.isTextPresent(expectedText)), "There is no '" + expectedText + "' text on the page")
#
#     def waitForElementPresent(self, tester, byCriteria, value):
#         """
#         Wait for element present
#         :param  criteria, value
#         """
#         self.waitForElementPresentWithMessage(tester, byCriteria, value,
#                                               "Element by" + str(byCriteria) + "=" + value + " not present on page!")
#
#     def waitForElementPresentByName(self, tester, name):
#         """
#         Wait for element present by name
#         :param  name
#         """
#         self.waitForElementPresentByNameWithMessage(tester, name,
#                                                     "Element with name =" + str(name) + " not present on page!")
#
#     def isCheckboxSelectedBySelector(self, locator):
#         """
#         Verify check box is selected
#         :param  locator
#         """
#         element = self.driver.find_element_by_css_selector(locator)
#         return element.get_attribute("checked")
#
#     def isCheckboxSelectedByID(self, id):
#         """
#         Verify check box is selected by id
#         :param  id
#         """
#         element = self.driver.find_element_by_id(id)
#         return element.get_attribute("checked")
#
#     """
#     Following are the key press
#     """
#
#     def press_back(self):
#         print
#         "Press Back"
#         self.driver.press_keycode(4)
#         self.pause(3)
#
#     def press_home(self):
#         print
#         "Press Back"
#         self.driver.press_keycode(3)
#         self.pause(3)
#
#     def press_right(self):
#         print
#         "Press right"
#         self.driver.press_keycode(22)
#         self.pause(3)
#
#     def press_left(self):
#         print
#         "Press left"
#         self.driver.press_keycode(21)
#         self.pause(3)
#
#     def press_up(self):
#         print
#         "Press up"
#         self.driver.press_keycode(19)
#         self.pause(3)
#
#     def press_down(self):
#         print
#         "Press down"
#         self.driver.press_keycode(20)
#         self.pause(3)
#
#     def press_enter(self):
#         print
#         "Press enter"
#         self.driver.press_keycode(23)
#         self.pause(3)
#
#     def tap_position(self, x, y):
#         print
#         "Tap position"
#         self.driver.tap([(x, y)])
#         self.pause(3)
#
#     def press_search(self):
#         print
#         "Press search"
#         self.driver.press_keycode(54)
#         self.pause(3)
#
#     def press_menu(self):
#         print
#         "Press Menu"
#         self.driver.press_keycode(82)
#         self.pause(5)
#
#     def device_landscape(self):
#         print
#         "Rotate to landscape"
#         self.driver.orientation = 'LANDSCAPE'
#
#     def device_portrait(self):
#         print
#         "Rotate to portrait"
#         self.driver.orientation = 'PORTRAIT'
#
#     def hide_keyboard(self):
#         try:
#             self.driver.hide_keyboard()
#         except:
#             pass
#
#     def ilovefan(self):
#         """
#         workaround for checking the I love fan button
#         """
#         print
#         "checking for the I love fan popup"
#         if (self.settings.platform == "AndroidApp"):
#             try:
#                 pass
#                 # self.clickButtonByTextById("No, I don't love Fan TV.", "android:id/text1")
#             except:
#                 pass
#
#     def swipeLeftElementByXpath(self, xpath):
#         """
#         swipe left by xpath
#         :param  xpath
#         """
#         i = 0
#         for i in range(self.repeatTimes):
#             if (self.isElementDisplayedByXpath(xpath)):
#                 print
#                 "Element by Xpath:" + re.sub('\W+', '', xpath) + " found"
#                 return
#             else:
#                 self.scroll(320, 373, 84, 373, 500)
#         print
#         "Element by xpath:" + re.sub('\W+', '', xpath) + " not displayed"
#
#     def swipeRightElementByXpath(self, xpath):
#         """
#         swipe right by xpath
#         :param  xpath
#         """
#         i = 0
#         for i in range(self.repeatTimes):
#             if (self.isElementDisplayedByXpath(xpath)):
#                 print
#                 "Element by Xpath:" + re.sub('\W+', '', xpath) + " found"
#                 return
#             else:
#                 self.scroll(84, 373, 320, 373, 500)
#         print
#         "Element by xpath:" + re.sub('\W+', '', xpath) + " not displayed"
#
#     def getScreenHeight(self):
#         """
#         returns the window's height as an int
#         """
#         return self.driver.get_window_size()['height']
#
#     def getScreenWidth(self):
#         """
#         returns the window's width as an int
#         """
#         return self.driver.get_window_size()['width']
#
#     def swipeLeftElementByName(self, name):
#         """
#         swipe left by name
#         :param  name
#         """
#         i = 0
#         for i in range(self.repeatTimes):
#             if (self.isElementDisplayedByName(name)):
#                 print
#                 "Element by Name:" + re.sub('\W+', '', name) + " found"
#                 return
#             else:
#                 self.scroll(320, 373, 84, 373, 500)
#         print
#         "Element by Name:" + re.sub('\W+', '', name) + " not displayed"
#
#     def swipeRightElementByName(self, name):
#         """
#         swipe right by name
#         :param  name
#         """
#         i = 0
#         for i in range(self.repeatTimes):
#             if (self.isElementDisplayedByName(name)):
#                 print
#                 "Element by Name:" + re.sub('\W+', '', name) + " found"
#                 return
#             else:
#                 self.scroll(84, 373, 320, 373, 500)
#         print
#         "Element by Name:" + re.sub('\W+', '', name) + " not displayed"
#
#     def tapOnCenterScreen(self):
#         """
#         Hard tap on screen
#         """
#         self.driver.tap(1, 134, 526, 1)
#
#     def wait_for_element_by_name(self, name, repeat=5, interval=2):
#         """
#         Wait for element by name
#         :param  name
#         """
#         i = 0
#         self.pause(interval)
#         for i in range(repeat):
#             i = i + 1
#             if (self.isElementPresentByName(name)):
#                 return
#             try:
#                 'waiting...'
#                 self.pause(interval)
#             except:
#                 print
#                 "Element by Name:" + re.sub('\W+', '', name) + " not present"
#
#     def wait_for_element_by_xpath(self, xpath, repeat=5, interval=5):
#         """
#         Wait for element by xpath
#         :param  xpath
#         """
#         i = 0
#         for i in range(repeat):
#             i = i + 1
#             if (self.isElementPresentByXPATH(xpath)):
#                 return
#             try:
#                 'waiting...'
#                 self.pause(interval)
#             except:
#                 print
#                 "Element by Xpath:" + re.sub('\W+', '', xpath) + " not present"
#
#     def tap_element_by_coordinates(self, x, y):
#         """
#         Tap on screen x,y
#         :parm x,y
#         """
#         self.pause(2)
#         self.driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": x, "y": y})
#         self.pause(2)
#
#     def typeTextByKey(self, text):
#         """
#         Input text by using android key code
#         :parm text
#         """
#         key_code = {
#             "A": 29,
#             "B": 30,
#             "C": 31,
#             "D": 32,
#             "E": 33,
#             "F": 34,
#             "G": 35,
#             "H": 36,
#             "I": 37,
#             "J": 38,
#             "K": 39,
#             "L": 40,
#             "M": 41,
#             "N": 42,
#             "O": 43,
#             "P": 44,
#             "Q": 45,
#             "R": 46,
#             "S": 47,
#             "T": 48,
#             "U": 49,
#             "V": 50,
#             "W": 51,
#             "X": 52,
#             "Y": 53,
#             "Z": 54
#         }
#
#         for k in text.upper():
#             self.driver.press_keycode(key_code[k])
#
#     def wait_on_loading_spinner(self):
#         """
#         This waits until the search progress spinner disappears to a max of 15 seconds (+4 sec)
#         :param none
#         """
#         print("Waiting for items.")
#         self.pause(3)
#         i = 0
#         while (self.isElementDisplayedById(self.LOC_SEARCH_PROGRESS_SPINNER) and i < 15):
#             i += 1
#             print("Still waiting... " + str(i))
#             self.pause(1)
#         self.pause(1)
#
#     def get_zone_current_time(self, date_format='%r', zone='UTC'):
#         '''
#         Method returns current time of given zone in specified format
#         '''
#         date = datetime.now(tz=pytz.utc)
#         date = date.astimezone(timezone(zone))
#         return date.strftime(date_format)
#
#
#
#
#

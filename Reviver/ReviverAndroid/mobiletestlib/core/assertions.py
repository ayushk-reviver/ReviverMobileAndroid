#from appium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
from mobiletestlib.core.base import AppiumBaseClass
import re
import time


class AppiumAssertions(object):

    '''
    classdocs
    '''
    # repeatTimes = 15
    # waitTime = 1000
    #
    # def assertTextPresent(self, tester, expectedText):
    #     print
    #     "asserting Text " + expectedText
    #     tester.assertTrue((self.isTextPresent(expectedText)), "Text \"" + str(
    #         expectedText) + "\" not present on page!" + self.driver.find_element_by_css_selector("html>body").text)
    #
    # def assertElementPresentById(self, tester, id):
    #
    #     tester.assertTrue((self.isElementPresentById(id)), "Element by id \"" + str(id) + "\" not present on page!")
    #
    # def assertElementPresentByName(self, tester, name, partial_match=None):
    #     print
    #     "asserting element availability :  ByName - " + name
    #     if not self.isElementPresentByName(name):
    #         raise NoSuchElementException("Element not found : ByName - %s" % name)
    #
    # def assertElementPresentByName_xpath(self, tester, name, xpath):
    #     print
    #     "asserting element availability :  ByName - " + name
    #     found_element = False
    #     if name != "none":
    #         if isinstance(xpath, list):
    #             for path in xpath:
    #                 webElements = self.driver.find_elements_by_xpath(path)
    #                 for element in webElements:
    #                     textActual = element.text
    #                     if textActual == name or name in textActual:
    #                         found_element = True
    #         else:
    #             webElements = self.driver.find_elements_by_xpath(xpath)
    #             for element in webElements:
    #                 textActual = element.text
    #                 if textActual == name or name in textActual:
    #                     found_element = True
    #     if not found_element:
    #         raise NoSuchElementException("Element not found : ByName - %s" % name)
    #
    # def assertTextNotPresent(self, tester, expectedText):
    #
    #     tester.assertTrue((self.isTextNotPresent(expectedText)),
    #                       "Text \"" + str(expectedText) + "\" is present on page!")
    #
    # def assertTextNotPresentById(self, tester, expectedText, locator):
    #     tester.assertTrue((self.isTextNotPresentById(expectedText, locator)),
    #                       "Text \"" + str(expectedText) + "\" is present on page!")
    #
    # def assertTextPresentByLocator(self, tester, expectedText, locator):
    #     print
    #     "asserting Text " + expectedText
    #     tester.assertTrue((self.isTextPresentByLocator(expectedText, locator)),
    #                       "Text \"" + str(expectedText) + " by Locator " + str(locator) + " not present")
    #
    # def assertTextPresentById(self, tester, expectedText, Id):
    #     print
    #     "asserting Text " + expectedText + " in " + re.sub('\W+', '', Id)
    #     tester.assertTrue((self.isTextPresentById(expectedText, Id)),
    #                       "Text \"" + str(expectedText) + " by Id " + str(Id) + " not present")
    #
    # def assertSubstringPresentById(self, tester, expectedText, Id):
    #     print
    #     "asserting Text " + expectedText + " in " + Id
    #     tester.assertTrue((self.isSubstringPresentById(expectedText, Id)),
    #                       "Substring \"" + str(expectedText) + " by Id " + str(Id) + " not present")
    #
    # def assertUnicodeSubstringPresentById(self, tester, expectedText, Id):
    #     print
    #     "asserting Text " + expectedText + " in " + Id
    #     tester.assertTrue((self.isUnicodeSubstringPresentById(expectedText, Id)),
    #                       "Substring \"" + expectedText + " by Id " + str(Id) + " not present")
    #
    # def assertSubstringPresentByXPATH(self, tester, expectedText, xpath):
    #     print
    #     "asserting Substring " + expectedText + " in " + xpath
    #     tester.assertTrue((self.isSubstringPresentByXPATH(expectedText, xpath)),
    #                       "Substring \"" + str(expectedText) + " by xpath " + str(xpath) + " not present")
    #
    # def assertTextPresentByXPATH(self, tester, expectedText, xpath):
    #     print
    #     "asserting Text " + expectedText + " in " + xpath
    #     tester.assertTrue((self.isTextPresentByXPATH(expectedText, xpath)),
    #                       "Text \"" + str(expectedText) + " by xpath " + str(xpath) + " not present")
    #
    # def assertTextNotPresentByLocator(self, tester, expectedText, locator):
    #     tester.assertTrue((self.isTextNotPresentByCssSelector(expectedText, locator)),
    #                       "Text \"" + str(expectedText) + " by Locator " + str(locator) + " present")
    #
    # def assertLabelPresentByLocator(self, tester, label, locator):
    #     tester.assertTrue((self.isTextPresentByLocator(label, locator)),
    #                       "Label \"" + str(label) + " by Locator " + str(locator) + " not present")
    #
    # def assertElementContainsText(self, tester, expectedText, locator):
    #     print
    #     "asserting Text " + expectedText
    #     # print str(self.driver.find_element_by_css_selector(locator).text)
    #     tester.assertTrue((self.isTextPresentByLocator(expectedText, locator)),
    #                       "Text \"" + str(expectedText) + " by Locator " + str(locator) + " not present")
    #     # self.assertTrue((expectedText in self.driver.find_element_by_css_selector(locator).text), "Element does not contain " + expectedText)
    #
    # def assertElementContainsTextById(self, tester, expectedText, id):
    #
    #     tester.assertTrue((self.isTextPresentById(expectedText, id)),
    #                       "Text \"" + str(expectedText) + " by Locator " + str(id) + " not present")
    #
    # def assertElementPresentByLocator(self, tester, locator):
    #
    #     tester.assertTrue((self.isElementPresentByLocator(locator)),
    #                       "Element by locator \"" + str(locator) + "\" not present on page!")
    #
    # def assertElementPresentByLinkText(self, tester, link_text):
    #     tester.assertTrue((self.isElementPresentByLinkText(link_text)),
    #                       "Element by link_text \"" + str(link_text) + "\" not present on page!")
    #
    # def assertElementPresentByXPATH(self, tester, xpath):
    #     tester.assertTrue((self.isElementPresentByXPATH(xpath)),
    #                       "Element by link_text \"" + str(xpath) + "\" not present on page!")
    #
    # def isElementSelected(self, locator):
    #     if (self.driver.find_element_by_css_selector(locator).is_selected()):
    #         return True
    #     else:
    #         return False
    #
    # def isElementSelectedById(self, id):
    #     if (self.driver.find_element_by_id(id).is_selected()):
    #         return True
    #     else:
    #         return False
    #
    # def isElementWithTextSelected(self, expectedText, locator):
    #     result = False
    #     elementsFound = self.driver.find_elements_by_css_selector(locator)
    #     for element in elementsFound:
    #         actualText = element.text
    #         if (actualText == expectedText):
    #
    #             print
    #             actualText
    #             print
    #             str(element)
    #             print
    #             str(element.is_selected())
    #             if (element.is_selected()):
    #                 result = True
    #             else:
    #                 result = False
    #
    #     return result
    #
    # def assertElementPresent(self, tester, byCriteria, value):
    #     if (self.isElementPresent(byCriteria, value)):
    #         print
    #         "True"
    #     else:
    #         print
    #         "False"
    #     tester.assertTrue((self.isElementPresent(byCriteria, value)),
    #                       "Element by criteria: \"" + str(byCriteria) + "\" not present on page!")
    #
    # def waitForTitleWithExtraTime(self, tester, title, extra_milliseconds):
    #     waitInterval = self.waitTime + int(extra_milliseconds) / 100;
    #
    #     try:
    #         # Wait before checking the page
    #         self.pause(1);
    #     except:
    #         print
    #         "Element not present"
    #     i = 0
    #     for i in xrange(self.repeatTimes):
    #         i = i + 1
    #         if (self.driver.title.strip() == title):
    #             print
    #             self.driver.title.strip()
    #             return
    #         else:
    #             try:
    #                 self.pause(waitInterval)
    #             except:
    #                 print
    #                 "Title:" + title + "not present"
    #
    #     tester.assertEquals(self.driver.title.strip(), title,
    #                         "Current title is equal '" + self.driver.title.strip() + "', but expected to be '" + title + "'")
    #
    # '''
    #  Assert title present on page
    #  @param title - Page Title
    # '''
    #
    # def assertTitle(self, tester, title):
    #     tester.assertTrue(self.isTitlePresent(title))
    #
    # def assertElementNotPresentByLocator(self, tester, locator):
    #     tester.assertFalse((self.isElementNotPresentByLocator(locator)),
    #                        "Element by locator \"" + str(locator) + "\" presents on page!")
    #
    # def assertElementNotPresentByXpath(self, tester, xpath):
    #     tester.assertFalse((self.isElementNotPresentByXpath(xpath)),
    #                        "Element by xpath \"" + str(xpath) + "\" presents on page!")
    #
    # def assertElementNotDisplayedById(self, tester, id):
    #     tester.assertFalse((self.isElementDisplayedById(id)), "Element by id \"" + str(id) + "\" displayed on page!")
    #
    # def assertElementNotPresentByName(self, tester, name):
    #     tester.assertFalse((self.isElementPresentByName(name)),
    #                        "Element by name \"" + str(name) + "\" not present on page!")
    #
    # def assertCheckboxNotSelectedBySelector(self, tester, locator):
    #     element = self.driver.find_element_by_css_selector(locator)
    #     tester.assertFalse(element.get_attribute("checked"))
    #
    # def assertCheckboxSelectedBySelector(self, tester, locator):
    #     element = self.driver.find_element_by_css_selector(locator)
    #     tester.assertTrue(element.get_attribute("checked"))

    def waitTillElementVisibleByXpathThanClick(self,tester,xpath):
        try:
            element=WebDriverWait(tester, 10).until(ec.visibility_of_element_located((By.XPATH, xpath)))
            element.click()
        except:
            print("waitTillElementVisibleByXpathThanClick failed")

    def waitTillElementVisibleByXpath(self, tester, xpath):
        try:
            element = WebDriverWait(tester, 10).until(ec.visibility_of_element_located((By.XPATH, xpath)))
            if(element.is_displayed()):
                return True
        except:
            print("waitTillElementVisibleByXpath failed")


    def verifyElementPresentByXpath(self,tester,xpath):
        try:
            element=tester.find_element_by_xpath(xpath)
            if(element.is_displayed()):
                return True
            else:
                return False
        except:
            print("verifyElementPresentByXpath failed")
            return False

    def sendTextInFieldByXpath(self,tester,text,xpath):
        try:
            tester.find_element_by_xpath(xpath).send_keys(text)
        except:
            print("sendTextInFieldByXpath failed")

    def tapOnElementByXpath(self,tester,xpath):
        try:
            tester.find_element_by_xpath(xpath).click()
        except:
            print("tapOnElementByXpath failed")


    def touchByBounds(self,tester,x,y):
        actions = TouchAction(tester)
        actions.tap(None, x, y, 1).perform()

    def waitForSomeTimeInSeconds(self,sec):
        time.sleep(sec)

    def getTextFromElementByXpath(self,tester,xpath):
        try:
            element = tester.find_element_by_xpath(xpath)
            return str(element.text)
        except:
            print("getTextFromElementByXpath failed")
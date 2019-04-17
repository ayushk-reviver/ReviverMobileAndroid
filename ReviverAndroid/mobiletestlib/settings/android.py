'''
Created on March 18, 2019
@author: rkaur
'''


class BaseAndroidSettings(object):

        '''

        needs to be updated
        if settings.build.upper() == "DEBUG" or "Debug" in settings.platform:
                PACKAGE_NAME = "tv.fan.mobile.debug"
        else:
                PACKAGE_NAME = "tv.fan.mobile"

        '''

        env = "QA"
        desired_caps = {
                "platformName": "Android",
                "deviceName": "FA7AD1A03350",
                "appPackage": "com.reviverauto.rplate",
                "appActivity": "com.reviverauto.rplate.SplashActivity",
                "noReset": "true"
        }
        desired_caps2 = {
                "platformName": "Android",
                "deviceName": "FA7AD1A03350",
                "appPackage": "com.reviverauto.rplate",
                "appActivity": "com.reviverauto.rplate.SplashActivity",
                "app":"C:/Users/akumar60/Desktop/Apks/Rplate_com.reviverauto.rplate.apk",
                "noReset": "false"
        }
        hub = "http://127.0.0.1:4723/wd/hub"

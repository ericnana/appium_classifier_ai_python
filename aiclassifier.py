#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
#import time





class TestAI_ClassifierDemoTest(unittest.TestCase):
    
    def setUp(self):
       desired_caps = {}
       desired_caps['platformName'] = 'Android'
       desired_caps['deviceName'] = 'Android Emulator'
       desired_caps['uiautomationName'] = 'UiAutomator2'
       
       #desired_caps['appPackage'] = 'com.ebay.mobile'
       #desired_caps['appActivity'] = 'com.ebay.mobile.activities.MainActivity'
       
       #desired_caps['appPackage'] = 'com.walmart.mg'
       #desired_caps['appActivity'] = 'com.mx.walmart.walmartgroceries.MainActivity'
       
       desired_caps['appPackage'] = 'com.android.settings'
       desired_caps['appActivity'] = 'com.android.settings.Settings'
       
       desired_caps['skipServerInstallation'] = True
       desired_caps['customFindModules'] = {'ai':'test-ai-classifier'}
       desired_caps['shouldUseCompactResponses'] = False
        
       self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
       
       #self.driver.implicitly_wait(5)

        
    def tearDown(self):
        self.driver.quit()
        
    
    def test_ai(self):
        self.driver.implicitly_wait(20)
        #time.sleep(20)
        
        #search = self.driver.find_element_by_custom('ai:search')
        search = self.driver.find_element(MobileBy.CUSTOM, 'ai:search')
        search.click()
        self.driver.implicitly_wait(20)

        #time.sleep(10)

if __name__== '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAI_ClassifierDemoTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
        


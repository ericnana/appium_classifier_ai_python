#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
#import org.openqa.selenium.By; 
#import org.openqa.selenium.WebElement;
#from selenium.webdriver.remote.webdriver import WebDriver
import time






class TestAI_ClassifierDemoTest(unittest.TestCase):
    
    def setUp(self):
       desired_caps = {}
       desired_caps['platformName'] = 'Android'
       desired_caps['deviceName'] = 'Android Emulator'#enter adb device
       desired_caps['uiautomationName'] = 'UiAutomator2'
       desired_caps['appPackage'] = 'com.ebay.mobile'
       desired_caps['appActivity'] = 'com.ebay.mobile.activities.MainActivity'
       desired_caps['customFindModules'] = {'ai':'test-ai-classifier'}
       desired_caps['shouldUseCpactResponse'] = False
        
        
       self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
        
       
        
    def tearDown(self):
        self.driver.quit()
        
    
    def test_ai(self):
        time.sleep(20)
        #mobileby = MobileBy.CUSTOM
        #search = self.driver.find_element_by_custom("ai:search")
        search = self.driver.find_element_by_custom('ai:cart')

        search.click()
        time.sleep(10)

if __name__== '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAI_ClassifierDemoTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
        


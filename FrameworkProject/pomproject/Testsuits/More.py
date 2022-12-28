import pytest
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
from FrameworkProject.pomproject.pages.loginPage import loginPage
from FrameworkProject.pomproject.pages.employeepage import employeepage
from FrameworkProject.pomproject.pages.searchpage import searchpage
from FrameworkProject.pomproject.pages.MorePage import MorePage

#/**
#*
#* @author JALA Academy
#*
#*
#*
#*
#*/

class MoreTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #browser lunching and maximizing the window
        cls.driver=webdriver.Chrome(executable_path=".\\chromedriver_win32\\chromedriver.exe")
        cls.driver.maximize_window()


    def test_more(self):
       driver = self.driver
       # entering the url of the application we are performing
       driver.get('https://magnus.jalatechnologies.com/')
       login = loginPage(driver)
       login.enter_username("training@jalaacademy.com")
       login.enter_password("jobprogram")
       login.click_login()
       time.sleep(2)

       # selecting more option
       more = MorePage(driver)

       more.select_more()
       # selecting multiple tabs
       more.select_multipletabs()
       time.sleep(2)
       more.select_plantosucceed()
       time.sleep(2)
       more.enter_textbox1('Thank you')
       more.enter_textbox2('For login')
       time.sleep(2)
       # selecting popups
       more.select_popup()
       time.sleep(2)
       more.select_popup1()
       more.select_popup2()
       more.select_popup3()
       time.sleep(2)

    def tearDown(self):
        # closing the browser after the login
        self.driver.close()
        self.driver.quit()
        print('Login test completed and employee id is created')

if __name__ == '__main__':
    unittest.main





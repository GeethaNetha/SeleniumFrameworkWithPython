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


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #browser lunching and maximizing the window
        cls.driver=webdriver.Chrome(executable_path=".\\chromedriver_win32\\chromedriver.exe")
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver=self.driver
        # entering the url of the application we are performing
        driver.get('https://magnus.jalatechnologies.com/')
        # login into the website by entering the login credentials
        login=loginPage(driver)
        login.enter_username("training@jalaacademy.com")
        login.enter_password("jobprogram")
        login.click_login()
        time.sleep(2)


    @classmethod
    def tearDownClass(cls) :
        #closing the browser after the login
        cls.driver.close()
        cls.driver.quit()
        print('Login test completed and employee id is created')

if __name__=='__main__':
    unittest.main



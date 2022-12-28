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

class searchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=".\\chromedriver_win32\\chromedriver.exe")
        cls.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        # entering the url of the application we are performing
        driver.get('https://magnus.jalatechnologies.com/')
        login = loginPage(driver)
        login.enter_username("training@jalaacademy.com")
        login.enter_password("jobprogram")
        login.click_login()
        time.sleep(2)

        # entering employee information to create an employee id
        employee = employeepage(driver)

        employee.click_employee()
        time.sleep(1)
        search = searchpage(driver)
        time.sleep(2)
        search.click_search()
        search.enter_name('Geetha')
        search.enter_mobilenum('7113267527')
        search.press_search()

    def tearDown(self):
        #closing the browser after the login
        self.driver.close()
        self.driver.quit()
        print('Login test completed and employee id is created')

if __name__ == '__main__':
        unittest.main


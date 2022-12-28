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

#/**
#*
#* @author JALA Academy
#*
#*
#*
#*
#*/

class employeeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #browser lunching and maximizing the window
        cls.driver=webdriver.Chrome(executable_path=".\\chromedriver_win32\\chromedriver.exe")
        cls.driver.maximize_window()


    def test_employee(self):
            driver = self.driver
            # entering the url of the application we are performing
            driver.get('https://magnus.jalatechnologies.com/')
            # login into the website by entering the login credentials
            login = loginPage(driver)
            login.enter_username("training@jalaacademy.com")
            login.enter_password("jobprogram")
            login.click_login()
            time.sleep(2)

            #entering employee information to create an employee id
            employee = employeepage(driver)

            employee.click_employee()
            time.sleep(1)
            employee.click_create()
            time.sleep(1)
            employee.enter_firstname("Geetha")
            employee.enter_lastname("Vemula")
            employee.enter_email('geetha@gmail.com')
            employee.enter_mobileno('7113267527')
            employee.enter_dob("2-9-2000")
            employee.click_gender()
            employee.enter_address('3-56/3,karimnager')
            employee.select_country('INDIA')
            employee.select_city('Hyderabad')
            employee.click_skill()
            employee.click_save()
            time.sleep(2)
    def tearDown(self) :
        #closing the browser after the login
        self.driver.close()
        self.driver.quit()
        print('Login test completed and employee id is created')

if __name__=='__main__':
    unittest.main

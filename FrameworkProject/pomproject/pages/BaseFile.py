import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
import time
import pytest

class BaseFile(unittest.TestCase):
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
        driver.find_element(By.ID,"UserName").send_keys("training@jalaacademy.com")
        driver.find_element(By.ID, "Password").send_keys("jobprogram")
        driver.find_element(By.ID,"btnLogin").click()

time.sleep(2)

@classmethod
def tearDownClass(cls) :
     #closing the browser after the login
     cls.driver.close()
     cls.driver.quit()
     print('Login test completed and employee id is created')

if __name__=='__main__':
    unittest.main



from selenium.webdriver.common.by import By
import pytest

#/**
#*
#* @author JALA Academy
#*
#*
#*
#*
#*/

class searchpage():
    def __init__(self,driver):
        self.driver=driver
        #selecting the search option
        self.search_tab_css_selector='#MenusDashboard > li.treeview.menu-open > ul > li:nth-child(2) > a'
        #searching employee detais by the name and mobile number
        self.name_textbox_id="Name"
        self.mobilenum_textbox_id="MobileNo"
        self.search_button_id="btnSearch"

    def click_search(self):
        self.driver.find_element(By.CSS_SELECTOR,self.search_tab_css_selector).click()

    def enter_name(self,name):
        self.driver.find_element(By.ID,self.name_textbox_id).send_keys(name)
    def enter_mobilenum(self,mobilenum):
        self.driver.find_element(By.ID,self.mobilenum_textbox_id).send_keys(mobilenum)
    def press_search(self):
        self.driver.find_element(By.ID,self.search_button_id).click()


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

class MorePage():

    def __init__(self,driver):
        self.driver=driver
        #select more
        self.more_tab_css_selector='#MenusDashboard > li:nth-child(3) > a'
        #select multiple tabs option
        self.multiple_tabs_css_selector='#MenusDashboard > li.treeview.menu-open > ul > li:nth-child(1) > a'
        #select plan to succeed or any one
        self.plantosucceed_tab_xpath='//*[@id="frmTabs"]/div/div/div/div/ul/li[1]/a'
        #entering the credentials in the mentioned field
        self.textbox1_id="textbox1"
        self.textbox2_id="textbox2"
        #select popup to work on popups
        self.popup_button_xpath="//a[normalize-space()='Popups']"
        self.popup1_button_xpath="//a[@id='btn-one']"
        self.popup2_button_xpath ="//a[@id='btn-two']"
        self.popup3_button_xpath ="//a[@id='btn-three']"

    def select_more(self):
        self.driver.find_element(By.CSS_SELECTOR,self.more_tab_css_selector).click()

    def select_multipletabs(self):
        self.driver.find_element(By.CSS_SELECTOR,self.multiple_tabs_css_selector).click()

    def select_plantosucceed(self):
        self.driver.find_element(By.XPATH,self.plantosucceed_tab_xpath).click()

    def enter_textbox1(self,comment):
        self.driver.find_element(By.ID,self.textbox1_id).send_keys(comment)

    def enter_textbox2(self,comment):
        self.driver.find_element(By.ID,self.textbox2_id).send_keys(comment)

    def select_popup(self):
        self.driver.find_element(By.XPATH, self.popup_button_xpath).click()

    def select_popup1(self):
        self.driver.find_element(By.XPATH, self.popup1_button_xpath).click()

    def select_popup2(self):
        self.driver.find_element(By.XPATH, self.popup2_button_xpath).click()

    def select_popup3(self):
        self.driver.find_element(By.XPATH,self.popup3_button_xpath).click()


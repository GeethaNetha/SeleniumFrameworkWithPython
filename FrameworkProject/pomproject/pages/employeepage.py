import pytest
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

class employeepage():
    def __init__(self,driver):
        self.driver=driver

        #selecting the employee page
        self.employee_tab_css_selector='#MenusDashboard > li:nth-child(2) > a'

        #selecting create option to entering the employee details
        self.create_tab_css_selector='#MenusDashboard > li.treeview.menu-open > ul > li:nth-child(1) > a'

        #enter the employee details
        self.firstname_textbox_id="FirstName"
        self.lastname_textbox_id="LastName"
        self.email_textbox_id = "EmailId"
        self.mobileno_textbox_id= "MobileNo"
        self.dob_textbox_id = "DOB"
        self.gender_radiobutton_id="rdbFemale"
        self.address_textbox_id = "Address"
        self.country_dropdown_id = "CountryId"
        self.city_dropdown_id = "CityId"
        self.skills_checkbox_id="chkSkill_1"
        self.save_button_xpath="//button[normalize-space()='Save']"

#selecting employee
    def click_employee(self):
        self.driver.find_element(By.CSS_SELECTOR,self.employee_tab_css_selector).click()
#selecting create option
    def click_create(self):
        self.driver.find_element(By.CSS_SELECTOR,self.create_tab_css_selector).click()

#filling the user credentials
    def enter_firstname(self,firstname):
        self.driver.find_element(By.ID, self.firstname_textbox_id).send_keys(firstname)
    def enter_lastname(self,lastname):
        self.driver.find_element(By.ID,self.lastname_textbox_id).send_keys(lastname)
    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_textbox_id).send_keys(email)
    def enter_mobileno(self,mobileno):
        self.driver.find_element(By.ID,self.mobileno_textbox_id).send_keys(mobileno)
    def enter_dob(self,dob):
        self.driver.find_element(By.ID, self.dob_textbox_id).send_keys(dob)
    def click_gender(self,):
        self.driver.find_element(By.ID,self.gender_radiobutton_id).click()
    def enter_address(self,address):
        self.driver.find_element(By.ID,self.address_textbox_id ).send_keys(address)
    def select_country(self,country):
        self.driver.find_element(By.ID,self.country_dropdown_id ).send_keys(country)
    def select_city(self,city):
        self.driver.find_element(By.ID,self.city_dropdown_id).send_keys(city)
    def click_skill(self):
        self.driver.find_element(By.ID,self.skills_checkbox_id).click()
    def click_save(self):
        self.driver.find_element(By.XPATH,self.save_button_xpath).click()
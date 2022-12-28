from selenium.webdriver.common.by import By

#/**
#*
#* @author JALA Academy
#*
#*
#*
#*
#*/

class loginPage():
    #creating a constructor and the constructor is __init__()
    def __init__(self,driver):
        self.driver=driver
        #created class for loginpage
        self.username_textbox_id ="UserName"
        self.password_textbox_id = "Password"
        self.login_button_id="btnLogin"

    def enter_username(self,username):
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.login_button_id).click()
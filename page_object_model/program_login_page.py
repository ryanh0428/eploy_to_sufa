from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test_data import temp_login_name, temp_login_pw
from time import sleep
from icecream import ic as print

class ProgramLoginPage():
    def __init__(self,driver:WebDriver,user_c) -> None:
        self.driver = driver
        self.login_tab_button = (By.ID, 'loginTab')
        self.registration_frame = (By.CLASS_NAME, 'fancybox-iframe')
        self.user_name = (By.ID, 'ctl00_ctl00_FormContent_LoginHolder_LoginBox2_ctl01_txtUsername')
        self.password = (By.ID, 'ctl00_ctl00_FormContent_LoginHolder_LoginBox2_ctl01_txtPassword')
        self.login_button = (By.ID, 'ctl00_ctl00_FormContent_LoginHolder_LoginBox2_ctl01_btnSubmit')
        
    def switch_to_register_iframe(self) -> None:
        sleep(1)
        register_iframe = WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(self.registration_frame))
        sleep(1)
        self.driver.switch_to.frame(register_iframe)
        
    def click_the_login_tab(self) -> None:
        self.driver.find_element(*self.login_tab_button).click()
        
    def give_username(self)-> None:
        user_name_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.user_name))
        user_name_field.send_keys(temp_login_name)
        
    def give_password(self) -> None:
        password_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.password))
        password_field.send_keys(temp_login_pw)
        
    def click_login_button(self) -> None:
        self.driver.find_element(*self.login_button).click()
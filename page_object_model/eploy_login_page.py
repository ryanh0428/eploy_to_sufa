from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import sys
import os
from time import sleep
# from test_data import login_password, login_name, eploy_url
# Add the parent directory of the current script to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test_data import login_password, login_name, eploy_url


class EployLoginPage():
    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.user_name_field = (By.ID, 'ctl00_main_ctl02_txtUsername')
        self.user_password_field = (By.ID, 'ctl00_main_ctl02_txtPassword')
        self.submit_button = (By.ID,'ctl00_main_ctl02_btnSubmit')
        
    def get_to_the_login_page(self):
        self.driver.get(eploy_url)
        self.driver.maximize_window()
    
    def provide_login_name(self):
        login_name_field = self.driver.find_element(*self.user_name_field)
        login_name_field.send_keys(login_name)

    def provide_login_password(self):
        login_password_field = self.driver.find_element(*self.user_password_field)
        login_password_field.send_keys(login_password)

    def click_submit_button(self):
        submit_button = self.driver.find_element(*self.submit_button)
        submit_button.click()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    eploy_login_page = EployLoginPage(driver)
    eploy_login_page.get_to_the_login_page()
    eploy_login_page.provide_login_name()
    eploy_login_page.provide_login_password()
    eploy_login_page.click_submit_button()
    sleep(5)




    
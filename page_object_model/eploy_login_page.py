import sys
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
# from test_data import login_password, login_name, eploy_url
# Add the parent directory of the current script to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test_data import login_password, login_name, eploy_url



class EployLoginPage():
    """
    A Page Object Model (POM) class representing the Eploy login page.

    This class provides locators for the login page elements and methods 
    to interact with them, allowing automation of the login process.

    Attributes:
        driver (WebDriver): The Selenium WebDriver instance controlling the browser.
        user_name_field (tuple): Locator for the username input field.
        user_password_field (tuple): Locator for the password input field.
        submit_button (tuple): Locator for the login submit button.
    """
    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.user_name_field = (By.ID, 'ctl00_main_ctl02_txtUsername')
        self.user_password_field = (By.ID, 'ctl00_main_ctl02_txtPassword')
        self.submit_button = (By.ID,'ctl00_main_ctl02_btnSubmit')
        
    def get_to_the_login_page(self):
        """
        Navigates to the Eploy login page and maximizes the browser window.

        This method directs the WebDriver instance to the specified Eploy login URL 
        and ensures the browser window is maximized for better visibility.

        Raises:
            WebDriverException: If the browser fails to load the URL.
        """
        self.driver.get(eploy_url)
        self.driver.maximize_window()
    
    def provide_login_name(self):
        """
        Enters the login username into the username input field.

        This method locates the username input field using its predefined locator 
        and inputs the login name imported from the test data file.

        Raises:
            NoSuchElementException: If the username field is not found in the DOM.
            ElementNotInteractableException: If the username field is present but not interactable.
        """
        login_name_field = self.driver.find_element(*self.user_name_field)
        login_name_field.send_keys(login_name)

    def provide_login_password(self):
        """
        Enters the login password into the password input field.

        This method locates the password field using its predefined locator 
        and inputs the password imported from the test data file.

        Raises:
            NoSuchElementException: If the password field is not found in the DOM.
            ElementNotInteractableException: If the password field is present but not interactable.
        """
        login_password_field = self.driver.find_element(*self.user_password_field)
        login_password_field.send_keys(login_password)

    def click_submit_button(self):
        """
        Clicks the submit button on the Eploy login page.
        
        This method locates the submit button using its predefined locator and clicks it.
        
        Raises:
            NoSuchElementException: If the submit button cannot be found in the DOM.
            ElementNotInteractableException: If the submit button is present but not clickable.
        """
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




    
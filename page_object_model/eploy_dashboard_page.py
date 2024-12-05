from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from eploy_login_page import EployLoginPage
# from test_data import login_password, login_name, eploy_url
# Add the parent directory of the current script to sys.path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test_data import login_password, login_name, eploy_url

from time import sleep
class EployDashboardPage():
    def __init__(self,driver:WebDriver, test_data:dict):
        self.driver = driver
        self.search_box = (By.ID, 'QuickSearchKeyword')
        self.vacancy = (By.PARTIAL_LINK_TEXT, 'Vacancies')
        self.hk_programe_link = (By.XPATH, "//a[contains(text(), 'Software')]")
        self.search_code = test_data.get('Vacancy ID')
        self.top_list = (By.CLASS_NAME,'c-quicksearch__top')
        self.search_iframe = (By.ID, 'SearchIframe')
        self.hong_kong_software_gp = (By.ID, '_yuiResizeMonitor')
        self.view_live = (By.ID, 'ViewLiveBtn')
        
        
                

    def search_for_vacancy_code(self):
        search_box_element = WebDriverWait(self.driver,15).until(EC.element_to_be_clickable((self.search_box)))
        search_box_element.send_keys(self.search_code)
        search_box_element.send_keys(Keys.RETURN)

    def click_on_vancancies_tab(self):
        # top_list = WebDriverWait(self.driver,15).until(EC.presence_of_element_located((self.top_list)))
        # vancancies_tab = WebDriverWait(top_list,10).until(EC.visibility_of_element_located((self.vacancy)))
        # vancancies_tab.click()
        # Check if the element is in the DOM
        element_exists = self.driver.execute_script("return document.getElementById('toplist') != null;")
        if element_exists:
            print("toplist is in the DOM.")
        else:
            print("toplist is not in the DOM yet.")
        element_exists = self.driver.execute_script("return document.getElementById('SearchIframe') != null;")
        if element_exists:
            print("SearchIframe is in the DOM.")
        else:
            print("SearchIframe is not in the DOM yet.")
        table = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.search_iframe))
        self.driver.switch_to.frame(table)
        top_list = WebDriverWait(self.driver,15).until(EC.presence_of_element_located((self.top_list)))
        vancancies_tab = WebDriverWait(top_list,10).until(EC.visibility_of_element_located((self.vacancy)))
        vancancies_tab.click()
        hong_kong_link = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.hk_programe_link)))
        hong_kong_link.click()
        # element_exists = self.driver.execute_script("return document.getElementById('statusbar') != null;")
        # if element_exists:
        #     print("statusbar is in the DOM.")
        # else:
        #     print("statusbar is not in the DOM yet.")
            
        # element_exists = self.driver.execute_script("return document.getElementById('ViewLiveBtn') != null;")
        # if element_exists:
        #     print("ViewLiveBtn is in the DOM.")
        # else:
        #     print("ViewLiveBtn is not in the DOM yet.")
        view_live_button = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.view_live)))
        view_live_button.click()
        sleep(10)
        
        
        
        
        
        

    
        
if __name__ == '__main__':
    driver = webdriver.Chrome()
    eploy_login_page = EployLoginPage(driver)
    eploy_login_page.get_to_the_login_page()
    eploy_login_page.provide_login_name()
    eploy_login_page.provide_login_password()
    eploy_login_page.click_submit_button()
    eploy_dashboard_page = EployDashboardPage(driver,{'Vacancy ID':'497'})
    eploy_dashboard_page.search_for_vacancy_code()
    eploy_dashboard_page.click_on_vancancies_tab()
    sleep(5)

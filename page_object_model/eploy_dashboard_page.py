from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
from time import sleep
class EployDashboardPage():
    def __init__(self,driver:WebDriver, test_data:dict):
        self.driver = driver
        self.search_box = (By.ID, 'QuickSearchKeyword')
        self.vacancy = (By.LINK_TEXT, 'Vacancies')
        self.hk_programe_link = (By.XPATH, "//a[contains(text(), 'Software')]")
        self.search_code = test_data.get('Vacancy ID')

    def search_for_vacancy_code(self):
        search_box_element = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((self.search_box)))
        search_box_element.send_keys(self.search_code)
        search_box_element.send_keys(Keys.RETURN)

    def 

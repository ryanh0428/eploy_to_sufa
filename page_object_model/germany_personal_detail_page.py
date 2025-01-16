from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test_data import login_password
from time import sleep

class GermanyPersonalDetailPage(): #may use inheritance for other region??
    def __init__(self,driver:WebDriver, test_data:dict):
        self.driver = driver
        self.title_box = (By.XPATH, '//label[contains(text(),"Title")]/')
        
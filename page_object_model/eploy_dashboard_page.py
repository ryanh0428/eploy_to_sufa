from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from icecream import ic as print
from selenium.webdriver.common.action_chains import ActionChains
# from test_data import login_password, login_name, eploy_url
# Add the parent directory of the current script to sys.path
import sys
import os
from time import sleep

class EployDashboardPage():
    """
    A Page Object Model (POM) class representing the Eploy Dashboard page for automated testing.

    This class encapsulates the interactions and elements on the Eploy Dashboard page, such as searching
    for a vacancy code, navigating to the vacancies tab, and interacting with specific program links.

    Attributes:
        driver (WebDriver): The Selenium WebDriver instance used to interact with the web page.
        search_box (tuple): Locator for the search box element on the dashboard page.
        vacancy (tuple): Locator for the "Vacancies" tab link.
        hk_programe_link (tuple): Locator for the "Software" program link (Hong Kong specific).
        search_code (str): The vacancy ID used for searching vacancies, retrieved from test data.
        top_list (tuple): Locator for the top search result container.
        search_iframe (tuple): Locator for the search iframe.
        hong_kong_software_gp (tuple): Locator for the Hong Kong software group element.
        view_live (tuple): Locator for the "View Live" button.

    Methods:
        search_for_vacancy_code():
            Searches for a vacancy using the provided vacancy code from test data.

        click_on_vancancies_tab():
            Navigates to the vacancies tab, clicks on a specific program link, and interacts with the
            "View Live" button.

    Example Usage:
        driver = webdriver.Chrome()
        test_data = {"Vacancy ID": "12345"}
        dashboard_page = EployDashboardPage(driver, test_data)

        # Search for a vacancy code
        dashboard_page.search_for_vacancy_code()

        # Click on the vacancies tab and interact with program links
        dashboard_page.click_on_vancancies_tab()
    """
    def __init__(self,driver:WebDriver, test_data:dict):
        self.driver = driver
        self.search_box = (By.ID, 'QuickSearchKeyword')
        self.vacancy = (By.PARTIAL_LINK_TEXT, 'Vacancies')
        self.first_programe_link = (By.XPATH, "//tr[contains(@class, 'datamenutablefirstrow')]/td[2]")
        self.avatar_initial = test_data.get('Initial')
        self.search_code = test_data.get('Vacancy ID')
        self.recruiter_role = test_data.get('Role')
        self.top_list = (By.CLASS_NAME,'c-quicksearch__top')
        self.search_iframe = (By.ID, 'SearchIframe')
        self.hong_kong_software_gp = (By.ID, '_yuiResizeMonitor')
        self.view_live = (By.ID, 'ViewLiveBtn')
        self.avatar_div = (By.XPATH, '//form/div[4]') #//*[@id="aspnetForm"]/div[4]
        self.switch_role_button = (By.XPATH, '//span[text()="Switch Role"]')
        self.roles_list = (By.XPATH, '//*[@id="ctl00_AdminTopBar1_dropDownAnchor_menu"]')
        
        
        
                

    def search_for_vacancy_code(self) -> None:
        """
        Searches for a vacancy using the provided vacancy code.

        This method waits for the search box element to become clickable, inputs the vacancy code
        provided in the `test_data` dictionary during class initialization, and triggers the search
        by simulating a Return key press.

        Args:
            None

        Returns:
            None

        Raises:
            TimeoutException: If the search box does not become clickable within the timeout period.

        Example:
            dashboard_page.search_for_vacancy_code()
        """
        sleep(1)
        search_box_element = WebDriverWait(self.driver,15).until(EC.element_to_be_clickable((self.search_box)))
        search_box_element.send_keys(self.search_code)
        search_box_element.send_keys(Keys.RETURN)

    def click_on_vancancies_tab(self):
        """
        Navigates to the vacancies tab, interacts with the Hong Kong program link, 
        and clicks the "View Live" button.

        This method performs the following actions:
        1. Waits for the search iframe to be visible and switches to it.
        2. Waits for the vacancies tab to be visible within the iframe and clicks it.
        3. Waits for the Hong Kong program link to be visible and clicks it.
        4. Executes JavaScript to interact with the page's DOM.
        5. Waits for the "View Live" button to appear and clicks it.

        Args:
            None

        Returns:
            None

        Raises:
            TimeoutException: If any of the elements do not become visible or clickable within the timeout period.

        Example:
            dashboard_page.click_on_vancancies_tab()
        """
        table = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.search_iframe))
        self.driver.switch_to.frame(table)
        top_list = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.top_list)))
        vancancies_tab = WebDriverWait(top_list,10).until(EC.visibility_of_element_located((self.vacancy)))
        vancancies_tab.click()
        first_link = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((self.first_programe_link)))
        first_link.click()
        self.driver.execute_script("return document.body.innerHTML;")
        view_live_button = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.view_live))
        view_live_button.click()
        
    def switch_role(self) -> None:
        avater_div = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.avatar_div))
        avater = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, f'.//div[text()="{self.avatar_initial}"]')))
        avater.click()
        switch_role_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.switch_role_button))
        switch_role_button.click()
        role_button_xpath = f'//span[text()="{self.recruiter_role}"]'
        target_role_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, role_button_xpath)))
        ActionChains(self.driver).scroll_to_element(target_role_button)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(target_role_button)).click()
        sleep(1)
        while True:
            if self.driver.execute_script("return document.readyState") == "complete":
                break
            sleep(1)

        

    
        
if __name__ == '__main__':
    from eploy_login_page import EployLoginPage
    driver = webdriver.Chrome()
    eploy_login_page = EployLoginPage(driver)
    eploy_login_page.get_to_the_login_page()
    eploy_login_page.provide_login_name()
    eploy_login_page.provide_login_password()
    eploy_login_page.click_submit_button()
    eploy_dashboard_page = EployDashboardPage(driver,{'Vacancy ID':'1121', 'Role': 'Germany - Recruiter','Initial':'RH'})
    eploy_dashboard_page.switch_role()
    eploy_dashboard_page.search_for_vacancy_code()
    eploy_dashboard_page.click_on_vancancies_tab()

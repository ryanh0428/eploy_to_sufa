from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from icecream import ic as print
from time import sleep


class ProgramApplyPage():
    def __init__(self,driver:WebDriver) -> None:
        self.driver = driver
        self.apply_button = (By.LINK_TEXT, 'Apply')
        self.id_apply_button = (By.ID, 'ctl00_ctl00_topContent_title_LnkApplySticky')
        self.accept_policy = (By.ID, 'epdsubmit')
        
    def switch_to_program_tab(self)-> None:
        original_tab = self.driver.current_window_handle
        windows = self.driver.window_handles
        new_tab = [handle for handle in windows if handle != original_tab][0]
        self.driver.switch_to.window(new_tab)
        
    def click_accept_policy(self) -> None:
        
            accept_button = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.accept_policy))
            sleep(3)
            accept_button.click()
            sleep(3)
            print(self.driver.execute_script("return document.readyState") == 'complete')
            # x = 0
            # while True:
            #     sleep(2)
            #     print(self.driver.execute_script("return document.readyState"))
            #     if self.driver.execute_script("return document.readyState") == 'complete':
            #         accept_button.click()
            #     x += 1
            #     if x == 10:
            #         break

            
        # WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.accept_policy)).click()
        # sleep(2)
        # while True:
        #     if self.driver.execute_script("return document.readyState") == "complete":
        #         break
        #     sleep(1)
        # WebDriverWait(self.driver,15).until(EC.invisibility_of_element_located(self.accept_policy))
        
    def click_apply_button(self) -> None:
        # self.driver.execute_script("return document.body.innerHTML;")
        apply_button = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.id_apply_button))
        apply_button.click()

        
if __name__ == '__main__':
    from eploy_login_page import EployLoginPage
    driver = webdriver.Chrome()
    eploy_login_page = EployLoginPage(driver)
    eploy_login_page.get_to_the_login_page()
    eploy_login_page.provide_login_name()
    eploy_login_page.provide_login_password()
    eploy_login_page.click_submit_button()
    from eploy_dashboard_page import EployDashboardPage
    eploy_dashboard_page = EployDashboardPage(driver,{'Vacancy ID':'1121', 'Role': 'Germany - Recruiter','Initial':'RH'})
    eploy_dashboard_page.switch_role()
    eploy_dashboard_page.search_for_vacancy_code()
    eploy_dashboard_page.click_on_vancancies_tab()
    program_apply_page = ProgramApplyPage(driver)
    program_apply_page.switch_to_program_tab()
    program_apply_page.click_accept_policy()
    program_apply_page.click_apply_button()
    sleep(5)
    
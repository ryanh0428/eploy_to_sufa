from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from icecream import ic
from time import sleep

class HkGraduateProgramApplyPage():
    def __init__(self,driver:WebDriver) -> None:
        self.driver = driver
        self.apply_button = (By.LINK_TEXT, 'Apply')
        self.id_apply_button = (By.ID, 'ctl00_ctl00_topContent_title_LnkApplySticky')
        self.accept_policy = (By.ID, 'epdsubmit')
        
    def switch_to_hk_graduate_program_tab(self)-> None:
        original_tab = self.driver.current_window_handle
        ic(original_tab)
        windows = self.driver.window_handles
        ic(windows)
        new_tab = [handle for handle in windows if handle != original_tab][0]
        ic(new_tab)
        self.driver.switch_to.window(new_tab)
        
    def click_accept_policy(self) -> None:
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.accept_policy)).click()
        
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
    eploy_dashboard_page = EployDashboardPage(driver,{'Vacancy ID':'497'})
    eploy_dashboard_page.search_for_vacancy_code()
    eploy_dashboard_page.click_on_vancancies_tab()
    hk_graduate_program_apply_page = HkGraduateProgramApplyPage(driver)
    hk_graduate_program_apply_page.switch_to_hk_graduate_program_tab()
    hk_graduate_program_apply_page.click_accept_policy()
    hk_graduate_program_apply_page.click_apply_button()
    sleep(5)
    
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# Add the parent directory of the current script to sys.path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class ClickNextPage():
    def __init__(self,driver:WebDriver)->None:
        self.driver = driver
        self.next_button = (By.XPATH, './/input[@value = "Next"]')
        self.actions = ActionChains(driver)
        
    def click_next_button(self)->None:
        next_button = self.driver.find_element(*self.next_button)
        self.actions.scroll_to_element(next_button)
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(next_button)).click()
        

if __name__ == '__main__':
    from eploy_login_page import EployLoginPage
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
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
    from page_object_model.program_apply_page import ProgramApplyPage
    hk_graduate_program_apply_page = ProgramApplyPage(driver)
    hk_graduate_program_apply_page.switch_to_program_tab()
    hk_graduate_program_apply_page.click_accept_policy()
    hk_graduate_program_apply_page.click_apply_button()
    from page_object_model.program_login_page import ProgramLoginPage
    program_login_page = ProgramLoginPage(driver)
    program_login_page.switch_to_register_iframe()
    program_login_page.click_the_login_tab()
    program_login_page.give_username()
    program_login_page.give_password()
    program_login_page.click_login_button()
    from page_object_model.germany_personal_detail_page import GermanyPersonalDetailPage
    germany_personal_detail_page = GermanyPersonalDetailPage(driver,{'Title': 'Mr', 'Country': 'Germany', 'First name': 'F_Name_De_4','Last Name':'L_Name_De_4', 'Mobile Number' : '123455667','Address Line 1': 'Test Line 1','Address Line 2' : 'Test Line 2', 'City': 'Frankfurt', 'Postcode':'56789'})
    germany_personal_detail_page.click_submit_if_presented()
    germany_personal_detail_page.select_title()
    germany_personal_detail_page.pick_country()
    germany_personal_detail_page.pick_have_permit()
    germany_personal_detail_page.fill_in_text_fields()
    germany_personal_detail_page.pick_hear_about_option()
    germany_personal_detail_page.click_next_button()
    click_next_page = ClickNextPage(driver)
    click_next_page.click_next_button()
    
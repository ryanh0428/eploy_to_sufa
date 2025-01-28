from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test_data import cv_path
from time import sleep

class GermanyUploadCvPage():
    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.pick_option = (By.XPATH, './/label[contains(text(),"hier deinen Lebenslauf")]/parent::div/following-sibling::div/select')
        self.upload_cv_button = (By.XPATH, './/button[text() = "Upload CV"]')
        self.upload_iframe = (By.XPATH, './/iframe[@title="Upload CV"]')
        self.file_box = (By.XPATH, './/input[@type="file"]')
        self.upload_file_button = (By.XPATH, './/input[@value = "Upload File"]')
        self.next_button = (By.XPATH, './/input[@value = "Next"]')
        
    def pick_upload_option(self):
        upload_option = Select(WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.pick_option)))
        upload_option.select_by_visible_text('Upload New')
        
    def click_upload_cv_button(self):
        upload_cv_button = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.upload_cv_button))
        upload_cv_button.click()
        
    def provide_upload_file_path(self):
        upload_iframe = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.upload_iframe))
        self.driver.switch_to.frame(upload_iframe)
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.file_box)).send_keys(cv_path)
        # upload_iframe.find_element(*self.file_box).send_keys(cv_path)
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.upload_file_button)).click()
        # upload_iframe.find_element(*self.upload_file_button).click()
        
    def click_the_next_button(self):
        self.driver.switch_to.default_content()
        self.driver.find_element(*self.next_button).click()
        
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
    # germany_personal_detail_page.click_accept_button()
    germany_personal_detail_page.select_title()
    germany_personal_detail_page.pick_country()
    germany_personal_detail_page.pick_have_permit()
    germany_personal_detail_page.fill_in_text_fields()
    germany_personal_detail_page.pick_hear_about_option()
    germany_personal_detail_page.click_next_button()
    from page_object_model.click_next_page import ClickNextPage
    click_next_page = ClickNextPage(driver)
    click_next_page.click_next_button()
    from page_object_model.germany_academic_background_page import GermanyAcademicBackgroundPage
    germany_academic_background_page = GermanyAcademicBackgroundPage(driver)
    germany_academic_background_page.click_the_academic_level()
    germany_academic_background_page.select_no_for_other_qualification()
    germany_academic_background_page.click_the_next_button()
    germany_upload_cv_page = GermanyUploadCvPage(driver)
    germany_upload_cv_page.pick_upload_option()
    germany_upload_cv_page.click_upload_cv_button()
    germany_upload_cv_page.provide_upload_file_path()
    germany_upload_cv_page.click_the_next_button()
    sleep(5)
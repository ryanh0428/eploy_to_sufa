from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class DeclarationPage():
    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.check_box = (By.XPATH, './/label[contains(normalize-space(),"and consent to receiving information from FDM Group in relation to this request")]/following-sibling::span/input')
        self.submit_button = (By.XPATH,'.//input[@type = "submit" and @value = "Submit"]')
        
        
    def click_check_box(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.check_box)).click()
        
    def click_submit_button(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.submit_button)).click()
        
    
        
if __name__ == '__main__':
    from page_object_model.eploy_login_page import EployLoginPage
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    eploy_login_page = EployLoginPage(driver)
    eploy_login_page.get_to_the_login_page()
    eploy_login_page.provide_login_name()
    eploy_login_page.provide_login_password()
    eploy_login_page.click_submit_button()
    from page_object_model.eploy_dashboard_page import EployDashboardPage
    eploy_dashboard_page = EployDashboardPage(driver,{'Vacancy ID':'1121', 'Role': 'Germany - Recruiter','Initial':'RH'})
    eploy_dashboard_page.switch_role()
    eploy_dashboard_page.search_for_vacancy_code()
    eploy_dashboard_page.click_on_vancancies_tab()
    from page_object_model.program_apply_page import ProgramApplyPage
    hk_graduate_program_apply_page = ProgramApplyPage(driver)
    hk_graduate_program_apply_page.switch_to_program_tab()
    hk_graduate_program_apply_page.click_accept_policy()
    hk_graduate_program_apply_page.click_apply_button()
    from page_object_model.first_register_page import FirstRegisterPage
    first_register_page = FirstRegisterPage(driver,{'First name': 'F_Name_De_12', 'Last Name':'L_Name_De_12','Email Address': 'Eploy.TestDe3101_De_12@fdmgroup.com','Currently Working':'NO','Country':'Germany'})
    first_register_page.switch_to_register_iframe()
    first_register_page.select_fdm_communication()
    first_register_page.select_which_one_box()
    first_register_page.provide_first_name()
    first_register_page.provide_last_name()
    first_register_page.provide_email_address()
    first_register_page.provide_confirmed_email_address()
    first_register_page.provide_password()
    first_register_page.select_location_of_work()
    first_register_page.answer_work_for_us()
    first_register_page.answer_previously_work_for_us()
    first_register_page.select_program_interested_in()
    first_register_page.answer_attending_university()
    first_register_page.select_university()
    first_register_page.select_graduation_month()
    first_register_page.select_graduation_year()
    first_register_page.provide_major()
    first_register_page.click_register_button()
    from page_object_model.germany_personal_detail_page import GermanyPersonalDetailPage
    germany_personal_detail_page = GermanyPersonalDetailPage(driver,{'Title': 'Mr', 'Country': 'Germany', 'First name': 'F_Name_De_12','Last Name':'L_Name_De_12', 'Mobile Number' : '123455667','Address Line 1': 'Test Line 1','Address Line 2' : 'Test Line 2', 'City': 'Frankfurt', 'Postcode':'56789'})
    germany_personal_detail_page.click_submit_if_presented()
    # germany_personal_detail_page.click_accept_button()
    germany_personal_detail_page.select_title()
    germany_personal_detail_page.pick_country()
    germany_personal_detail_page.pick_have_permit()
    germany_personal_detail_page.fill_in_text_fields()
    # germany_personal_detail_page.pick_hear_about_option()
    germany_personal_detail_page.click_next_button()
    from page_object_model.click_next_page import ClickNextPage
    click_next_page = ClickNextPage(driver)
    click_next_page.click_next_button()
    from page_object_model.germany_academic_background_page import GermanyAcademicBackgroundPage
    germany_academic_background_page = GermanyAcademicBackgroundPage(driver)
    germany_academic_background_page.click_the_academic_level()
    germany_academic_background_page.select_no_for_other_qualification()
    germany_academic_background_page.click_the_next_button()
    from page_object_model.germany_upload_cv_page import GermanyUploadCvPage
    germany_upload_cv_page = GermanyUploadCvPage(driver)
    germany_upload_cv_page.pick_upload_option()
    germany_upload_cv_page.click_upload_cv_button()
    germany_upload_cv_page.provide_upload_file_path()
    germany_upload_cv_page.click_the_next_button()
    declaration_page = DeclarationPage(driver)
    declaration_page.click_check_box()
    declaration_page.click_submit_button()
    sleep(20)
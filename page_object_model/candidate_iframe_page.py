from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# Add the parent directory of the current script to sys.path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.common_function import page_toggle
from time import sleep

class CandidateIframePage():
    def __init__(self, driver:WebDriver, test_data:dict):
        self.driver = driver
        self.candidate_iframe_locator = (By.XPATH, f'.//div[contains(@aria-label, "{test_data.get('First Name')}")]/div[@class = "fancybox-inner"]/div[@class = "fancybox-stage"]/div/div/iframe' )
        self.create_action_now_locator = (By.XPATH, './/input[@value = "Create Action Now"]')
        self.telephone_interview_button = (By.XPATH, './/a[contains(text(), "Telephone Interview")]')
        self.software_engineering_button = (By.XPATH, './/a[contains(text(), "Software Engineering")]')
        self.actions = ActionChains(self.driver)

    def switch_to_candidate_iframe(self):
        self.driver.switch_to.default_content()
        candidate_iframe = WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(self.candidate_iframe_locator))
        self.driver.switch_to.frame(candidate_iframe)

    def click_telephone_interview(self):
        telephone_interview_button = self.driver.find_element(*self.telephone_interview_button)
        self.actions.scroll_to_element(telephone_interview_button)
        telephone_interview_button.click()

    def click_create_action_now_button(self):
        create_action_now_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.create_action_now_locator))
        create_action_now_button.click()

    def click_step_software_engineering(self):
        software_engineering_button = self.driver.find_element(*self.software_engineering_button)
        self.actions.scroll_to_element(software_engineering_button)
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.software_engineering_button))
        software_engineering_button.click()


if __name__ == '__main__':
    from eploy_login_page import EployLoginPage
    service = Service(r'C:\Users\ryan_work\Documents\GitHub\eploy_to_sufa\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
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
    # eploy_dashboard_page.click_view_live()
    eploy_dashboard_page.click_work_on_vacancy()
    # # eploy_dashboard_page.click_on_vancancies_tab()

    # from page_object_model.program_apply_page import ProgramApplyPage
    # program_apply_page = ProgramApplyPage(driver)
    # program_apply_page.switch_to_program_tab()
    # program_apply_page.click_accept_policy()
    # program_apply_page.click_apply_button()
    # from page_object_model.first_register_page import FirstRegisterPage
    # first_register_page = FirstRegisterPage(driver,{'First name': 'F_Name_De_2_0702', 'Last Name':'L_Name_De_2_0702','Email Address': 'Eploy.TestDE_02_0702@fdmgroup.com','Currently Working':'NO','Country':'Germany'})
    # first_register_page.switch_to_register_iframe()
    # first_register_page.select_fdm_communication()
    # first_register_page.select_which_one_box()
    # first_register_page.provide_first_name()
    # first_register_page.provide_last_name()
    # first_register_page.provide_email_address()
    # first_register_page.provide_confirmed_email_address()
    # first_register_page.provide_password()
    # first_register_page.select_location_of_work()
    # first_register_page.answer_work_for_us()
    # first_register_page.answer_previously_work_for_us()
    # first_register_page.select_program_interested_in()
    # first_register_page.answer_attending_university()
    # first_register_page.select_university()
    # first_register_page.select_graduation_month()
    # first_register_page.select_graduation_year()
    # first_register_page.provide_major()
    # first_register_page.click_register_button()
    # sleep(5)
    # from page_object_model.germany_personal_detail_page import GermanyPersonalDetailPage
    # germany_personal_detail_page = GermanyPersonalDetailPage(driver,{'Title': 'Mr', 'Country': 'Germany', 'First name': 'F_Name_De_2_0702','Last Name':'L_Name_De_2_0702', 'Mobile Number' : '123455667','Address Line 1': 'Test Line 1','Address Line 2' : 'Test Line 2', 'City': 'Frankfurt', 'Postcode':'56789'})
    # germany_personal_detail_page.click_submit_if_presented()
    # # germany_personal_detail_page.click_accept_button()
    # germany_personal_detail_page.select_title()
    # germany_personal_detail_page.pick_country()
    # germany_personal_detail_page.pick_have_permit()
    # germany_personal_detail_page.fill_in_text_fields()
    # # germany_personal_detail_page.pick_hear_about_option()
    # germany_personal_detail_page.click_next_button()
    # sleep(5)
    # from page_object_model.click_next_page import ClickNextPage
    # click_next_page = ClickNextPage(driver)
    # click_next_page.click_next_button()
    # sleep(5)
    # from page_object_model.germany_academic_background_page import GermanyAcademicBackgroundPage
    # germany_academic_background_page = GermanyAcademicBackgroundPage(driver)
    # germany_academic_background_page.click_the_academic_level()
    # germany_academic_background_page.select_no_for_other_qualification()
    # germany_academic_background_page.click_the_next_button()
    # sleep(5)
    # from page_object_model.germany_upload_cv_page import GermanyUploadCvPage
    # germany_upload_cv_page = GermanyUploadCvPage(driver)
    # germany_upload_cv_page.pick_upload_option()
    # germany_upload_cv_page.click_upload_cv_button()
    # germany_upload_cv_page.provide_upload_file_path()
    # germany_upload_cv_page.click_the_next_button()
    # sleep(5)
    # from page_object_model.declaration_page import DeclarationPage
    # declaration_page = DeclarationPage(driver)
    # declaration_page.click_check_box()
    # declaration_page.click_submit_button()
    # sleep(5)
    # page_toggle(driver)
    # eploy_dashboard_page.click_work_on_vacancy()
    # eploy_dashboard_page.click_go_to_pipeline()
    # from page_object_model.pipeline_page import PipelinePage
    # pipeline_page = PipelinePage(driver, {'First Name': 'F_Name_De_2_0702'})
    # pipeline_page.click_the_name_on_the_candidate_card()
    


    eploy_dashboard_page.click_go_to_pipeline()
    # from pipeline_page import PipelinePage
    # pipeline_page = PipelinePage(driver, {'First Name': 'F_Name_De_2_0702'})
    # # pipeline_page.drag_candidate_card_to_telephone_interview_column()
    # pipeline_page.click_the_name_on_the_candidate_card()
    # candidate_iframe_page = CandidateIframePage(driver, {'First Name': 'F_Name_De_2_0702'})
    # candidate_iframe_page.switch_to_candidate_iframe()
    # candidate_iframe_page.click_telephone_interview()
    # candidate_iframe_page.click_create_action_now_button()
    # from create_action_iframe_page import CreateActionIframePage
    # create_action_iframe_page = CreateActionIframePage(driver)
    # create_action_iframe_page.switch_to_create_action_iframe()
    # create_action_iframe_page.set_outcome_to_passed()
    # create_action_iframe_page.click_save_button()
    # candidate_iframe_page.switch_to_candidate_iframe()
    # candidate_iframe_page.click_step_software_engineering()
    # candidate_iframe_page.click_create_action_now_button()
    # create_action_iframe_page.switch_to_create_action_iframe()
    # create_action_iframe_page.set_outcome_to_started()
    from pipeline_page import PipelinePage
    pipeline_page = PipelinePage(driver, {'First Name': 'F_Name_De_2_0702'})
    # pipeline_page.drag_candidate_card_to_telephone_interview_column()
    pipeline_page.click_the_name_on_the_candidate_card()
    candidate_iframe_page = CandidateIframePage(driver, {'First Name': 'F_Name_De_2_0702'})
    candidate_iframe_page.switch_to_candidate_iframe()
    candidate_iframe_page.click_step_software_engineering()
    candidate_iframe_page.click_create_action_now_button()
    from create_action_iframe_page import CreateActionIframePage
    create_action_iframe_page = CreateActionIframePage(driver)
    create_action_iframe_page.switch_to_create_action_iframe()
    create_action_iframe_page.set_outcome_to_started()

    sleep(10)

 


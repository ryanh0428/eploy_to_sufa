from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# from test_data import login_password, login_name, eploy_url
# Add the parent directory of the current script to sys.path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test_data import login_password
from time import sleep

class FirstRegisterPage():
    def __init__(self,driver:WebDriver,test_data:dict) -> None:
        self.driver = driver
        self.registration_frame = (By.CLASS_NAME, 'fancybox-iframe')
        self.hear_us_drop_down = (By.ID, 'ctl00_ctl00_FormContent_RegistrationHolder_ITSRegistrationControl_CanC_InfluenceToApply')
        self.which_one_box = (By.XPATH, '//div[@id = "div_CanC_InfluenceToApplyDetail"]//select')
        self.first_name_field = (By.ID, 'ctl00_ctl00_FormContent_RegistrationHolder_ITSRegistrationControl_CanC_FirstName')
        self.last_name_field = (By.ID,'ctl00_ctl00_FormContent_RegistrationHolder_ITSRegistrationControl_CanC_Surname')
        self.email_field = (By.ID, 'ctl00_ctl00_FormContent_RegistrationHolder_ITSRegistrationControl_CanC_Email')
        self.confirm_email_field = (By.ID, 'ctl00_ctl00_FormContent_RegistrationHolder_ITSRegistrationControl_Email_Copy1')
        self.password_div = (By.ID, 'div_CanC_Password')
        self.location_button = (By.XPATH, '//button/span[text() = "Select"]')
        self.location_HK = (By.XPATH, '//div[@title = "Hong Kong"]') #may get it from test_data, let see, first try hard code, if it is working, we get it dynmaically
        self.currently_working_div = (By.ID, 'div_CanC_IsEmployee')
        self.previously_working_div = (By.ID, 'div_CanC_IsPreviousEmployee')
        self.interested_stream_box = (By.CSS_SELECTOR, 'div#div_Question_9_271 Select')
        self.university_qualification_div = (By.ID, 'div_Question_3_782')
        self.university_select_div = (By.ID,'div_Question_9_762')
        self.university_search_box = (By.XPATH,'//input[@type = "text" and @placeholder = "Search..."]')
        self.major_box = ()
        self.register_button = (By.CSS_SELECTOR, 'input[value = "Register"]') #want to use XPATH/CSS looking for the word register value="Register"
        self.test_data = test_data
        self.actions = ActionChains(driver)
        
    def switch_to_register_iframe(self) -> None:
        sleep(1)
        register_iframe = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.registration_frame))
        sleep(1)
        self.driver.switch_to.frame(register_iframe)
        
    def select_fdm_communication(self) -> None:
        Select(self.driver.find_element(*self.hear_us_drop_down)).select_by_visible_text('Bootcamp')
        
    def select_which_one_box(self) -> None:
        if WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(self.which_one_box,'Please Select')):
            select_box = self.driver.find_element(*self.which_one_box)
            Select(select_box).select_by_visible_text('AppAcademy')


        
    def provide_first_name(self) -> None:
        first_name = self.test_data.get('First name')
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        
    def provide_last_name(self) -> None:
        last_name = self.test_data.get('Last Name')
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        
    def provide_email_address(self) -> None:
        email_address = self.test_data.get('Email Address')
        self.driver.find_element(*self.email_field).send_keys(email_address)
        
    def provide_confirmed_email_address(self) -> None:
        email_address = self.test_data.get('Email Address')
        self.driver.find_element(*self.confirm_email_field).send_keys(email_address)
        
    def provide_password(self) -> None:
        password_field = self.driver.find_element(*self.password_div).find_element(By.CSS_SELECTOR,'input[type = "password"]')
        password_field.send_keys(login_password)
        
    def select_location_of_work(self) -> None:
        
        location_button = self.driver.find_element(*self.location_button)
        self.actions.scroll_to_element(location_button)
        location_button.click()
        hong_kong_location = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.location_HK))
        self.actions.scroll_to_element(hong_kong_location)
        hong_kong_location.click()
        
    def answer_work_for_us(self) -> None:
        work_for_us = self.test_data.get('Currently Working')
        if work_for_us.lower() == 'yes':
            option_index = 0
        else:
            option_index = 1
        option_index = 0 if work_for_us.lower() == 'yes' else 1
        all_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.currently_working_div)).find_elements(By.CSS_SELECTOR, 'input')
        all_option[option_index].click()
        
    def answer_previously_work_for_us(self) -> None:
        all_option = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.previously_working_div)).find_elements(By.CSS_SELECTOR, 'input')
        all_option[1].click()
        
    def select_program_interested_in(self)->None:
        if WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element(self.interested_stream_box, 'Please Select')):
            program_box = self.driver.find_element(*self.interested_stream_box)
            Select(program_box).select_by_visible_text('Graduate Program/Careers Development Program')
            
    def answer_attending_university(self,option = 0)->None:
        uni_qualification_div = self.driver.find_element(*self.university_qualification_div)
        input_list = uni_qualification_div.find_elements(By.TAG_NAME,'input')
        input_list[option].click()
        
    def select_university(self) -> None:
        sleep(5)
        
        uni_select_div = self.driver.find_element(*self.university_select_div)
        self.actions.scroll_to_element(uni_select_div)
        search_button = WebDriverWait(uni_select_div,10).until(EC.element_to_be_clickable((By.TAG_NAME,'button')))
        #working on this line, why it is unclickable???
        search_button.click()
        search_box = WebDriverWait(uni_select_div,10).until(EC.presence_of_element_located(self.university_search_box))
        search_box.send_keys('Hong Kong Baptist University')
        bu_box = WebDriverWait(uni_select_div,10).until(EC.presence_of_all_elements_located((By.XPATH,'//span[text()="Hong Kong Baptist University"]')))
        bu_box.click()
        sleep(5)
        
        
        
        
    
        
        
    
        
        
        
        
        
        
    
        
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
    from hk_graduate_program_apply_page import HkGraduateProgramApplyPage
    hk_graduate_program_apply_page = HkGraduateProgramApplyPage(driver)
    hk_graduate_program_apply_page.switch_to_hk_graduate_program_tab()
    hk_graduate_program_apply_page.click_accept_policy()
    hk_graduate_program_apply_page.click_apply_button()
    first_register_page = FirstRegisterPage(driver,{'First name': 'F_Name_HK_4', 'Last Name':'L_Name_HK_4','Email Address': 'Eploy.TestHK03@fdmgroup.com','Currently Working':'NO'})
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
    
    
    

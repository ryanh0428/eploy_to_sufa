from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
# from test_data import login_password, login_name, eploy_url
# Add the parent directory of the current script to sys.path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test_data import login_password
from time import sleep
from icecream import ic as print

class FirstRegisterPage():
    def __init__(self,driver:WebDriver,test_data:dict) -> None:
        self.driver = driver
        self.registration_frame = (By.CLASS_NAME, 'fancybox-iframe')
        self.hear_us_drop_down = (By.ID, 'ctl00_ctl00_FormContent_RegistrationHolder_ITSRegistrationControl_CanC_InfluenceToApply')
        self.which_one_box = (By.XPATH, './/div[@id = "div_CanC_InfluenceToApplyDetail"]//select')
        self.first_name_field = (By.ID, 'ctl00_ctl00_FormContent_RegistrationHolder_ITSRegistrationControl_CanC_FirstName')
        self.last_name_field = (By.ID,'ctl00_ctl00_FormContent_RegistrationHolder_ITSRegistrationControl_CanC_Surname')
        self.email_field = (By.ID, 'ctl00_ctl00_FormContent_RegistrationHolder_ITSRegistrationControl_CanC_Email')
        self.confirm_email_field = (By.ID, 'ctl00_ctl00_FormContent_RegistrationHolder_ITSRegistrationControl_Email_Copy1')
        self.password_div = (By.ID, 'div_CanC_Password')
        self.location_button = (By.XPATH, './/label[contains(text(), "Which FDM Location")]/parent::*/following-sibling::div[1]/select')
        self.location_HK = (By.XPATH, './/div[@title = "Hong Kong"]') #may get it from test_data, let see, first try hard code, if it is working, we get it dynmaically
        self.currently_working_div = (By.ID, 'div_CanC_IsEmployee')
        self.previously_working_div = (By.ID, 'div_CanC_IsPreviousEmployee')
        self.interested_stream_box = (By.CSS_SELECTOR, 'div#div_Question_9_271 Select')
        self.university_qualification_div = (By.XPATH, './/legend[contains(normalize-space(), "Are you currently or have you")]/following-sibling::div[1]')
        self.university_select_div = (By.XPATH,'.//label[contains(text(), "Which university")]/parent::*/following-sibling::div[1]')
        self.general_search_box_locator = (By.XPATH,'.//input[@type = "text" and @placeholder = "Search..."]')
        self.major_box = ()
        self.register_button = (By.CSS_SELECTOR, 'input[value = "Register"]') #want to use XPATH/CSS looking for the word register value="Register"
        self.graduation_month_dropdown = (By.XPATH, './/label[contains(text(), "Graduation Month")]/ancestor::*[2]//select')
        self.graduation_year_div = (By.XPATH, './/label[contains(text(), "Graduation Year")]/ancestor::*[2]')
        self.academic_major = (By.XPATH, './/label[contains(text(), "degree/academic major")]/ancestor::*[2]//input')
        self.register_button = (By.XPATH, './/input[@value = "Register"]')
        self.test_data = test_data
        self.actions = ActionChains(driver)
        
    def switch_to_register_iframe(self) -> None:
        sleep(1)
        register_iframe = WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(self.registration_frame))
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
        self.actions.scroll_to_element(self.driver.find_element(*self.location_button))
        location_select_element = Select(WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.location_button)))
        location_select_element.select_by_visible_text('Hong Kong')
        
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
        self.actions.scroll_to_element(uni_qualification_div)
        input_list = uni_qualification_div.find_elements(By.TAG_NAME,'input')
        input_list[option].click()
        
    def select_university(self) -> None:
        uni_select_div = self.driver.find_element(*self.university_select_div)
        self.actions.scroll_to_element(uni_select_div)
        span_in_button = uni_select_div.find_element(By.XPATH, './/button/span[contains(text(),"Select")]')
        span_in_button.click()
        search_box = WebDriverWait(uni_select_div,10).until(EC.presence_of_element_located(self.general_search_box_locator))
        search_box.send_keys('Hong Kong Baptist University')
        bu_box = WebDriverWait(uni_select_div,10).until(EC.presence_of_element_located((By.XPATH,'.//span[text()="Hong Kong Baptist University"]')))
        bu_box.click()
        
    def select_graduation_month(self) -> None:
        graduation_month = self.driver.find_element(*self.graduation_month_dropdown)
        self.actions.scroll_to_element(graduation_month)
        graduation_month_select = Select(graduation_month)
        graduation_month_select.select_by_visible_text('March')
        
    def select_graduation_year(self) -> None:
        graduation_year = self.driver.find_element(*self.graduation_year_div)
        graduation_year_button = graduation_year.find_element(By.XPATH,'.//button/span[text()="Select"]')
        self.actions.scroll_to_element(graduation_year_button)
        graduation_year_button.click()
        search_box = graduation_year.find_element(By.XPATH, './/input[@type = "text" and @placeholder = "Search..."]')
        search_box.send_keys('2020')
        year_box = WebDriverWait(graduation_year, 10).until(EC.visibility_of_element_located((By.XPATH, './/li//span[text() = "2020"]')))
        year_box.click()
        
    def provide_major(self) -> None:
        major_text_box = self.driver.find_element(*self.academic_major)
        self.actions.scroll_to_element(major_text_box)
        major_text_box.send_keys('Test')
        
    def click_register_button(self) -> None:
        register_button = self.driver.find_element(*self.register_button)
        self.actions.scroll_to_element(register_button)
        register_button.click()
        sleep(15)
        
        
        
    
        
    
        
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
    from page_object_model.program_apply_page import HkGraduateProgramApplyPage
    hk_graduate_program_apply_page = HkGraduateProgramApplyPage(driver)
    hk_graduate_program_apply_page.switch_to_hk_graduate_program_tab()
    hk_graduate_program_apply_page.click_accept_policy()
    hk_graduate_program_apply_page.click_apply_button()
    first_register_page = FirstRegisterPage(driver,{'First name': 'F_Name_HK_4', 'Last Name':'L_Name_HK_4','Email Address': 'Eploy.TestHK1401@fdmgroup.com','Currently Working':'NO'})
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
    
    
    
    

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test_data import login_password
from time import sleep
from icecream import ic as print

class GermanyPersonalDetailPage(): #may use inheritance for other region??
    def __init__(self,driver:WebDriver, test_data:dict):
        self.driver = driver
        self.timezone_save_button = (By.XPATH, './/*[@value="Save"]')
        # self.timezone_save_button = (By.ID, 'ctl00_FlagSelector_ctl00_btnContinue')
        self.timezone_save_button_outside_div = (By.XPATH, './/*[@id="fancybox-container-1"]/div[2]/div[1]/div')
        self.title_box = (By.XPATH, './/label[contains(text(),"Title")]/parent::div/following-sibling::div[1]/select')
        self.country_box = (By.XPATH, './/label[contains(text(),"Country")]/parent::div/following-sibling::div[1]/select')
        self.hear_about = (By.XPATH, '//label[contains(text(), "hear about")]/parent::div/following-sibling::div[1]/select')
        self.title = test_data.get('Title')
        self.test_data = test_data
        self.work_permit_yes_button = (By.XPATH, './/label[text()="Yes"]/preceding-sibling::input[1]')
        self.next_button = (By.XPATH, './/input[@value = "Next"]')
        self.actions = ActionChains(driver)

    def click_submit_if_presented(self) -> None:
        sleep(5)
        self.driver.execute_script("return document.body.innerHTML;")
        save_button = self.driver.find_element(*self.timezone_save_button)
        save_button.click()


        
    def construct_input_field_tuple(self,question_key) -> tuple:
        return (By.XPATH, f'//label[contains(text(), "{question_key}")]/parent::div/following-sibling::div[1]/input')
    
    def select_title(self)->None:
        title_option = Select(WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.title_box)))
        title_option.select_by_visible_text(self.title)
        
    def input_text_field(self, field, value)->None:
        locator_tuple = self.construct_input_field_tuple(field)
        element = self.driver.find_element(*locator_tuple)
        self.actions.scroll_to_element(element)
        element.send_keys(value)
        
    def pick_country(self)->None:
        country = self.test_data.get('Country')
        country_drop_down = Select(self.driver.find_element(*self.country_box))
        self.actions.scroll_to_element(country_drop_down)
        country_drop_down.select_by_visible_text(country)
        
        
    def pick_have_permit(self)->None:
        yes_button = self.driver.find_element(*self.work_permit_yes_button)
        self.actions.scroll_to_element(yes_button)
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(yes_button)).click()
        
    def pick_hear_about_option(self)->None:
        hear_about_drop_down = Select(self.driver.find_element(*self.hear_about))
        self.actions.scroll_to_element(hear_about_drop_down)
        hear_about_drop_down.select_by_visible_text('FDM Newsletter')
        
    def click_next_button(self)->None:
        next_button = self.driver.find_element(*self.next_button)
        self.actions.scroll_to_element(next_button)
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(next_button)).click()
        
        
        
    def fill_in_text_fields(self):
        fields_required_list = ['First name', 'Last Name', 'Mobile Number','Address Line 1','Address Line 2', 'City', 'Postcode']
        for field in fields_required_list:
            value = self.test_data.get(field)
            print(field)
            print(value)
            if field == 'Mobile Number':
                self.input_text_field('Mobile',value)
            elif field == 'First name':
                self.input_text_field('First Name',value)
            elif field == 'Address Line 1':
                self.input_text_field('Address line 1',value)
            elif field == 'Address Line 2':
                self.input_text_field('Address line 2',value)
            elif field == 'Postcode':
                self.input_text_field('Postal Code',value)
            else:
                self.input_text_field(field,value)
                
                
        
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
    germany_personal_detail_page = GermanyPersonalDetailPage(driver,{'Title': 'Mr', 'Country': 'Germany', 'First name': 'F_Name_De_4','Last Name':'L_Name_De_4', 'Mobile Number' : '123455667','Address Line 1': 'Test Line 1','Address Line 2' : 'Test Line 2', 'City': 'Frankfurt', 'Postcode':'56789'})
    germany_personal_detail_page.click_submit_if_presented()
    germany_personal_detail_page.select_title()
    germany_personal_detail_page.pick_country()
    germany_personal_detail_page.pick_have_permit()
    germany_personal_detail_page.fill_in_text_fields()
    germany_personal_detail_page.pick_hear_about_option()
    germany_personal_detail_page.click_next_button()
    sleep(10)
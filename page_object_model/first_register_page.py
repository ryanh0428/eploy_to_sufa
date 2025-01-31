from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# from test_data import login_password, login_napythonme, eploy_url
# Add the parent directory of the current script to sys.path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test_data import login_password
from time import sleep
from icecream import ic as print

class FirstRegisterPage():
    """
    Represents the first registration page of the Eploy system.

    This class provides methods to interact with form elements required for user registration.
    """
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
        """
        Switches the WebDriver context to the registration iframe.

        This method:
        1. Waits for the registration iframe to become visible.
        2. Switches the WebDriver context to the iframe.

        Raises:
            TimeoutException: If the registration iframe does not appear within the timeout.
            NoSuchElementException: If the iframe is not found in the DOM.
            ElementNotInteractableException: If the iframe is present but not interactable.
        """
        sleep(1)
        register_iframe = WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(self.registration_frame))
        sleep(1)
        self.driver.switch_to.frame(register_iframe)
        
    def select_fdm_communication(self) -> None:
        """
        Selects 'Bootcamp' from the 'How did you hear about us?' dropdown.

        This action:
        1. Locates the dropdown element.
        2. Uses Selenium's Select class to choose 'Bootcamp' from the dropdown.

        Raises:
            NoSuchElementException: If the dropdown is not found in the DOM.
            ElementNotInteractableException: If the dropdown is present but not interactable.
            UnexpectedTagNameException: If the located element is not a <select> element.
        """
        Select(self.driver.find_element(*self.hear_us_drop_down)).select_by_visible_text('Bootcamp')
        
    def select_which_one_box(self) -> None:
        """
        Selects 'AppAcademy' from a dropdown menu when 'Please Select' is displayed.

        This method:
        1. Waits until the dropdown contains 'Please Select'.
        2. Locates the dropdown element.
        3. Uses Selenium's Select class to choose 'AppAcademy' from the dropdown.

        Raises:
            TimeoutException: If 'Please Select' does not appear within the timeout.
            NoSuchElementException: If the dropdown is not found in the DOM.
            ElementNotInteractableException: If the dropdown is present but not interactable.
            UnexpectedTagNameException: If the located element is not a <select> element.
        """
        if WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(self.which_one_box,'Please Select')):
            select_box = self.driver.find_element(*self.which_one_box)
            Select(select_box).select_by_visible_text('AppAcademy')


        
    def provide_first_name(self) -> None:
        """
        Enters the first name into the first name input field.

        This method:
        1. Retrieves the 'First name' from `test_data`.
        2. Locates the first name input field.
        3. Enters the retrieved first name into the field.

        Raises:
            NoSuchElementException: If the first name input field is not found.
            ElementNotInteractableException: If the input field is present but not interactable.
            KeyError: If 'First name' is missing from `test_data`.
        """
        first_name = self.test_data.get('First name')
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        
    def provide_last_name(self) -> None:
        """
        Enters the last name into the last name input field.

        This method:
        1. Retrieves the 'Last Name' from `test_data`.
        2. Locates the last name input field.
        3. Enters the retrieved last name into the field.

        Raises:
            NoSuchElementException: If the last name input field is not found.
            ElementNotInteractableException: If the input field is present but not interactable.
            KeyError: If 'Last Name' is missing from `test_data`.
        """
        last_name = self.test_data.get('Last Name')
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        
    def provide_email_address(self) -> None:
        """
        Enters the email address into the email input field.

        This method:
        1. Retrieves the 'Email Address' from `test_data`.
        2. Locates the email input field.
        3. Enters the retrieved email address into the field.

        Raises:
            NoSuchElementException: If the email input field is not found.
            ElementNotInteractableException: If the input field is present but not interactable.
            KeyError: If 'Email Address' is missing from `test_data`.
        """
        email_address = self.test_data.get('Email Address')
        self.driver.find_element(*self.email_field).send_keys(email_address)
        
    def provide_confirmed_email_address(self) -> None:
        """
        Enters the confirmed email address into the email confirmation input field.

        This method:
        1. Retrieves the 'Email Address' from `test_data`.
        2. Locates the email confirmation input field.
        3. Enters the retrieved email address into the field.

        Raises:
            NoSuchElementException: If the email confirmation input field is not found.
            ElementNotInteractableException: If the input field is present but not interactable.
            KeyError: If 'Email Address' is missing from `test_data`.
        """
        email_address = self.test_data.get('Email Address')
        self.driver.find_element(*self.confirm_email_field).send_keys(email_address)
        
    def provide_password(self) -> None:
        """
        Enters the login password into the password input field.

        This method:
        1. Locates the password input field within the designated container.
        2. Enters the password retrieved from `login_password`.

        Raises:
            NoSuchElementException: If the password field or its parent container is not found.
            ElementNotInteractableException: If the password field is present but not interactable.
        """
        password_field = self.driver.find_element(*self.password_div).find_element(By.CSS_SELECTOR,'input[type = "password"]')
        password_field.send_keys(login_password)
        
    def select_location_of_work(self) -> None:
        """
        Selects 'Hong Kong' as the work location from a dropdown menu.

        This method:
        1. Scrolls to ensure the location dropdown is visible.
        2. Waits for the dropdown to become clickable.
        3. Uses Selenium's Select class to choose 'Hong Kong' from the dropdown.

        Raises:
            TimeoutException: If the location dropdown does not become clickable within the timeout.
            NoSuchElementException: If the location dropdown is not found in the DOM.
            ElementNotInteractableException: If the dropdown is present but not interactable.
            UnexpectedTagNameException: If the located element is not a <select> element.
        """
        country = self.test_data.get('Country')
        self.actions.scroll_to_element(self.driver.find_element(*self.location_button))
        location_select_element = Select(WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.location_button)))
        location_select_element.select_by_visible_text(country)
        
    def answer_work_for_us(self) -> None:
        """
        Selects the appropriate response for the 'Are you currently working for us?' question.

        This method:
        1. Retrieves the 'Currently Working' value from the test data.
        2. Determines the correct option index based on whether the value is 'Yes' or not.
        3. Waits until the selection section becomes clickable.
        4. Finds all input elements (radio buttons) within the section.
        5. Clicks the appropriate option.

        Raises:
            TimeoutException: If the currently working section does not become clickable within the timeout.
            NoSuchElementException: If the input elements are not found.
            ElementNotInteractableException: If the input element is present but not clickable.
            IndexError: If there are fewer than two options in the selection list.
            AttributeError: If 'Currently Working' is missing or not a string in test data.
        """
        work_for_us:str = self.test_data.get('Currently Working')
        option_index = 0 if 'yes' in work_for_us.lower() else 1
        all_option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.currently_working_div)).find_elements(By.CSS_SELECTOR, 'input')
        all_option[option_index].click()
        
    def answer_previously_work_for_us(self) -> None:
        """
        Selects the second option in the 'Have you previously worked for us?' question.

        This method:
        1. Waits until the previously working section becomes clickable.
        2. Finds all input elements (radio buttons or checkboxes) within the section.
        3. Clicks the second option (index 1).

        Raises:
            TimeoutException: If the previously working section does not become clickable within the timeout.
            NoSuchElementException: If the input elements are not found.
            ElementNotInteractableException: If the input element is present but not clickable.
            IndexError: If there are fewer than two options in the selection list.
        """
        all_option = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.previously_working_div)).find_elements(By.CSS_SELECTOR, 'input')
        all_option[1].click()
        
    def select_program_interested_in(self)->None:
        """
        Selects 'Graduate Program/Careers Development Program' from the program dropdown.

        This method:
        1. Waits until the dropdown contains the text 'Please Select'.
        2. Locates the program selection dropdown.
        3. Uses Selenium's Select class to choose 'Graduate Program/Careers Development Program'.

        Raises:
            TimeoutException: If 'Please Select' does not appear within the timeout period.
            NoSuchElementException: If the dropdown is not found in the DOM.
            ElementNotInteractableException: If the dropdown is present but not interactable.
            UnexpectedTagNameException: If the located element is not a <select> element.
        """
        if WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element(self.interested_stream_box, 'Please Select')):
            program_box = self.driver.find_element(*self.interested_stream_box)
            Select(program_box).select_by_visible_text('Graduate Program/Careers Development Program')
            
    def answer_attending_university(self,option = 0)->None:
        """
        Selects an answer for the 'Are you currently or have you ever attended university?' question.

        This method:
        1. Locates the university qualification section.
        2. Scrolls to ensure it is visible.
        3. Finds all input elements (radio buttons or checkboxes) within the section.
        4. Clicks the option specified by the `option` index.

        Args:
            option (int, optional): The index of the input element to select (default is 0).

        Raises:
            NoSuchElementException: If the university qualification section or input elements are not found.
            ElementNotInteractableException: If the input element is present but not clickable.
            IndexError: If the `option` index is out of range.
        """
        uni_qualification_div = self.driver.find_element(*self.university_qualification_div)
        self.actions.scroll_to_element(uni_qualification_div)
        input_list = uni_qualification_div.find_elements(By.TAG_NAME,'input')
        input_list[option].click()
        
    def select_university(self) -> None:
        """
        Selects 'Hong Kong Baptist University' from the university dropdown.

        This method:
        1. Locates the university selection dropdown.
        2. Scrolls to ensure the dropdown is visible.
        3. Clicks the 'Select' button to open the dropdown.
        4. Waits for the search box to appear and enters 'Hong Kong Baptist University'.
        5. Waits for the corresponding option to be available and selects it.

        Raises:
            NoSuchElementException: If any required element is not found in the DOM.
            ElementNotInteractableException: If an element is present but not interactable.
            TimeoutException: If the search box or university option does not appear within the timeout period.
        """
        uni_select_div = self.driver.find_element(*self.university_select_div)
        self.actions.scroll_to_element(uni_select_div)
        span_in_button = uni_select_div.find_element(By.XPATH, './/button/span[contains(text(),"Select")]')
        span_in_button.click()
        search_box = WebDriverWait(uni_select_div,10).until(EC.presence_of_element_located(self.general_search_box_locator))
        search_box.send_keys('Hong Kong Baptist University')
        bu_box = WebDriverWait(uni_select_div,10).until(EC.presence_of_element_located((By.XPATH,'.//span[contains(text(), "Hong Kong Baptist University")]')))
        bu_box.click()
        
    def select_graduation_month(self) -> None:
        """
        Selects 'March' as the graduation month from a dropdown menu.

        This method:
        1. Locates the graduation month dropdown element.
        2. Ensures the dropdown is visible by scrolling to it.
        3. Uses Selenium's Select class to choose 'March' from the dropdown.

        Raises:
            NoSuchElementException: If the dropdown is not found in the DOM.
            ElementNotInteractableException: If the dropdown is present but not interactable.
            UnexpectedTagNameException: If the located element is not a <select> element.
        """
        graduation_month = self.driver.find_element(*self.graduation_month_dropdown)
        self.actions.scroll_to_element(graduation_month)
        graduation_month_select = Select(graduation_month)
        graduation_month_select.select_by_visible_text('March')
        
    def select_graduation_year(self) -> None:
        """
        Selects the graduation year from a dropdown menu.

        This method:
        1. Locates the graduation year dropdown container.
        2. Clicks the 'Select' button to open the dropdown.
        3. Enters '2020' into the search box.
        4. Waits for the matching option ('2020') to become visible and selects it.

        Raises:
            NoSuchElementException: If any required element is not found in the DOM.
            ElementNotInteractableException: If an element is present but not interactable.
            TimeoutException: If the graduation year option does not become visible in time.
        """
        graduation_year = self.driver.find_element(*self.graduation_year_div)
        graduation_year_button = graduation_year.find_element(By.XPATH,'.//button/span[text()="Select"]')
        self.actions.scroll_to_element(graduation_year_button)
        graduation_year_button.click()
        search_box = graduation_year.find_element(By.XPATH, './/input[@type = "text" and @placeholder = "Search..."]')
        search_box.send_keys('2020')
        year_box = WebDriverWait(graduation_year, 10).until(EC.visibility_of_element_located((By.XPATH, './/li//span[text() = "2020"]')))
        year_box.click()
        
    def provide_major(self) -> None:
        """
        Enters a placeholder academic major into the major text box.

        This method locates the academic major input field, ensures it is visible by 
        scrolling to it, and enters the text 'Test'.

        Raises:
            NoSuchElementException: If the major text box is not found in the DOM.
            ElementNotInteractableException: If the text box is present but not interactable.
        """
        major_text_box = self.driver.find_element(*self.academic_major)
        self.actions.scroll_to_element(major_text_box)
        major_text_box.send_keys('Test')
        
    def click_register_button(self) -> None:
        """
        Scrolls to and clicks the 'Register' button on the first registration page.

        This method locates the register button, ensures it is visible by scrolling to it, 
        clicks the button, and then waits for 5 seconds to allow the page to load.

        Raises:
            NoSuchElementException: If the register button is not found in the DOM.
            ElementNotInteractableException: If the register button is present but not clickable.
        """
        register_button = self.driver.find_element(*self.register_button)
        self.actions.scroll_to_element(register_button)
        register_button.click()
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
    eploy_dashboard_page = EployDashboardPage(driver,{'Vacancy ID':'1121', 'Role': 'Germany - Recruiter','Initial':'RH'})
    eploy_dashboard_page.switch_role()
    eploy_dashboard_page.search_for_vacancy_code()
    eploy_dashboard_page.click_on_vancancies_tab()
    from page_object_model.program_apply_page import ProgramApplyPage
    hk_graduate_program_apply_page = ProgramApplyPage(driver)
    hk_graduate_program_apply_page.switch_to_program_tab()
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
    
    
    
    

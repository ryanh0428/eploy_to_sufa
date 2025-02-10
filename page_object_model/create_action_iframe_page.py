from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class CreateActionIframePage():
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.outcome_option = (By.XPATH, './/label[contains(text(), "Outcome")]/parent::div/following-sibling::div/select')
        self.salesforce_id_input = (By.XPATH, './/label[contains(text(), "Salesforce ID:")]/parent::div/following-sibling::div/input')
        self.save_button = (By.XPATH, './/input[@value = "Save"]')
        self.create_action_iframe = (By.XPATH, ".//iframe")
        self.actions = ActionChains(self.driver)

    def switch_to_create_action_iframe(self):
        sleep(1)
        # create_action_iframe = WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(self.create_action_iframe))
        self.driver.switch_to.default_content()
        all_iframes = self.driver.find_elements(By.TAG_NAME,'iframe')
        for iframe in all_iframes:
            self.driver.switch_to.frame(iframe)
            try:
                self.driver.find_element(By.XPATH, './/h1[contains(text(),"Create Action")]')
                break
            except NoSuchElementException:
                self.driver.switch_to.default_content()
                continue
        # create_action_iframe_ele = WebDriverWait(self.driver,10).until(EC.frame_to_be_available_and_switch_to_it(self.create_action_iframe))
        # create_action_iframe = WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(self.create_action_iframe))
        # self.driver.switch_to.frame(create_action_iframe_ele)

    def set_outcome_to_passed(self):
        outcome_option = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.outcome_option))
        Select(outcome_option).select_by_visible_text('Passed')

    def set_outcome_to_started(self):
        outcome_option = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.outcome_option))
        Select(outcome_option).select_by_visible_text('Passed')

    def provide_salesforce_id(self):
        salesforce_id = self.driver.find_element(*self.salesforce_id_input)
        self.actions.scroll_to_element(salesforce_id)
        salesforce_id.send_keys('Test Start Date/DO NOT BOOK')

    def click_save_button(self):
        save_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_button))
        save_button.click()




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
    eploy_dashboard_page.click_go_to_pipeline()
    from pipeline_page import PipelinePage
    pipeline_page = PipelinePage(driver, {'First Name': 'De_4F'})
    # pipeline_page.drag_candidate_card_to_telephone_interview_column()
    pipeline_page.click_the_name_on_the_candidate_card()
    from candidate_iframe_page import CandidateIframePage
    candidate_iframe_page = CandidateIframePage(driver, {'First Name': 'De_4F'})
    pipeline_page.switch_to_candidate_iframe()
    pipeline_page.click_telephone_interview()
    pipeline_page.click_create_action_now_button()
    create_action_iframe_page = CreateActionIframePage(driver)
    create_action_iframe_page.set_outcome_to_passed()
    create_action_iframe_page.click_save_button()
    sleep(10)

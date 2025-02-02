#experiment drag and drop done
#identify the key steps to push a candidate through the pipeline do it on monday
#use click button which may be more robust than drag and drop do it on monday
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class PipelinePage:
    def __init__(self, driver:WebDriver, test_data:dict):
        self.driver = driver
        self.candidate_card = (By.XPATH, f".//a[contains(text(), '{test_data.get('First Name')}')]/parent::h3/parent::div")
        self.telephone_interview_column = (By.XPATH, "//div[contains(@class, 'its-o-flexi__cell') and contains(@class, 'its-c-workflow__column') and contains(@class, 'stage-1') and contains(@class, 'ui-sortable')]")
        self.actions = ActionChains(self.driver)

    def drag_candidate_card_to_telephone_interview_column(self):
        candidate_card_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.candidate_card))
        self.actions.scroll_to_element(candidate_card_element)
        telephone_interview_column_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.telephone_interview_column))
        ActionChains(self.driver).drag_and_drop(candidate_card_element, telephone_interview_column_element).perform()


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
    pipeline_page = PipelinePage(driver, {'First Name': 'De_4F'})
    pipeline_page.drag_candidate_card_to_telephone_interview_column()
    sleep(10)
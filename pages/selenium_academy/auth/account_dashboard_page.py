from urllib.parse import urljoin

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from config import Config, MadisonIslandEndpoints
from pages.base_page import BasePage


class AccountDashboardPage(BasePage):
    URL = urljoin(Config.MADISON_ISLAND_BASE_URL, MadisonIslandEndpoints.ACCOUNT_DASHBOARD_URL)

    REGISTRATION_MESSAGE_BOX = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div/ul/li/ul/li/span')
    HELLO_TEXT = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/p[1]/strong')
    EDIT_ADDRESS = (
        By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div/div[4]/div[2]/div[1]/div/div[1]/a'
    )

    COMPANY_INPUT = (By.ID, 'company')
    TELEPHONE_INPUT = (By.ID, 'telephone')
    FAX_INPUT = (By.ID, 'fax')
    STREET_ADDRESS_INPUT = (By.ID, 'street_1')
    STREET_ADDRESS_2_INPUT = (By.ID, 'street_2')
    CITY_INPUT = (By.ID, 'city')
    STATE_INPUT = (By.ID, 'region')
    ZIP_INPUT = (By.ID, 'zip')
    COUNTRY_SELECT = (By.ID, 'country')
    SAVE_ADDRESS_BUTTON = (By.CSS_SELECTOR, '.buttons-set > button:nth-child(2)')

    DEFAULT_ADDRESS = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/ol/li[1]/address')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    @property
    def registration_message_box(self):
        return self.browser.find_element(*AccountDashboardPage.REGISTRATION_MESSAGE_BOX)

    @property
    def hello_text(self):
        return self.browser.find_element(*AccountDashboardPage.HELLO_TEXT).text

    @property
    def edit_address(self):
        return self.browser.find_element(*AccountDashboardPage.EDIT_ADDRESS)

    @property
    def company_input(self):
        return self.browser.find_element(*AccountDashboardPage.COMPANY_INPUT)
    
    @property
    def telephone_input(self):
        return self.browser.find_element(*AccountDashboardPage.TELEPHONE_INPUT)

    @property
    def fax_input(self):
        return self.browser.find_element(*AccountDashboardPage.FAX_INPUT)

    @property
    def street_address_1_input(self):
        return self.browser.find_element(*AccountDashboardPage.STREET_ADDRESS_INPUT)
    
    @property
    def street_address_2_input(self):
        return self.browser.find_element(*AccountDashboardPage.STREET_ADDRESS_2_INPUT)
    
    @property
    def city_input(self):
        return self.browser.find_element(*AccountDashboardPage.CITY_INPUT)

    @property
    def state_input(self):
        return self.browser.find_element(*AccountDashboardPage.STATE_INPUT)
    
    @property
    def zip_input(self):
        return self.browser.find_element(*AccountDashboardPage.ZIP_INPUT)
    
    @property
    def country_select(self):
        return self.browser.find_element(*AccountDashboardPage.COUNTRY_SELECT)

    @property
    def save_address_button(self):
        return self.browser.find_element(*AccountDashboardPage.SAVE_ADDRESS_BUTTON)

    @property
    def default_address(self):
        return self.browser.find_element(*AccountDashboardPage.DEFAULT_ADDRESS)

    def _input_name_to_element(self, input_name):
        return {
            'company': self.company_input,
            'telephone': self.telephone_input,
            'fax': self.fax_input,
            'street_address': self.street_address_1_input,
            'street_address_2': self.street_address_2_input,
            'city': self.city_input,
            'state': self.state_input,
            'zip': self.zip_input,
            'country': self.country_select,
        }[input_name]

    def edit_address_book(self, input_data: dict):
        self.edit_address.click()

        for input_name, input_value in input_data.items():
            if input_name == 'country':
                select = Select(
                    WebDriverWait(self.browser, Config.DEFAULT_TIMEOUT * 2)
                    .until(
                        expected_conditions.element_to_be_clickable(AccountDashboardPage.COUNTRY_SELECT)
                    )
                )
                select.select_by_visible_text(input_value)
            else:
                self._input_name_to_element(input_name).clear()
                self._input_name_to_element(input_name).send_keys(input_value)

        self.save_address_button.click()

    def get_default_address(self):
        return self.default_address.text

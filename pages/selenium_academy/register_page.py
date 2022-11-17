from urllib.parse import urljoin

from selenium.webdriver.common.by import By

from config import (
    Config,
    MadisonIslandEndpoints,
)
from pages.base_page import BasePage


class RegisterPage(BasePage):
    URL = urljoin(Config.MADISON_ISLAND_BASE_URL, MadisonIslandEndpoints.REGISTER_URL)

    FIRST_NAME_INPUT = (By.XPATH, '//*[@id="firstname"]')
    MIDDLE_NAME_INPUT = (By.XPATH, '//*[@id="middlename"]')
    LAST_NAME_INPUT = (By.XPATH, '//*[@id="lastname"]')
    EMAIL_ADDRESS_INPUT = (By.XPATH, '//*[@id="email_address"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]')
    CONFIRM_PASSWORD_INPUT = (By.XPATH, '//*[@id="confirmation"]')
    NEWSLETTER_CHECKBOX = (By.XPATH, '//*[@id="is_subscribed"]')
    REGISTER_BUTTON = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button')

    def __init__(self, browser):
        super().__init__(browser)
        self.open()

    def open(self):
        self.browser.get(RegisterPage.URL)

    @property
    def first_name_input(self):
        return self.browser.find_element(*RegisterPage.FIRST_NAME_INPUT)

    @property
    def middle_name_input(self):
        return self.browser.find_element(*RegisterPage.MIDDLE_NAME_INPUT)

    @property
    def last_name_input(self):
        return self.browser.find_element(*RegisterPage.LAST_NAME_INPUT)

    @property
    def email_address_input(self):
        return self.browser.find_element(*RegisterPage.EMAIL_ADDRESS_INPUT)
    
    @property
    def password_input(self):
        return self.browser.find_element(*RegisterPage.PASSWORD_INPUT)
    
    @property
    def confirm_password_input(self):
        return self.browser.find_element(*RegisterPage.CONFIRM_PASSWORD_INPUT)
    
    @property
    def sign_up_for_newsletter_checkbox(self):
        return self.browser.find_element(*RegisterPage.NEWSLETTER_CHECKBOX)

    @property
    def register_button(self):
        return self.browser.find_element(*RegisterPage.REGISTER_BUTTON)

    def _input_name_to_element(self, input_name):
        return {
            'first_name': self.first_name_input,
            'last_name': self.last_name_input,
            'middle_name': self.middle_name_input,
            'email': self.email_address_input,
            'password': self.password_input,
            'confirm_password': self.confirm_password_input,
        }[input_name]

    def register(self, input_data: dict, sign_up_for_news: bool = False):
        for input_name, input_value in input_data.items():
            self._input_name_to_element(input_name).send_keys(input_value)

        if sign_up_for_news:
            self.sign_up_for_newsletter_checkbox.click()

        self.register_button.click()

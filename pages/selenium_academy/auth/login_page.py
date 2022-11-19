from urllib.parse import urljoin

from selenium.webdriver.common.by import By

from config import Config, MadisonIslandEndpoints
from pages.base_page import BasePage
from pages.selenium_academy.auth import AccountDashboardPage


class LoginPage(BasePage):
    URL = urljoin(Config.MADISON_ISLAND_BASE_URL, MadisonIslandEndpoints.LOGIN_URL)

    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'pass')
    SUBMIT_BUTTON = (By.ID, 'send2')

    REGISTRATION_MESSAGE_BOX = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div/ul/li/ul/li/span')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.open()

    def open(self):
        self.browser.get(LoginPage.URL)
        self.wait_for_presence_of_all_elements_located(LoginPage.EMAIL_INPUT)
        self.wait_for_presence_of_all_elements_located(LoginPage.PASSWORD_INPUT)

    @property
    def email_input(self):
        return self.browser.find_element(*LoginPage.EMAIL_INPUT)

    @property
    def password_input(self):
        return self.browser.find_element(*LoginPage.PASSWORD_INPUT)

    @property
    def submit_button(self):
        return self.browser.find_element(*LoginPage.SUBMIT_BUTTON)

    def login(self, email: str, password: str) -> AccountDashboardPage:
        self.email_input.send_keys(email)
        self.password_input.send_keys(password)

        self.click_button_or_press_enter_on_input(
            input=self.password_input,
            button=self.submit_button,
            enter=False
        )

        return AccountDashboardPage(browser=self.browser)

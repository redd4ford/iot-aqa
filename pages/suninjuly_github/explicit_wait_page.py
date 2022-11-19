from urllib.parse import urljoin

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from config import Config, SunInJulyGithubEndpoints
from pages.base_page import BasePage


class ExplicitWaitPage(BasePage):
    URL = urljoin(Config.SUN_IN_JULY_BASE_URL, SunInJulyGithubEndpoints.EXPLICIT_WAIT_URL)

    PRICE_ELEMENT = (By.ID, 'price')
    BOOK_BUTTON = (By.CSS_SELECTOR, '#book')
    X_VALUE = (By.ID, 'input_value')
    RESULT_INPUT = (By.ID, 'answer')
    SUBMIT_BUTTON = (By.ID, 'solve')

    def __init__(self, browser):
        super().__init__(browser)
        self.open()

    def open(self):
        self.browser.get(ExplicitWaitPage.URL)
        
    @property
    def price(self):
        return self.browser.find_element(*ExplicitWaitPage.PRICE_ELEMENT)

    @property
    def book_button(self):
        return self.browser.find_element(*ExplicitWaitPage.BOOK_BUTTON)

    @property
    def result_input(self):
        return self.browser.find_element(*ExplicitWaitPage.RESULT_INPUT)

    @property
    def submit_button(self):
        return self.browser.find_element(*ExplicitWaitPage.SUBMIT_BUTTON)

    @property
    def x_value(self) -> int:
        return int(self.browser.find_element(*ExplicitWaitPage.X_VALUE).text)

    def wait_until_price_is_100(self):
        return WebDriverWait(self.browser, Config.DEFAULT_TIMEOUT * 12).until(
            expected_conditions.text_to_be_present_in_element(
                self.PRICE_ELEMENT,
                '$100'
            )
        )

    def book(self):
        self.book_button.click()

    def answer(self, value: float, enter: bool = False):
        self.result_input.send_keys(value)

        self.click_button_or_press_enter_on_input(
            input=self.result_input,
            button=self.submit_button,
            enter=enter,
        )

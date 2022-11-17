from urllib.parse import urljoin

from selenium.webdriver.common.by import By

from config import (
    Config,
    SunInJulyGithubEndpoints,
)
from pages.base_page import BasePage


class RobotCaptchaPage(BasePage):
    URL = urljoin(Config.SUN_IN_JULY_BASE_URL, SunInJulyGithubEndpoints.ROBOT_CAPTCHA_URL)

    X_VALUE = (By.XPATH, '//*[@id="input_value"]')
    RESULT_INPUT = (By.ID, 'answer')
    ROBOT_CHECKBOX = (By.ID, 'robotCheckbox')
    ROBOTS_RULE_RADIOBUTTON = (By.ID, 'robotsRule')
    SUBMIT_BUTTON = (By.XPATH, '/html/body/div/form/button')

    def __init__(self, browser):
        super().__init__(browser)
        self.open()

    def open(self):
        self.browser.get(RobotCaptchaPage.URL)
        self.browser.implicitly_wait(Config.DEFAULT_TIMEOUT // 2)

    @property
    def x_value(self) -> int:
        return int(self.browser.find_element(*RobotCaptchaPage.X_VALUE).text)

    @property
    def result_input(self):
        return self.browser.find_element(*RobotCaptchaPage.RESULT_INPUT)

    @property
    def robot_checkbox(self):
        return self.browser.find_element(*RobotCaptchaPage.ROBOT_CHECKBOX)

    @property
    def robots_rule_radiobutton(self):
        return self.browser.find_element(*RobotCaptchaPage.ROBOTS_RULE_RADIOBUTTON)

    @property
    def submit_button(self):
        return self.browser.find_element(*RobotCaptchaPage.SUBMIT_BUTTON)

    def answer(self, value: float, enter: bool = False):
        self.result_input.send_keys(value)
        self.robot_checkbox.click()
        self.robots_rule_radiobutton.click()

        self.click_button_or_press_enter_on_input(
            input=self.result_input,
            button=self.submit_button,
            enter=enter,
        )

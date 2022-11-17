from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from config import Config


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def wait_for_presence_of_all_elements_located(self, locator, timeout=Config.DEFAULT_TIMEOUT):
        WebDriverWait(self.browser, timeout).until(
            expected_conditions.presence_of_all_elements_located(locator)
        )

    def click_element_from_list_of_elements(self, locator, number_of_element, timeout=Config.DEFAULT_TIMEOUT):
        elements = WebDriverWait(self.browser, timeout).until(
            expected_conditions.presence_of_all_elements_located(locator)
        )
        elements[number_of_element].click()

    @classmethod
    def click_button_or_press_enter_on_input(cls, input, button, enter: bool = False):
        if enter:
            input.send_keys(Keys.RETURN)
        else:
            button.click()

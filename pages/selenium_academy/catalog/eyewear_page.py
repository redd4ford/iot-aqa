from urllib.parse import urljoin

from selenium.webdriver.common.by import By

from config import Config, MadisonIslandEndpoints
from pages.base_page import BasePage


class EyewearPage(BasePage):
    URL = urljoin(Config.MADISON_ISLAND_BASE_URL, MadisonIslandEndpoints.ACCESSORIES_EYEWEAR_URL)

    MESSAGE_FIELD = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div[2]/div[1]/p[2]')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    class StaticData:
        NO_PRODUCTS_TEXT = 'There are no products matching the selection.'

    @property
    def message_field(self):
        return self.browser.find_element(*EyewearPage.MESSAGE_FIELD)

    def is_items(self):
        return self.message_field.text != EyewearPage.StaticData.NO_PRODUCTS_TEXT

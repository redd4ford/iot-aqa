from urllib.parse import urljoin, quote

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from config import Config, MadisonIslandEndpoints
from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    URL = urljoin(Config.MADISON_ISLAND_BASE_URL, MadisonIslandEndpoints.CATALOG_SEARCH_URL)

    MEN_CATEGORY = (By.PARTIAL_LINK_TEXT, 'Men')
    RED_COLOR = (By.CSS_SELECTOR, 'li.option-red:nth-child(1) > a:nth-child(1) > span:nth-child(1) > img:nth-child(1)')

    def __init__(self, browser, query_param: str):
        super().__init__(browser)
        self.browser = browser
        self.open(query_param)

    def open(self, query_param: str):
        self.browser.get(
            f'{SearchResultsPage.URL}/?q={quote(query_param)}'
        )

    @property
    def men_category(self):
        return self.browser.find_element(*SearchResultsPage.MEN_CATEGORY)

    def choose_men_category(self):
        self.men_category.click()

    def is_red_shirt_present(self):
        try:
            self.browser.find_element(*SearchResultsPage.RED_COLOR)
        except NoSuchElementException:
            return False
        return True

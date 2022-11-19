from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import Config
from pages.base_page import BasePage
from pages.selenium_academy.catalog import (
    WomenTopsAndBlousesPage,
    EyewearPage
)
from pages.selenium_academy.main import SearchResultsPage


class HomePage(BasePage):
    URL = Config.MADISON_ISLAND_BASE_URL

    NAVIGATION_WOMEN = (By.CSS_SELECTOR, 'li.level0:nth-child(1) > a:nth-child(1)')
    NAVIGATION_WOMEN_TOPS_AND_BLOUSES = (By.XPATH, '/html/body/div/div[2]/header/div/div[3]/nav/ol/li[1]/ul/li[3]/a')
    NAVIGATION_ACCESSORIES = (By.CSS_SELECTOR, 'li.level0:nth-child(3) > a:nth-child(1)')
    NAVIGATION_ACCESSORIES_EYEWEAR = (By.XPATH, '/html/body/div/div[2]/header/div/div[3]/nav/ol/li[3]/ul/li[2]/a')
    SEARCH_FIELD = (By.ID, 'search')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.open()

    def open(self):
        self.browser.get(HomePage.URL)

    @property
    def navigation_women(self):
        return self.browser.find_element(*HomePage.NAVIGATION_WOMEN)

    @property
    def navigation_accessories(self):
        return self.browser.find_element(*HomePage.NAVIGATION_ACCESSORIES)

    @property
    def navigation_women_tops_and_blouses(self):
        return self.browser.find_element(*HomePage.NAVIGATION_WOMEN_TOPS_AND_BLOUSES)

    @property
    def navigation_accessories_eyewear(self):
        return self.browser.find_element(*HomePage.NAVIGATION_ACCESSORIES_EYEWEAR)

    @property
    def search_field(self):
        return self.browser.find_element(*HomePage.SEARCH_FIELD)

    def point_in_navigation_dropdown(self, element):
        ActionChains(self.browser).move_to_element(element).perform()

    def navigate_to_women_tops_and_blouses(self) -> WomenTopsAndBlousesPage:
        self.point_in_navigation_dropdown(element=self.navigation_women)
        WebDriverWait(self.browser, Config.DEFAULT_TIMEOUT * 2).until(
            expected_conditions.element_to_be_clickable(HomePage.NAVIGATION_WOMEN_TOPS_AND_BLOUSES)
        ).click()
        return WomenTopsAndBlousesPage(self.browser)

    def navigate_to_accessories_eyewear(self) -> EyewearPage:
        self.point_in_navigation_dropdown(element=self.navigation_accessories)
        WebDriverWait(self.browser, Config.DEFAULT_TIMEOUT * 2).until(
            expected_conditions.element_to_be_clickable(HomePage.NAVIGATION_ACCESSORIES_EYEWEAR)
        ).click()
        return EyewearPage(self.browser)

    def search(self, text: str) -> SearchResultsPage:
        self.search_field.send_keys(text)
        self.search_field.send_keys(Keys.RETURN)
        return SearchResultsPage(self.browser, text)

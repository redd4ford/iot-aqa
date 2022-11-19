from urllib.parse import urljoin

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import Config, MadisonIslandEndpoints
from pages.base_page import BasePage


class WomenTopsAndBlousesPage(BasePage):
    URL = urljoin(Config.MADISON_ISLAND_BASE_URL, MadisonIslandEndpoints.WOMEN_TOPS_AND_BLOUSES_URL)

    FILTER_COLOR_PINK = (
        By.CSS_SELECTOR,
        'dd.even:nth-child(4) > ol:nth-child(1) > li:nth-child(2) > a:nth-child(1) > '
        'span:nth-child(1) > img:nth-child(1)'
    )

    RESULTS_UL = (
        By.XPATH,
        '/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul'
    )

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    @property
    def filter_color_pink(self):
        return self.browser.find_element(*WomenTopsAndBlousesPage.FILTER_COLOR_PINK)

    @property
    def results(self):
        return self.browser.find_element(*WomenTopsAndBlousesPage.RESULTS_UL)

    def choose_pink_color(self):
        self.filter_color_pink.click()

    def is_results(self):
        elements = WebDriverWait(self.browser, Config.DEFAULT_TIMEOUT * 2).until(
            expected_conditions.presence_of_all_elements_located(
                WomenTopsAndBlousesPage.RESULTS_UL
            )
        )
        return len(elements) > 0

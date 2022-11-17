import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Config:
    DRIVER = webdriver.Chrome(ChromeDriverManager().install())
    DEFAULT_TIMEOUT: int = 5

    SUN_IN_JULY_BASE_URL: str = os.getenv('SIJ_GH_URL', 'https://suninjuly.github.io')
    MADISON_ISLAND_BASE_URL: str = os.getenv('SA_URL', 'http://demo-store.seleniumacademy.com')

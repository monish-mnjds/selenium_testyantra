from selenium import webdriver
import pytest
from Library.Config import BROWSER, URL, DRIVER_PATH


class DriverInit:
    @pytest.fixture(autouse=True, scope='class')
    def driver_init(self, request):
        if BROWSER.upper() == 'CHROME':
            driver = webdriver.Chrome(DRIVER_PATH)
        elif BROWSER.upper() == 'SAFARI':
            driver = webdriver.Safari()
        request.cls.driver = driver
        driver.get(URL)
        driver.maximize_window()
        yield
        driver.quit()

import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SetupDriver:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.link = 'https://www.saucedemo.com/'

    def setup_driver(self):
        self.driver.get(self.link)
        logging.info(f'Opened URL: {self.link}')
        WebDriverWait(self.driver, 30).until(EC.url_to_be(self.link))
        WebDriverWait(self.driver, 30).until(EC.title_contains("Swag Labs"))
        return self.driver

    def close_driver(self):
        logging.info('Closing browser...')
        self.driver.quit()
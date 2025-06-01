from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SetupDriver:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.link = 'https://www.saucedemo.com/'

    def setup_driver(self):
        self.driver.get(self.link) # Переходить по URL
        WebDriverWait(self.driver, 30).until(EC.url_to_be(self.link)) # Ожидает URl
        WebDriverWait(self.driver, 30).until(EC.title_contains("Swag Labs")) # Ожидает заголовок
        return self.driver # Возвращает драйвер для дальнейшего использования

    def close_driver(self):
        print('Браузер закрыт\n')
        self.driver.quit() # Закрывает браузер
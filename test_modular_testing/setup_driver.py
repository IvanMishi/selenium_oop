from selenium import webdriver  # Импорт веб-драйвера
from selenium.webdriver.support.ui import WebDriverWait  # Импорт ожидания
from selenium.webdriver.support import expected_conditions as EC  # Импорт условий

class SetupDriver:  # Класс настройки драйвера
    def __init__(self):  # Конструктор
        self.driver = webdriver.Chrome() # Инициализация драйвера Chrome
        self.base_url = 'https://www.saucedemo.com/' # URL тестового сайта

    def setup_driver(self):  # Метод настройки
        self.driver.get(self.base_url) # Открытие базового URL
        WebDriverWait(self.driver, 30).until(EC.url_to_be(self.base_url)) # Ожидание загрузки URL
        WebDriverWait(self.driver, 30).until(EC.title_contains("Swag Labs")) # Ожидание появления заголовка
        return self.driver  # Возврат драйвера

    def close_driver(self):  # Метод закрытия
        print('Браузер закрыт')
        self.driver.quit()  # Корректное завершение работы драйвера
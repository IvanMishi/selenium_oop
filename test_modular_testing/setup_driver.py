import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями
from faker import Faker # Импортируем класс Faker из установленной библиотеки


class SetupDriver():
    def __init__(self):
        """Инициализация драйвера и генератора фейковых данных."""
        self.driver = webdriver.Chrome() # Сохраняет переданный драйвер как атрибут объекта для дальнейшего использования.
        self.fake = Faker("ru_RU")  # Создаём экземпляр класса Faker для генерации данных на русском языке.
        self.link = 'https://www.saucedemo.com/'  # Указываем целевую URL

    def setup_driver(self):
        """Метод создает экземпляр драйвера и открывает браузер по требуемой URL."""
        self.driver.get(self.link)  # Переходит по указанной ссылке.
        print('Ожидает загрузку страницы.')
        WebDriverWait(self.driver, 60).until(EC.url_to_be(self.link))
        print('Убеждается, что URL корректный.')
        assert self.link == self.driver.current_url, f'Ожидаемый URL: {self.link}, Фактический URL: {self.driver.current_url}'
        time.sleep(5)  # Задержка для завершения загрузки страницы
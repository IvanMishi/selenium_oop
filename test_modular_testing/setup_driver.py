from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SetupDriver:
    def __init__(self):
        """Инициализация драйвера"""
        self.driver = webdriver.Chrome() # Создает экземпляр ChromeDriver при инициализации объекта
        self.link = 'https://www.saucedemo.com/' # URL тестируемого приложения

    def setup_driver(self):
        """Настройка драйвера"""
        self.driver.get(self.link) # Переходит по ссылке
        WebDriverWait(self.driver, 30).until(EC.url_to_be(self.link)) # Ожидает загрузку конкретного URL (до 30 секунд)
        WebDriverWait(self.driver, 30).until(EC.title_contains("Swag Labs")) # Ожидае заголовок, с текстом "Swag Labs"
        return self.driver # Возвращает настроенный драйвер для использования в других частях программы

    def close_driver(self):
        """Безопасное завершение"""
        print('Браузер закрыт\n')
        self.driver.quit() # Закрывает браузер и освобождает ресурсы.
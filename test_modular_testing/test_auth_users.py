import time  # Импорт модуля для работы со временем
from users import users  # Импорт списка пользователей из модуля users
from setup_driver import SetupDriver  # Импорт класса SetupDriver
from logining_page import LoginPage  # Импорт класса LoginPage


class TestAuth:  # Объявление класса для тестирования авторизации
    """Класс тестирования авторизации в системе"""

    def __init__(self):  # Конструктор класса
        self.driver_setup = SetupDriver() # Создает экземпляр класса SetupDriver
        self.driver = self.driver_setup.setup_driver() # Получает настроенный драйвер
        self.login_page = LoginPage(self.driver) # Инициализация страницы авторизации

    def autorization_users(self):  # Метод тестирования авторизации
        print('Запуск теста авторизации пользователей')

        for user in users:  # Цикл по списку пользователей
            print(f'\nТестирование {user.username} пользователя.')
            self.login_page.authorization(user) # Авторизация пользователя
            self.driver.get("https://www.saucedemo.com/") # Возврат на страницу авторизации
            time.sleep(1)  # Пауза для стабилизации
        self.driver_setup.close_driver() # Закрывает браузер после выполнения теста
        print("Все тесты завершены")


# Создание экземпляра класса TestAuth
test_runner = TestAuth()
# Запуск теста авторизации
test_runner.autorization_users()
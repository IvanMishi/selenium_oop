from users import users  # Импортируем список пользователей
from setup_driver import SetupDriver
from login_page import LoginPage
import time


class TestAuth:
    """Класс тестирования авторизации в системе"""
    def __init__(self):
        """Метод инициализации класса TestAuth.
            Этот метод вызывается автоматически при создании нового объекта данного класса.
            Он отвечает за установку начальных значений и конфигураций, необходимых для работы экземпляра класса.
            """
        self.set = SetupDriver()  # Создает экземпляр класса SetupDriver из модуля setup_driver
        self.driver = self.set.setup_driver()  # Получает настройки драйвера.
        self.login_page = LoginPage(self.driver)  # Создает объект страницы авторизации, передавая драйвер.

    def autorization_users(self):
        """Метод для тестирования авторизации всех пользователей"""
        print('Запуск теста авторизации пользователей')

        for user in users:
            print(f'\n--- Тестирование пользователя: {user.username} ---')

            # Выполняем авторизацию для текущего пользователя
            self.login_page.authorization(user)

            # Возвращаемся на страницу авторизации для следующего теста
            self.driver.get("https://www.saucedemo.com/")
            time.sleep(1)  # Небольшая пауза для стабилизации

        # Закрываем браузер после всех тестов
        self.set.close_driver()
        print("Все тесты завершены")


# Создает экземпляр класса TestAuth и запускает тест:
start_test = TestAuth()  # Создает объект тестирования.
start_test.autorization_users()  # Запускает тест для авторизации пользователя.

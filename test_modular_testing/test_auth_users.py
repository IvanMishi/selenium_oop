from users import standard_user, locked_out_user, problem_user, performance_glitch_user # Импортирует различные типы пользователей.
from setup_driver import SetupDriver # Импортирует класс с настройками драйвера.
from login_page import LoginPage  # Импортируем класс для авторизации.


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
        """Метод для тестирования авторизации  пользователей"""
        print('Запуск теста авторизации стандартного пользователя')  # Выводит сообщение о начале теста.
        self.login_page.authorization(users) # Пытается авторизовать каждого пользователя.
        self.set.close_driver()  # Закрывает браузер после завершения каждого теста.


# Создает экземпляр класса TestAuth и запускает тест:
start_test = TestAuth()  # Создает объект тестирования.
start_test.autorization_users()  # Запускает тест для авторизации пользователя.

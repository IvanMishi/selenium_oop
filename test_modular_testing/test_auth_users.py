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


    def test_standard_user_login(self):
        """Метод для тестирования авторизации стандартного пользователя"""
        print('Запуск теста авторизации стандартного пользователя')  # Выводит сообщение о начале теста.
        self.login_page.authorization(standard_user) # Пытается авторизовать стандартного пользователя.
        self.set.close_driver()  # Закрывает браузер после завершения теста.

    def test_locked_out_user_login(self):
        """Метод для тестирования авторизации заблокированного пользователя"""
        print('Запуск теста авторизации заблокированного пользователя') # Выводит сообщение о начале теста для проблемного пользователя.
        self.login_page.authorization(locked_out_user) # Пытается авторизовать проблемного пользователя.
        self.set.close_driver() # Закрывает браузер после завершения теста.

    def test_problem_user_login(self):
        """Метод для тестирования авторизации проблемного пользователя"""
        print('Запуск теста авторизации проблемного пользователя') # Выводит сообщение о начале теста для глючного пользователя.
        self.login_page.authorization(problem_user) # Пытается авторизовать глючного пользователя.
        self.set.close_driver()  # Закрывает браузер после завершения теста.

    def performance_glitch_user(self):
        """Метод для тестирования авторизации глючного пользователя"""
        print('Запуск теста авторизации глючного пользователя')
        self.login_page.authorization(performance_glitch_user)
        self.set.close_driver()  # Закрывает браузер после завершения теста.


# Создает экземпляр класса TestAuth и запускает тесты:
start_test = TestAuth()  # Создает объект тестирования.
start_test.test_standard_user_login()  # Запускает тест для стандартного пользователя.
start_test = TestAuth()  # Создает новый объект тестирования.
start_test.test_locked_out_user_login()  # Запускает тест для заблокированного пользователя.
start_test = TestAuth()  # Создает новый объект тестирования.
start_test.test_problem_user_login()  # Запускает тест для проблемного пользователя.
start_test = TestAuth()  # Создает новый объект тестирования.
start_test.performance_glitch_user()  # Запускает тест для глючного пользователя.
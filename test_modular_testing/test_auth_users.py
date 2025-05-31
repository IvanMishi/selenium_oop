import time
from users import standard_user, locked_out_user, problem_user, performance_glitch_user
from setup_driver import SetupDriver
from login_page import LoginPage  # Импортируем класс авторизации


# Абстракция
class TestAuth:
    """Класс, включающий сценарий тестирования авторизации в системе"""
    # Констркутор
    def __init__(self):
        self.set = SetupDriver()  # Создаем экземпляр класса SetupDriver
        self.driver = self.set.setup_driver()  # Получаем настроенный драйвер
        self.login_page = LoginPage(self.driver)  # Передаем драйвер в LoginPage

    def test_standard_user_login(self):
        """Метод для тестирования авторизации стандартного пользователя"""
        print('Запуск теста авторизации стандартного пользователя')
        self.login_page.authorization(standard_user)

    def test_locked_out_user_login(self):
        """Метод для тестирования авторизации заблокированного пользователя"""
        print('Запуск теста авторизации заблокированного пользователя')
        self.login_page.authorization(locked_out_user)

    def test_problem_user_login(self):
        """Метод для тестирования авторизации проблемного пользователя"""
        print('Запуск теста авторизации проблемного пользователя')
        self.login_page.authorization(problem_user)

    def performance_glitch_user(self):
        """Метод для тестирования авторизации проблемного пользователя"""
        print('Запуск теста авторизации проблемного пользователя')
        self.login_page.authorization(performance_glitch_user)



# Создаем экземпляр класса и вызываем его методы:
start_test = TestAuth()
start_test.test_standard_user_login()

start_test = TestAuth()
start_test.test_locked_out_user_login()

start_test = TestAuth()
start_test.test_problem_user_login()

start_test = TestAuth()
start_test.performance_glitch_user()


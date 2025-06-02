from users import standard_user, locked_out_user, problem_user, performance_glitch_user # Импортирует пользователей.
from setup_driver import SetupDriver # Импортирует класс с настройками драйвера.
from login_page import LoginPage  # Импортируем класс для авторизации.



class TestAuth:
    """Класс тестирования авторизации в системе"""
    def __init__(self):
        self.set = SetupDriver()  # Создает экземпляр класса SetupDriver из модуля setup_driver
        self.driver = self.set.setup_driver()  # Получает настройки драйвера.
        self.login_page = LoginPage(self.driver)  # Передает драйвер в LoginPage.

    def test_standard_user_login(self):
        """Метод для тестирования авторизации стандартного пользователя"""
        print('Запуск теста авторизации стандартного пользователя')
        self.login_page.authorization(standard_user)
        self.set.close_driver()  # Закрывает браузер после теста

    def test_locked_out_user_login(self):
        """Метод для тестирования авторизации заблокированного пользователя"""
        print('Запуск теста авторизации заблокированного пользователя')
        self.login_page.authorization(locked_out_user)
        self.set.close_driver()  # Закрывает браузер после теста

    def test_problem_user_login(self):
        """Метод для тестирования авторизации проблемного пользователя"""
        print('Запуск теста авторизации проблемного пользователя')
        self.login_page.authorization(problem_user)
        self.set.close_driver()  # Закрывает браузер после теста

    def performance_glitch_user(self):
        """Метод для тестирования авторизации глючного пользователя"""
        print('Запуск теста авторизации глючного пользователя')
        self.login_page.authorization(performance_glitch_user)
        self.set.close_driver()  # Закрывает браузер после теста


# Создает экземпляр класса и вызываем его методы:
start_test = TestAuth()
start_test.test_standard_user_login()
# Создает экземпляр класса и вызываем его методы:
start_test = TestAuth()
start_test.test_locked_out_user_login()
# Создает экземпляр класса и вызываем его методы:
start_test = TestAuth()
start_test.test_problem_user_login()
# Создает экземпляр класса и вызываем его методы:
start_test = TestAuth()
start_test.performance_glitch_user()


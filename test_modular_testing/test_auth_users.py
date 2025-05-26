from users import standard_user, locked_out_user, problem_user, performance_glitch_user
from setup_driver import SetupDriver
from login_page import LoginPage  # Импортируем класс авторизации


class TestAuth:
    """Класс, включающий сценарий тестирования авторизации в системе"""


    def __init__(self):
        self.set = SetupDriver()  # Создаем экземпляр класса SetupDriver
        self.driver = self.set.setup_driver()  # Получаем настроенный драйвер
        self.login_page = LoginPage()  # Создаем экземпляр LoginPage для использования методов авторизации


    def test_standard_user_login(self):
        """Метод для тестирования авторизации стандартного пользователя"""
        print('Запуск теста авторизации стандартного пользователя')
        self.login_page.authorization(standard_user)  # Выполняем авторизацию стандартного пользователя


start_test = TestAuth()
start_test.test_standard_user_login()


#     def test_locked_out_user_login(self):
#         # Логика авторизации для заблокированного пользователя
#         result = self.login(locked_out_user.username, locked_out_user.password)
#         # self.assertFalse(result)  # Проверка на неуспешную авторизацию
#
#     def test_problem_user_login(self):
#         # Логика авторизации для пользователя с проблемами
#         result = self.login(problem_user.username, problem_user.password)
#         # self.assertFalse(result)  # Проверка на неуспешную авторизацию
#
#     def test_performance_glitch_user_login(self):
#         # Логика авторизации для пользователя с проблемами нажатий
#         result = self.login(performance_glitch_user.username, performance_glitch_user.password)
#         # self.assertFalse(result)  # Проверка на неуспешную авторизацию
#
#     def login(self, username, password):
#         # Реальная логика авторизации
#         # Здесь должна быть реализация API или UI для авторизации
#         pass
#
# # Создаем экземпляр класса и вызываем его методы:

# Создаем экземпляр класса и вызываем его методы:




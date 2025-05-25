import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями
from faker import Faker # Импортируем класс Faker из установленной библиотеки

from tests.login_page import Login_page
from users import standard_user, locked_out_user, problem_user, performance_glitch_user


class TestAuth():  # Общий класс, который будет содержать методы для работы в данном тесте, используется для описания веб-страницы в Selenium Python
    """Класс включающий сценарий о проверке авторизации в системе"""




    def test_standard_user_login(self):
        # Логика авторизации для стандартного пользователя
        result = self.login(standard_user.username, standard_user.password)
        # self.assertTrue(result)  # Проверка успешной авторизации

    def test_locked_out_user_login(self):
        # Логика авторизации для заблокированного пользователя
        result = self.login(locked_out_user.username, locked_out_user.password)
        # self.assertFalse(result)  # Проверка на неуспешную авторизацию

    def test_problem_user_login(self):
        # Логика авторизации для пользователя с проблемами
        result = self.login(problem_user.username, problem_user.password)
        # self.assertFalse(result)  # Проверка на неуспешную авторизацию

    def test_performance_glitch_user_login(self):
        # Логика авторизации для пользователя с проблемами нажатий
        result = self.login(performance_glitch_user.username, performance_glitch_user.password)
        # self.assertFalse(result)  # Проверка на неуспешную авторизацию

    def login(self, username, password):
        # Реальная логика авторизации
        # Здесь должна быть реализация API или UI для авторизации
        pass

# Создаем экземпляр класса и вызываем его методы:

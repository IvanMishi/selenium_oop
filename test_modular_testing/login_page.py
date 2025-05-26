# Класс LoginPage используется для авторизации на веб-сайте.
import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from setup_driver import SetupDriver

class LoginPage:
    def __init__(self):  # Убираем параметры для конструктора, так как они не нужны в данном контексте
        self.driver = SetupDriver()  # Инициализируем драйвер

    def authorization(self, user):  # Метод для выполнения авторизации
        """Метод для авторизации на сайте."""
        try:
            print('Логинится в системе')
            # Вводим имя пользователя
            input_username = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))
            input_username.send_keys(user.username)
            # Вводим пароль
            input_password = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
            input_password.send_keys(user.password)
            # Кликаем по кнопке логина
            button_login = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "login-button")))
            button_login.click()
            print('Авторизуется успешно')

        except Exception as e:
            print(f'Произошла ошибка при авторизации: {e}')
import time  # Импорт модуля времени
from selenium.webdriver.common.by import By  # Импорт стратегий поиска
from selenium.webdriver.support.ui import WebDriverWait  # Импорт явного ожидания
from selenium.webdriver.support import expected_conditions as EC  # Импорт условий ожидания
from selenium.common.exceptions import NoSuchElementException  # Импорт исключения
from Base.base_class import Base

class LoginPage(Base): # Наследование - класс потомок (вызвает методы родителя, драйвер)
    url = 'https://www.saucedemo.com/' # Обращение к URL из той страницы на которой она находится
    def __init__(self, driver):
        super().__init__(driver) # Указывает, что это потомок класса
        self.driver = driver



# ЛОКАТОРЫ.
    username = "user-name" # Локатор на странице по ID.
    password = "password" # Локатор на странице по ID.
    login_button = "login-button" # Локатор на странице по ID.



# ГЕТТЕРЫ. (Методы для использования локаторов)
    def get_username_field(self): # Возвращает значение локатора.
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.username))) # Указывает на локатор вне метода через self.
    def get_password_field(self): # Возвращает значение локатора
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.password))) # Указывает на локатор вне метода через self.
    def get_login_button(self): # Возвращает значение локатора
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.login_button))) # Указывает на локатор вне метода через self.



# ДЕЙСТВИЯ. (Методы для использования геттеров)
    def input_username(self, username):
        self.get_username_field().send_keys(username) # Указывает на геттер через self.
        print('Вводит логин')
    def input_password(self, password):
        self.get_password_field().send_keys(password) # Указывает на геттер через self.
        print('Вводит пароль')
    def click_login_button(self):
        self.get_login_button().click() # Указывает на геттер через self.
        print('Нажимает кнопку авторизации на сайте')



# МЕТОДЫ. (Тестовые шаги с использованием действий)
    def autorization_user(self):
        self.driver.get(self.url) # Вызывает метод открытия URL # Указывает на локатор вне метода через self.
        # self.driver.maximize_window() # Указывает на локатор вне метода через self.
        self.input_username('standart_user')# Вызов метода ввода данных о логине стандартного пользователя.
        self.input_username('secret_sauce')  # Вызов метода ввода данных пароля для стандартного пользователя.
        self.click_login_button() # Вызов метода нажатия на кнопку авторизации на сайте.
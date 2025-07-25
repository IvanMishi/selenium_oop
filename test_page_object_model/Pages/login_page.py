import time  # Модуль для работы с функцией ожидания
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями
from setuptools.package_index import user_agent #

from Base.base_class import Base #


class LoginPage(Base): # Наследование методов от Base
    """ Класс содержащий локаторы и методы для страницы Авторизации"""  # Для того, чтобы авторизоваться, нам необходимо выполнить три действия - ввести логин, ввести пароль, нажать кнопку "Войти".

    # КОНСТРУКТОР __init__
    def __init__(self, driver):
        super().__init__(driver)  # 'super' - указывает, что это потомок класса
        self.driver = driver

# ЛОКАТОРЫ. (Локаторы элементов, которые находятся на странице авторизации)
    username = "user-name" # Локатор на странице по ID.
    password = "password" # Локатор на странице по ID.
    login_button = "login-button" # Локатор на странице по ID.
    title_element = "title" # Локатор на странице указывающий на класс title.


# ГЕТТЕРЫ. (Методы, которые будут осуществлять поиск элементов, по ЛОКАТОРАМ, используя определенные условия поиска, и возвращающие результат данного поиска.)
    def get_username_field(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.username))) # Ищет поле на странице по указанному локатору вне метода через self и возвращает его значение далее.
    def get_password_field(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.password))) # Ищет поле на странице по указанному локатору вне метода через self и возвращает его значение далее.
    def get_login_button(self): #
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.login_button))) # Ищет кнопку на странице по указанному локатору вне метода через self и возвращает его значение далее.
    def get_title_value(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, self.title_element))) # Ищет title на странице по указанному локатору вне метода через self и возвращает его значение далее.


# ДЕЙСТВИЯ. (Методы, которые будут принимать результат поиска от ГЕТТЕРОВ и производить требуемой действие, например кликать или вводить требуемую информациюв)
    def input_username(self, username): # Функция принимает значение username. Оно передается  при перечислении самих шагов теста, для использования разных тестовых данных.
        self.get_username_field().send_keys(username) # Вызывает метод на геттера через self и вводит данные.
        print('Вводит логин')
    def input_password(self, password):  # Функция принимает значение password. Оно передается  при перечислении самих шагов теста, для использования разных тестовых данных.
        self.get_password_field().send_keys(password) # Вызывает метод на геттера через self и вводит данные.
        print('Вводит пароль')
    def click_login_button(self):
        self.get_login_button().click() # Вызывает метод на геттера через self и нажимает кнопку.
        print('Нажимает кнопку авторизации на сайте')


# МЕТОДЫ. (Метод, содержащий список ДЕИИСТВИЙ, как шагов.)
    def authorization_user(self):
        self.driver.get(self.url) # Вызывает метод открытия URL # Стандартный вызов - не через conftest
        self.get_current_url()
        self.input_username('standard_user')# Вызов действия ввода данных о логине стандартного пользователя.
        self.input_password('secret_sauce')  # Вызов действия ввода данных пароля для стандартного пользователя.
        self.click_login_button() # Вызов действия нажатия на кнопку авторизации на сайте.
        print('Авторизован')
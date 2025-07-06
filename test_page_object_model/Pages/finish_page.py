import time  # Импорт модуля времени
from selenium.webdriver.common.by import By  # Импорт стратегий поиска
from selenium.webdriver.support.ui import WebDriverWait  # Импорт явного ожидания
from selenium.webdriver.support import expected_conditions as EC  # Импорт условий ожидания
from selenium.common.exceptions import NoSuchElementException  # Импорт исключения
from Base.base_class import Base

class FinishPage(Base): # Наследование - класс потомок (вызвает методы родителя, драйвер)
    """ Класс содержащий локаторы и методы для страницы оплаты товара"""  # Для того, чтобы авторизоваться, нам необходимо выполнить три действия - ввести логин, ввести пароль, нажать кнопку "Войти".


    # Конструктор __init__
    def __init__(self, driver):
        super().__init__(driver) # Указывает, что это потомок класса
        self.driver = driver


# МЕТОДЫ. (Метод, содержащий список ДЕИИСТВИЙ, как шагов.)
    def finish(self):
        self.get_current_url()
        self.assert_url("https://www.saucedemo.com/inventory.html")
        self.get_screenshot('e') # Вызов метода для подтверждения авторизации на сайте, resulе - значение с которым сравнивается.


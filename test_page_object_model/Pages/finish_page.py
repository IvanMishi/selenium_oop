import time  # Импорт модуля времени
from selenium.webdriver.common.by import By  # Импорт стратегий поиска
from selenium.webdriver.support.ui import WebDriverWait  # Импорт явного ожидания
from selenium.webdriver.support import expected_conditions as EC  # Импорт условий ожидания
from selenium.common.exceptions import NoSuchElementException  # Импорт исключения

from Base.base_class import Base  # Импорт базового класса, от которого наследуются методы.
class FinishPage(Base):  # Наследование - класс потомок (Вызвает методы родителя, драйвер)
    # """ Класс содержащий локаторы и методы для страницы оплаты товара"""

    # КОНСТРУКТОР __init__
    def __init__(self, driver):
        super().__init__(driver)  # 'super' - указывает, что это потомок класса
        self.driver = driver

        # ЛОКАТОРЫ. (Локаторы элементов, которые находятся на странице авторизации)
    title_element = "title"  # Локатор на странице указывающий на класс title.

    # ГЕТТЕРЫ. (Методы, которые будут осуществлять поиск элементов, по ЛОКАТОРАМ, используя определенные условия поиска, и возвращающие результат данного поиска.)
    def get_title_value(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, self.title_element)))  # Ищет title на странице по указанному локатору вне метода через self и возвращает его значение далее.


    # МЕТОДЫ. (Метод, содержащий список ДЕИИСТВИЙ, как шагов.)
    def finish(self):
        self.get_current_url()
        self.assert_word(self.get_title_value(), 'Checkout: Complete!')  # Убеждается, что переход на страницу выполнен
        self.assert_url("https://www.saucedemo.com/checkout-complete.html")
        self.get_screenshot()

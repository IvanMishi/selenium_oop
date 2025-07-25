import time  # Модуль для работы с функцией ожидания
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями

from Base.base_class import Base # Импорт базового класса, от которого наследуются методы.
class PaymentPage(Base): # Наследование - класс потомок (Вызвает методы родителя, драйвер)
    """ Класс содержащий локаторы и методы для страницы оплаты товара"""


# Конструктор __init__
    def __init__(self, driver):
        super().__init__(driver)  # Указывает, что это потомок класса.
        self.driver = driver


# ЛОКАТОРЫ. (Локаторы элементов, которые находятся на странице авторизации)
    button_finish = "finish" # Локатор кнопки оплаты товаров на странице по ID.
    title_element = "title" # Локатор на странице указывающий на класс title.

# ГЕТТЕРЫ. (Методы, которые будут осуществлять поиск элементов, по ЛОКАТОРАМ, используя определенные условия поиска, и возвращающие результат данного поиска.)
    def get_button_finish(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.button_finish))) # Ищет кнопку оплаты товаров на странице по указанному локатору вне метода через self и возвращает его значение далее.
    def get_title_value(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, self.title_element)))  # Ищет title на странице по указанному локатору вне метода через self и возвращает его значение далее.

# ДЕЙСТВИЯ. (Методы, которые будут принимать результат поиска от ГЕТТЕРОВ и производить требуемой действие, например кликать или вводить требуемую информациюв)
    def click_button_finish(self):
        self.get_button_finish().click()  # Вызывает метод на геттере через self и нажимает кнопку.
        print('Нажимает кнопку "finish" для подтверждения оплаты товаров')


# МЕТОДЫ. (Метод, содержащий список ДЕИИСТВИЙ, как шагов.)
    def select_product(self):
        self.get_current_url()
        self.assert_word(self.get_title_value(), 'Checkout: Overview')  # Убеждается, что переход на страницу выполнен
        self.click_button_finish() # Нажимает кнопку подтверждения оплаты товара.



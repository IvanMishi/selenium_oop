import time  # Модуль для работы с функцией ожидания
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями
from Base.base_class import Base


class ClientInfoPage(Base): # Наследование - класс потомок (Вызывает методы родителя)
    """ Класс содержащий локаторы и методы для страницы заполнения данными о клиенте"""  # Для того, чтобы авторизоваться, нам необходимо выполнить три действия - ввести логин, ввести пароль, нажать кнопку "Войти".


    # Конструктор __init__
    def __init__(self, driver):
        super().__init__(driver) # Указывает, что это потомок класса.
        self.driver = driver


# ЛОКАТОРЫ. (Локаторы элементов, которые находятся на странице авторизации)
    first_name = "first-name" # Локатор на странице по ID.
    last_name = "last-name" # Локатор на странице по ID.
    postal_code = "postal-code" # Локатор на странице по ID.
    button_continue = "continue"  # Локатор на странице по ID.
    title_element = "title" # Локатор на странице указывающий на класс title.

# ГЕТТЕРЫ. (Методы, которые будут осуществлять поиск элементов, по ЛОКАТОРАМ, используя определенные условия поиска, и возвращающие результат данного поиска.)
    def get_first_name(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.first_name))) # Ищет поле на странице по указанному локатору вне метода через self и возвращает его значение далее.
    def get_last_name(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.last_name))) # Ищет поле на странице по указанному локатору вне метода через self и возвращает его значение далее.
    def get_postal_code(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.postal_code))) # Ищет поле на странице по указанному локатору вне метода через self и возвращает его значение далее.
    def get_button_continue(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.button_continue))) # Ищет кнопку на странице по указанному локатору вне метода через self и возвращает его значение далее.
    def get_title_value(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, self.title_element)))  # Ищет title на странице по указанному локатору вне метода через self и возвращает его значение далее.

# ДЕЙСТВИЯ. (Методы, которые будут принимать результат поиска от ГЕТТЕРОВ и производить требуемой действие, например кликать или вводить требуемую информацию.)
    def input_first_name(self, first_name): # Функция принимает значение username. Оно передается при перечислении самих шагов теста, для использования разных тестовых данных.
        self.get_first_name().send_keys(first_name) # Вызывает метод на геттера через self и вводит данные.
        print('Заполняет поле именем клиента')
    def input_last_name(self, last_name):  # Функция принимает значение password. Оно передается при перечислении самих шагов теста, для использования разных тестовых данных.
        self.get_last_name().send_keys(last_name) # Вызывает метод на геттера через self и вводит данные.
        print('Заполняет поле фамилией клиента')
    def input_postal_code(self, postal_code):  # Функция принимает значение password. Оно передается при перечислении самих шагов теста, для использования разных тестовых данных.
        self.get_postal_code().send_keys(postal_code) # Вызывает метод на геттера через self и вводит данные.
        print('Заполняет поле почтовый индекс')
    def click_button_continue(self):
        self.get_button_continue().click() # Вызывает метод на геттере через self и нажимает кнопку.
        print('Нажимает кнопку продолжить после заполнения полей клиентскими данными')


# МЕТОДЫ. (Метод, содержащий список ДЕИИСТВИЙ, как шагов.)
    def input_client_information(self):
        self.get_current_url()
        self.assert_word(self.get_title_value(), 'Checkout: Your Information')  # Убеждается, что переход на страницу выполнен
        self.input_first_name(self.fake.first_name())
        self.input_last_name(self.fake.last_name())
        self.input_postal_code(self.fake.port_number())
        self.click_button_continue()



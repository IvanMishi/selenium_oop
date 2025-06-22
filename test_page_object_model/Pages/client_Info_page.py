import time  # Импорт модуля времени
from selenium.webdriver.common.by import By  # Импорт стратегий поиска
from selenium.webdriver.support.ui import WebDriverWait  # Импорт явного ожидания
from selenium.webdriver.support import expected_conditions as EC  # Импорт условий ожидания
from selenium.common.exceptions import NoSuchElementException  # Импорт исключения
from Base.base_class import Base
from faker import Faker # Импортируем класс Faker из установленной библиотеки


class ClientInfoPage(Base): # Наследование - класс потомок (вызвает методы родителя, драйвер)
    """ Класс содержащий локаторы и методы для страницы заполнения данными о клиенте'"""  # Для того, чтобы авторизоваться, нам необходимо выполнить три действия - ввести логин, ввести пароль, нажать кнопку "Войти".


    # Конструктор __init__, в целом Мы можем его не использовать, так как сам driver у нас будет подтягиваться из теста, но он может понадобиться, на случай необходимости использовать новые переменные которые будут использоваться в разных классах.
    def __init__(self, driver):
        super().__init__(driver) # Указывает, что это потомок класса
        self.driver = driver
        fake = Faker(
            "ru_Ru")  # Создаём экземпляр класса Faker, указывая, что хотим генерировать данные на (ru_Ru - русский язык)


    #
    # print('Заполняет поля данными о заказчике')
    # for i in driver.find_elements(By.CSS_SELECTOR, '[class="input_error form_input"]'):
    #     i.send_keys(fake.random_letter())




# ЛОКАТОРЫ. (Локаторы элементов, которые находятся на странице авторизации)
    first_name = "first-name" # Локатор на странице по ID .
    last_name = "last-name" # Локатор на странице по ID .
    postal_code = "postal-code" # Локатор на странице по ID .
    button_continue = "continue"  # Локатор на странице по ID .


# ГЕТТЕРЫ. (Методы, которые будут осуществлять поиск элементов, по ЛОКАТОРАМ, используя определенные условия поиска, и возвращающие результат данного поиска.)
    def get_first_name(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.first_name))) # Ищет поле на странице по указанному локатору вне метода через self и возвращает его значение далее.
    def get_last_name(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.last_name))) # Ищет поле на странице по указанному локатору вне метода через self и возвращает его значение далее.
    def get_postal_code(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.postal_code))) # Ищет поле на странице по указанному локатору вне метода через self и возвращает его значение далее.
    def get_button_continue(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.button_continue))) # Ищет поле на странице по указанному локатору вне метода через self и возвращает его значение далее.


# ДЕЙСТВИЯ. (Методы, которые будут принимать результат поиска от ГЕТТЕРОВ и производить требуемой действие, например кликать или вводить требуемую информациюв)
    def input_first_name(self, first_name): # Функция принимает значение username. Оно передается  при перечислении самих шагов теста, для использования разных тестовых данных.
        self.get_first_name.send_keys(first_name) # Вызывает метод на геттера через self и вводит данные.
        print('Заполняет поле именем клиента')
    def input_last_name(self, last_name):  # Функция принимает значение password. Оно передается  при перечислении самих шагов теста, для использования разных тестовых данных.
        self.get_last_name().send_keys(last_name) # Вызывает метод на геттера через self и вводит данные.
        print('Заполняет поле фамилией клиента')
    def input_postal_code(self, postal_code):  # Функция принимает значение password. Оно передается  при перечислении самих шагов теста, для использования разных тестовых данных.
        self.get_last_name().send_keys(postal_code) # Вызывает метод на геттера через self и вводит данные.
        print('Заполняет поле zip code')
    def click_button_continue(self):
        self.get_button_continue().click() # Вызывает метод на геттере через self и нажимает кнопку.
        print('Нажимает кнопку продолжить после заполнения полей клиентскими данными')



# МЕТОДЫ. (Метод, содержащий список ДЕИИСТВИЙ, как шагов.)
    def input_client_information(self):
        self.get_current_url()
        self.input_first_name(self.fake.random_letter())
        self.input_last_name(self.fake.random_letter())
        self.input_postal_code(self.fake.random_letter())
        self.click_button_continue()




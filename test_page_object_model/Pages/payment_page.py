import time  # Импорт модуля времени
from selenium.webdriver.common.by import By  # Импорт стратегий поиска
from selenium.webdriver.support.ui import WebDriverWait  # Импорт явного ожидания
from selenium.webdriver.support import expected_conditions as EC  # Импорт условий ожидания
from selenium.common.exceptions import NoSuchElementException  # Импорт исключения
from Base.base_class import Base

class PaymentPage(Base): # Наследование - класс потомок (вызвает методы родителя, драйвер)
    """ Класс содержащий локаторы и методы для страницы оплаты товара"""  # Для того, чтобы авторизоваться, нам необходимо выполнить три действия - ввести логин, ввести пароль, нажать кнопку "Войти".


    # Конструктор __init__, в целом Мы можем его не использовать, так как сам driver у нас будет подтягиваться из теста, но он может понадобиться, на случай необходимости использовать новые переменные которые будут использоваться в разных классах.
    def __init__(self, driver):
        super().__init__(driver) # Указывает, что это потомок класса
        self.driver = driver




# ЛОКАТОРЫ. (Локаторы элементов, которые находятся на странице авторизации)
    button_finish = "finish" # Локатор кнопки оплаты товаров на странице по ID.


# ГЕТТЕРЫ. (Методы, которые будут осуществлять поиск элементов, по ЛОКАТОРАМ, используя определенные условия поиска, и возвращающие результат данного поиска.)
    def get_button_finish(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.ID, self.button_finish))) # Ищет кнопку оплаты товаров на странице по указанному локатору вне метода через self и возвращает его значение далее.


# ДЕЙСТВИЯ. (Методы, которые будут принимать результат поиска от ГЕТТЕРОВ и производить требуемой действие, например кликать или вводить требуемую информациюв)
    def click_button_finish(self):
        self.get_button_finish().click()  # Вызывает метод на геттере через self и нажимает кнопку.
        print('Нажимает кнопку "finish" для подтверждения оплаты товаров')


# МЕТОДЫ. (Метод, содержащий список ДЕИИСТВИЙ, как шагов.)
    def select_product(self):
        self.get_current_url()
        self.click_button_finish() # Нажимает кнопку подтверждения оплаты товара.
        self.assert_word(self.get_title_value(),'Your Cart')  # Вызов метода для подтверждения авторизации на сайте, resulе - значение с которым сравнивается.


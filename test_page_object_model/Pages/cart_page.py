import time  # Импорт модуля времени
from selenium.webdriver.common.by import By  # Импорт стратегий поиска
from selenium.webdriver.support.ui import WebDriverWait  # Импорт явного ожидания
from selenium.webdriver.support import expected_conditions as EC  # Импорт условий ожидания
from selenium.common.exceptions import NoSuchElementException  # Импорт исключения
from Base.base_class import Base

class CartPage(Base): # Наследование - класс потомок (вызвает методы родителя, драйвер)
    """ Класс содержащий локаторы и методы для страницы Авторизации"""  # Для того, чтобы авторизоваться, нам необходимо выполнить три действия - ввести логин, ввести пароль, нажать кнопку "Войти".


    # Конструктор __init__, в целом Мы можем его не использовать, так как сам driver у нас будет подтягиваться из теста, но он может понадобиться, на случай необходимости использовать новые переменные которые будут использоваться в разных классах.
    def __init__(self, driver):
        super().__init__(driver) # Указывает, что это потомок класса
        self.driver = driver






# ЛОКАТОРЫ. (Локаторы элементов, которые находятся на странице авторизации)
    checkout_button = "checkout" # Локатор блока товаров на странице по ID.



# ГЕТТЕРЫ. (Методы, которые будут осуществлять поиск элементов, по ЛОКАТОРАМ, используя определенные условия поиска, и возвращающие результат данного поиска.)
    def get_checkout_button(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.checkout_button))) # Ищет кнопку перехода в корзину на странице по указанному локатору вне метода через self и возвращает его значение далее.



# ДЕЙСТВИЯ. (Методы, которые будут принимать результат поиска от ГЕТТЕРОВ и производить требуемой действие, например кликать или вводить требуемую информациюв)
    def click_checkout_button(self): #
        self.get_checkout_button.click()  # Вызывает метод на геттере через self и нажимает кнопку для перехода в корзину.
        print('Нажимает кнопку')



# МЕТОДЫ. (Метод, содержащий список ДЕИИСТВИЙ, как шагов.)
    def product_confirmation(self): # Подтверждение товара
        self.get_current_url()
        self.click_checkout_button() # Выбирает первые два товара


import time  # Импорт модуля времени
from selenium.common.exceptions import NoSuchElementException  # Импорт исключения
from selenium.webdriver.common.by import By  # Импорт стратегий поиска
from selenium.webdriver.support.ui import WebDriverWait  # Импорт явного ожидания
from selenium.webdriver.support import expected_conditions as EC  # Импорт условий ожидания
from Base.base_class import Base

class CartPage(Base):
    """ Класс содержащий локаторы и методы для страницы Корзина товаров"""

    # КОНСТРУКТОР __init__
    def __init__(self, driver):
        super().__init__(driver)  # 'super' - указывает, что это потомок класса
        self.driver = driver

# ЛОКАТОРЫ. (Локаторы элементов, которые находятся на странице авторизации)
    checkout_button = "checkout" # Локатор кнопки по ID.
    title_element = "title" # Локатор на странице указывающий на класс title.

# ГЕТТЕРЫ. (Методы, которые будут осуществлять поиск элементов, по ЛОКАТОРАМ, используя определенные условия поиска, и возвращающие результат данного поиска.)
    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, self.checkout_button)))
    def get_title_value(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, self.title_element))) # Ищет title на странице по указанному локатору вне метода через self и возвращает его значение далее.

# ДЕЙСТВИЯ. (Методы, которые будут принимать результат поиска от ГЕТТЕРОВ и производить требуемой действие, например кликать или вводить требуемую информациюв)
    def click_checkout_button(self): #
        self.get_checkout_button().click()  # Вызывает метод на геттере через self и нажимает кнопку для перехода в корзину.
        print('Нажимает кнопку для перехода к заполнению информации о заказчике')

# МЕТОДЫ. (Метод, содержащий список ДЕИИСТВИЙ, как шагов.)
    def product_confirmation(self): # Подтверждение товара
        self.get_current_url()
        self.assert_word(self.get_title_value(), 'Your Cart')  # Убеждается, что переход на страницу выполнен
        self.click_checkout_button()



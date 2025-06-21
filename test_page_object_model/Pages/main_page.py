import time  # Импорт модуля времени
from selenium.webdriver.common.by import By  # Импорт стратегий поиска
from selenium.webdriver.support.ui import WebDriverWait  # Импорт явного ожидания
from selenium.webdriver.support import expected_conditions as EC  # Импорт условий ожидания
from selenium.common.exceptions import NoSuchElementException  # Импорт исключения
from Base.base_class import Base

class MainPage(Base): # Наследование - класс потомок (вызвает методы родителя, драйвер)
    """ Класс содержащий локаторы и методы для страницы Авторизации"""  # Для того, чтобы авторизоваться, нам необходимо выполнить три действия - ввести логин, ввести пароль, нажать кнопку "Войти".


    # Конструктор __init__, в целом Мы можем его не использовать, так как сам driver у нас будет подтягиваться из теста, но он может понадобиться, на случай необходимости использовать новые переменные которые будут использоваться в разных классах.
    def __init__(self, driver):
        super().__init__(driver) # Указывает, что это потомок класса
        self.driver = driver



    # print('Убеждается что переход в корзину с товарами выполнен')
    # assert driver.find_element(By.CLASS_NAME, "title").text == 'Your Cart', f'Переход в корзину не выполнен'
    # time.sleep(2)
    # #
    # # print('Убеждается, что в корзине товаров добавлено - 2 шт')
    # quantity = []
    # for i in driver.find_elements(By.CSS_SELECTOR, '[data-test="item-quantity"]'):
    #     quantity.append(int(i.text))
    # assert sum(quantity) == 2, f'Количество товаров в корзине не корректно'
    # time.sleep(2)


# ЛОКАТОРЫ. (Локаторы элементов, которые находятся на странице авторизации)
    list_products = "inventory_item" # Локатор блока товаров на странице по CLASS_NAME .
    button_shopping_cart  = "shopping_cart_badge"  # Локатор кнопки для перехода в козину на странице по CLASS_NAME .


# ГЕТТЕРЫ. (Методы, которые будут осуществлять поиск элементов, по ЛОКАТОРАМ, используя определенные условия поиска, и возвращающие результат данного поиска.)
    def get_list_products(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, self.list_products))) # Ищет карточки товаров на странице по указанному локатору вне метода через self и возвращает его значение далее.

    def get_button_shopping_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, self.button_shopping_cart))) # Ищет кнопку перехода в корзину на странице по указанному локатору вне метода через self и возвращает его значение далее.



# ДЕЙСТВИЯ. (Методы, которые будут принимать результат поиска от ГЕТТЕРОВ и производить требуемой действие, например кликать или вводить требуемую информациюв)
    def click_item_list_product(self):
        for item in self.get_list_products()[:2]: # Выбирает из списка товаров первые два
            item.find_element(By.CLASS_NAME, "btn").click()   # Вызывает метод на геттере через self и нажимает кнопку для добавления товара в корзину в корзину.

    def click_button_shopping_cart(self): #
        self.get_button_shopping_cart().click()  # Вызывает метод на геттере через self и нажимает кнопку для перехода в корзину.
        print('Нажимает кнопку авторизации на сайте')



# МЕТОДЫ. (Метод, содержащий список ДЕИИСТВИЙ, как шагов.)
    def select_product(self):
        self.get_current_url()
        self.click_item_list_product() # Выбирает первые два товара
        self.click_button_shopping_cart() # Нажимает на кнопку перехода в корзину


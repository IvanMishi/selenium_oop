import time  # Модуль для работы с функцией ожидания
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями
from Base.base_class import Base

class MainPage(Base): # Наследование - класс потомок (вызвает методы родителя, драйвер)
    """ Класс содержащий локаторы и методы для страницы 'Main'"""  # Для того, чтобы авторизоваться, нам необходимо выполнить три действия - ввести логин, ввести пароль, нажать кнопку "Войти".

    # КОНСТРУКТОР __init__
    def __init__(self, driver):
        super().__init__(driver)  # 'super' - указывает, что это потомок класса
        self.driver = driver


# ЛОКАТОРЫ. (Локаторы элементов, которые находятся на странице авторизации)
    select_product_1 = "add-to-cart-sauce-labs-backpack" # Локатор  товара 1 на странице по ID
    select_product_2 = "add-to-cart-sauce-labs-bike-light"  # Локатор  товара 2 на странице по ID
    select_product_3 = "add-to-cart-sauce-labs-bolt-t-shirt"  # Локатор  товара 3 на странице по ID

    button_shopping_cart  = "shopping_cart_link"  # Локатор кнопки для перехода в козину на странице по CLASS_NAME
    button_checkout = "checkout"

    burger_menu = "//button[@id='react-burger-menu-btn']" # Локатор ,бургер меню на странице по ID
    link_about = "//a[@id='about_sidebar_link']" # Локатор , ссылки 'about' на странице в бургер меню по ID
    title_element = "title" # Локатор на странице указывающий на класс title.


# ГЕТТЕРЫ. (Методы, которые будут осуществлять поиск элементов, по ЛОКАТОРАМ, используя определенные условия поиска, и возвращающие результат данного поиска.)
    def get_select_products_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.select_product_1))) # Ищет карточки товаров на странице по указанному локатору вне метода через self и возвращает его значение далее.
    def get_select_products_2(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.select_product_2))) # Ищет карточки товаров на странице по указанному локатору вне метода через self и возвращает его значение далее.
    def get_select_products_3(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.select_product_3))) # Ищет карточки товаров на странице по указанному локатору вне метода через self и возвращает его значение далее.

    def get_button_shopping_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, self.button_shopping_cart))) # Ищет кнопку перехода в корзину на странице по указанному локатору вне метода через self и возвращает его значение далее.

    def get_burger_menu(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.burger_menu))) # Ищет кнопку перехода в корзину на странице по указанному локатору вне метода через self и возвращает его значение далее.
    def get_link_about(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.link_about)))  # Ищет кнопку перехода в корзину на странице по указанному локатору вне метода через self и возвращает его значение далее.
    def get_title_value(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, self.title_element))) # Ищет title на странице по указанному локатору вне метода через self и возвращает его значение далее.


# ДЕЙСТВИЯ. (Методы, которые будут принимать результат поиска от ГЕТТЕРОВ и производить требуемой действие, например кликать или вводить требуемую информациюв)
    def click_select_products_1(self):
        self.get_select_products_1().click() # Вызывает метод на геттере через self и нажимает кнопку для добавления товара в корзину в корзину.
        print('Выбирает первый товар')
    def click_select_products_2(self):
        self.get_select_products_2().click() # Вызывает метод на геттере через self и нажимает кнопку для добавления товара в корзину в корзину.
        print('Выбирает второй товар')
    def click_select_products_3(self):
        self.get_select_products_3().click() # Вызывает метод на геттере через self и нажимает кнопку для добавления товара в корзину в корзину.
        print('Выбирает третий товар')

    def click_button_shopping_cart(self): #
        self.get_button_shopping_cart().click()  # Вызывает метод на геттере через self и нажимает кнопку для перехода в корзину.
        print('Нажимает кнопку перехода в корзину')


    def click_get_burger_menu(self): #
        self.get_burger_menu().click()  # Вызывает метод на геттере через self и нажимает кнопку для перехода в корзину.
        print('Нажимает кнопку бургер-меню на сайте')
    def click_link_about(self): #
        self.get_link_about().click()  # Вызывает метод на геттере через self и нажимает кнопку для перехода по ссылке.
        print('Нажимает ссылку about в бургер-меню на сайте')


# МЕТОДЫ. (Метод, содержащий список ДЕИИСТВИЙ, как шагов.)
    # Метод для выбора продуктов
    def select_products_to_cart_1(self):
        self.get_current_url()
        self.assert_word(self.get_title_value(),'Products' ) # Убеждается, что переход на страницу выполнен
        self.get_screenshot(element=self.get_title_value())
        self.click_select_products_1()
        self.click_button_shopping_cart()
        time.sleep(1) # Ждет 1 сек

    def select_products_to_cart_2(self):
        self.get_current_url()
        self.assert_word(self.get_title_value(),'Products' ) # Убеждается, что переход на страницу выполнен
        self.get_screenshot(element=self.get_title_value())
        self.click_select_products_2()
        self.click_button_shopping_cart()
        time.sleep(1) # Ждет 1 сек

    def select_products_to_cart_3(self):
        self.get_current_url()
        self.assert_word(self.get_title_value(),'Products' ) # Убеждается, что переход на страницу выполнен
        self.get_screenshot(element=self.get_title_value())
        self.click_select_products_3()
        self.click_button_shopping_cart()
        time.sleep(1) # Ждет 1 сек


    # Метод для перехода по ссылке 'about' в 'бургер меню' на странице 'main_page'
    def select_menu_about(self):
        self.get_current_url()
        self.click_get_burger_menu() # Нажимает на 'бургер меню'
        time.sleep(1) # Ждет 1 сек
        self.click_link_about() # Нажимает на ссылку 'about' и переходит по ней
        self.assert_url('https://saucelabs.com/') # Убеждается, что переход выполнен

        time.sleep(3) # Ждет 3 сек

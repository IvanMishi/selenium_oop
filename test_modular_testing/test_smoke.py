import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from tests.login_page import Login_page

class TestSmoke:
    """Класс, включающий сценарий проверки авторизации в системе"""

    def __init__(self):
        self.driver = webdriver.Chrome()  # Инициализация драйвера
        self.fake = Faker()  # Инициализация Faker для генерации фейковых данных

    def wait_until_visible(self, by, value):
        """Ожидает видимости элемента"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, value)))

    def add_items_to_cart(self):
        """Добавляет товары в корзину и сохраняет их названия и цены"""
        item_name = []
        item_price = []
        print('Находит список товаров на странице...')
        list_item = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        print('Добавляет 2 первых товара из списка в корзину...')
        for item in list_item[:2]:
            item_name.append(item.find_element(By.CLASS_NAME, "inventory_item_name").text)
            item_price.append(float(item.find_element(By.CLASS_NAME, "inventory_item_price").text.split('$')[1]))
            item.find_element(By.CLASS_NAME, "btn").click()
        return item_name, item_price

    def verify_cart(self, expected_item_names, expected_item_prices):
        """Проверяет корректность товаров в корзине"""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.wait_until_visible(By.CLASS_NAME, "title")
        assert self.driver.find_element(By.CLASS_NAME, "title").text == 'Your Cart', 'Переход в корзину не выполнен'
        
        quantity = [int(i.text) for i in self.driver.find_elements(By.CSS_SELECTOR, '[data-test="item-quantity"]')]
        assert sum(quantity) == 2, 'Количество товаров в корзине некорректно'

        for price in expected_item_prices:
            assert price in [float(item.text.split('$')[1]) for item in self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")], 'Стоимость товаров не совпадает'

    def fill_checkout_form(self):
        """Заполняет форму оформления заказа"""
        self.driver.find_element(By.ID, "checkout").click()
        self.wait_until_visible(By.CSS_SELECTOR, '[data-test="title"]')
        assert self.driver.find_element(By.CSS_SELECTOR, '[data-test="title"]').text == 'Checkout: Your Information', 'Переход на страницу заполнения полей о заказчике не выполнен'
        
        inputs = self.driver.find_elements(By.CSS_SELECTOR, '[class="input_error form_input"]')
        for input_field in inputs:
            input_field.send_keys(self.fake.first_name())  # Или любую другую информацию

        self.driver.find_element(By.ID, "continue").click()
        self.wait_until_visible(By.CLASS_NAME, "cart_quantity_label")
        assert self.driver.find_element(By.CLASS_NAME, "cart_quantity_label").text == 'QTY', 'Переход на страницу с подтверждением заказа не выполнен'

    def test_smoke_path(self):
        """Основной тестовый метод"""
        item_names, item_prices = self.add_items_to_cart()
        self.verify_cart(item_names, item_prices)
        self.fill_checkout_form()

        # Проверка суммы товаров
        total_price = sum(item_prices)
        assert total_price == float(self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text.split('$')[1]), 'Сумма товаров некорректна'
        
        print('Нажимает кнопку "Finish" для завершения заказа...')
        self.driver.find_element(By.ID, "finish").click()
        self.wait_until_visible(By.CLASS_NAME, 'complete-header')
        assert self.driver.find_element(By.CLASS_NAME,'complete-header').text == 'Thank you for your order!', 'Ошибка: форма не отправлена, не найден элемент с подтверждающим текстом'

# Создаем экземпляр класса и вызываем его методы
test = TestSmoke()
test.test_smoke_path()
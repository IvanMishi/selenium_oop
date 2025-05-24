import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями
from faker import Faker # Импортируем класс Faker из установленной библиотеки

from tests.login_page import Login_page


class Test_smoke_1():  # Общий класс, который будет содержать методы для работы в данном тесте.
    """Класс включающий сценарий о проверке авторизации в системе"""


    def setup_driver(self):
        """Метод создает экземпляр драйвера и открывает браузер по требуемой URL."""
        self.driver = webdriver.Chrome()
        self.link = 'https://www.saucedemo.com/'
        self.driver.get(self.link)  # Переходит по указанной ссылке.
        print('Ожидает загрузку страницы.')
        WebDriverWait(self.driver, 60).until(EC.url_to_be(self.link))
        print('Убеждается, что URL корректный.')
        assert self.link == self.driver.current_url, f'Ожидаемый URL: {self.link}, Фактический URL: {self.driver.current_url}'
        self.fake = Faker("ru_Ru")  # Создаём экземпляр класса Faker, указывая, что хотим генерировать данные на (ru_Ru - русский язык)
        time.sleep(5)


    def test_authorization_valid(self):
        """Метод для выполнения успешной авторизации."""
        print('Тестовые данные для авторизации.')
        standard_user = 'standard_user'
        locked_out_user = 'locked_out_user'
        problem_user = 'problem_user'
        performance_glitch_user = 'performance_glitch_user'
        error_user = 'error_user'
        visual_user = 'visual_user'
        standard_password = 'secret_sauce'
        login = Login_page(self.driver) # Экземпляр класса Login_page в аргументы передан driver из setup_driver
        login.authorization(standard_user, 'secret_sauce') # Вызов метода для авторизации на сайте по двум обязательным атрибутам


    def test_smoke_path(self):
        # Создает списки для хранения информации о товаре
        item_name = []
        item_price = []
        print(f'Находит список товаров на странице')
        list_item = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f'Добавляет 2 первых товара из списка в козину ')
        for item in list_item[:2]:
            print(f'Сохраняет названия добавляемых товаров')
            item_name.append(item.find_element(By.CLASS_NAME, "inventory_item_name").text)
            print(f'Сохраняет стоимость добавляемых товаров')
            item_price.append(float(item.find_element(By.CLASS_NAME, "inventory_item_price").text.split('$')[1]))
            print('Находит кнопку для переход в корзину и нажимает на нее')
            item.find_element(By.CLASS_NAME, "btn").click()

        print('Переходит в корзину')
        button_shopping_cart = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        print('Убеждается что переход в корзину с товарами выполнен')
        assert self.driver.find_element(By.CLASS_NAME, "title").text == 'Your Cart', f'Переход в корзину не выполнен'
        time.sleep(2)

        print('Убеждается, что в корзине товаров добавлено - 2 шт')
        quantity = []
        for i in self.driver.find_elements(By.CSS_SELECTOR, '[data-test="item-quantity"]'):
            quantity.append(int(i.text))
        assert sum(quantity) == 2, f'Количество товаров в корзине не корректно'
        time.sleep(2)

        print('Сравнивает товары в корзине с добавленными')
        print("Имена товаов совпадают" if float(
            self.driver.find_element(By.CLASS_NAME, "inventory_item_price").text.split('$')[
                1]) in item_price else "Имена товаров не совпадают")
        print("Стоимость товаров совпадает" if float(
            self.driver.find_element(By.CLASS_NAME, "inventory_item_price").text.split('$')[
                1]) in item_price else "Стоимость товаров не совпадает")

        print('Переходит к заполнению данными о клиенте')
        button_checkout = self.driver.find_element(By.ID, "checkout").click()
        print('Убеждается, что переход к заполению данными о клиенте выполнен')
        assert self.driver.find_element(By.CSS_SELECTOR,'[data-test = "title"]').text == 'Checkout: Your Information', f'Переход на сраниу с заполнением полей о заказчике не выполнен'
        time.sleep(2)

        print('Заполняет поля данными о заказчике')
        for i in self.driver.find_elements(By.CSS_SELECTOR, '[class="input_error form_input"]'):
            i.send_keys(self.fake.random_letter())

        print('Переходит к подтверждению заказа')
        button_continue = self.driver.find_element(By.ID, "continue").click()
        print('Убеждается, что переход к подтверждению заказа выполнен')
        assert self.driver.find_element(By.CSS_SELECTOR,'[class="cart_quantity_label"]').text == 'QTY', f'Переход на сраниу с подтверждению заказа не выполнен'
        time.sleep(2)

        print('Сравнивает товары в корзине с добавленными')
        print("Имена товаов совпадают" if float(self.driver.find_element(By.CLASS_NAME, "inventory_item_price").text.split('$')[1]) in item_price else "Имена товаров не совпадают")
        print("Стоимость товаров совпадает" if float(self.driver.find_element(By.CLASS_NAME, "inventory_item_price").text.split('$')[1]) in item_price else "Стоимость товаров не совпадает")

        print('Убеждается, что сумма товаров корректна')
        assert sum(item_price) == float(self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text.split('$')[1]), f'Сумма товаров не корректна'
        print(f'{sum(item_price)}')
        time.sleep(5)

        print('находит и нажимает кнопку "Finish" для завершения заказа')
        button_finish = self.driver.find_element(By.ID, "finish").click()

        print('Убеждается, что форма отправлена успешно')
        assert self.driver.find_element(By.CLASS_NAME,'complete-header').text == 'Thank you for your order!', f'Ошибка: форма не отправлена, не найден элемнт с подтверждающим текстом или текст был изменен'
        time.sleep(5)



# Создаем экземпляр класса и вызываем его методы:
start_test = (Test_smoke_1
              ())
start_test.setup_driver()
start_test.test_authorization_valid()# Успешная авторизация, используя корректные данные
start_test.test_smoke_path()
import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями
from faker import Faker # Импортируем класс Faker из установленной библиотеки

from Pages.login_page import LoginPage





def test_buy_products():
    driver = webdriver.Chrome()
    # fake = Faker("ru_Ru")  # Создаём экземпляр класса Faker, указывая, что хотим генерировать данные на (ru_Ru - русский язык)
    login = LoginPage(driver) # Создает экземпляр родительского класса
    login.autorization_user() # Вызывает его метод


    # print(f'Находит список товаров на странице')
    # list_item = driver.find_elements(By.CLASS_NAME, "inventory_item")
    # print(f'Добавляет 2 первых товара из списка в козину ')
    # item_name = []
    # item_price = []
    # for item in list_item[:2]:
    #     print(f'Сохраняет названия добавляемых товаров')
    #     item_name.append(item.find_element(By.CLASS_NAME, "inventory_item_name").text)
    #     print(f'Сохраняет стоимость добавляемых товаров')
    #     item_price.append(float(item.find_element(By.CLASS_NAME, "inventory_item_price").text.split('$')[1]))
    #     print('Находит кнопку для переход в корзину и нажимает на нее')
    #     item.find_element(By.CLASS_NAME, "btn").click()


    # print('Переходит в корзину')
    # button_shopping_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
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
    #
    # print('Сравнивает товары в корзине с добавленными')
    # print("Имена товаов совпадают" if float(
    #     driver.find_element(By.CLASS_NAME, "inventory_item_price").text.split('$')[
    #         1]) in item_price else "Имена товаров не совпадают")
    # print("Стоимость товаров совпадает" if float(
    #     driver.find_element(By.CLASS_NAME, "inventory_item_price").text.split('$')[
    #         1]) in item_price else "Стоимость товаров не совпадает")
    #
    # print('Переходит к заполнению данными о клиенте')
    # button_checkout = driver.find_element(By.ID, "checkout").click()
    # print('Убеждается, что переход к заполению данными о клиенте выполнен')
    # assert driver.find_element(By.CSS_SELECTOR,
    #                            '[data-test = "title"]').text == 'Checkout: Your Information', f'Переход на сраниу с заполнением полей о заказчике не выполнен'
    # time.sleep(2)
    #
    # print('Заполняет поля данными о заказчике')
    # for i in driver.find_elements(By.CSS_SELECTOR, '[class="input_error form_input"]'):
    #     i.send_keys(fake.random_letter())
    #
    # print('Переходит к подтверждению заказа')
    # button_continue = driver.find_element(By.ID, "continue").click()
    # print('Убеждается, что переход к подтверждению заказа выполнен')
    # assert driver.find_element(By.CSS_SELECTOR,
    #                            '[class="cart_quantity_label"]').text == 'QTY', f'Переход на сраниу с подтверждению заказа не выполнен'
    # time.sleep(2)
    #
    # print('Сравнивает товары в корзине с добавленными')
    # print("Имена товаов совпадают" if float(
    #     driver.find_element(By.CLASS_NAME, "inventory_item_price").text.split('$')[
    #         1]) in item_price else "Имена товаров не совпадают")
    # print("Стоимость товаров совпадает" if float(
    #     driver.find_element(By.CLASS_NAME, "inventory_item_price").text.split('$')[
    #         1]) in item_price else "Стоимость товаров не совпадает")
    #
    # print('Убеждается, что сумма товаров корректна')
    # assert sum(item_price) == float(
    #     driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text.split('$')[1]), f'Сумма товаров не корректна'
    # print(f'{sum(item_price)}')
    # time.sleep(5)
    #
    # print('находит и нажимает кнопку "Finish" для завершения заказа')
    # button_finish = driver.find_element(By.ID, "finish").click()
    #
    # print('Убеждается, что форма отправлена успешно')
    # assert self.driver.find_element(By.CLASS_NAME,'complete-header').text == 'Thank you for your order!', f'Ошибка: форма не отправлена, не найден элемнт с подтверждающим текстом или текст был изменен'
    # time.sleep(2)

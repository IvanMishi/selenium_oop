import datetime
import os
from faker import Faker # Импортируем класс Faker из установленной библиотеки
from selenium.webdriver.common.by import By
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.remote.webelement import WebElement


class Base(): # Базовый класс в котором хранится драйвер, он будет родительским, для всех наших последующих страниц Pages
    """ Базовый класс, содержащий универсальные методы """ # Класс будет содержать универсальные методы, которые будут использоваться в классах наследниках.

    def __init__(self, driver): # Передает драйвер который хранит экземпляр драйвера chrome
        self.driver = driver
        self.url = 'https://www.saucedemo.com/'  # Обращение к URL из той страницы на которой она находится (Используется по дефолту без set_up)
        self.fake = Faker( "ru_Ru")  # Создаём экземпляр класса Faker, указывая, что хотим генерировать данные на (ru_Ru - русский язык)

    """ Метод, вывода в консоль текущего URL """
    # Метод вызывается в классе наследнике
    def get_current_url(self):
        """Метод вывода url в консоль"""
        get_url = self.driver.current_url # Переменная которая получает url в текущей сессии
        print(f"Перешел на страницу {get_url} ") # Вывод значения переменной


    """ Метод, проверки корректности текущего URL """
    def assert_url(self, result):
        """Проверка корректности URL"""
        get_url = self.driver.current_url
        print(get_url)
        assert result == get_url
        print("Корректная URL")


    """ Метод, проверки значения текста элемента на странице """
    # Метод вызывается в классе наследнике
    def assert_word(self, actual_result, expected_result):  # word - текст элемента со страницы, который подлежит проверке (например заголовок страниц)
        value_word = actual_result.text # Сохранение в переменную текстового значения данного элемента
        assert value_word == expected_result, f'\nОжидаемый   текст: {expected_result}, \nФактический текст: {value_word}' #Операция сравнения текста
        print(f'Корректное значение {value_word} на странице')


    """ Метод, проверки title на странице """
    # Метод вызывается в классе наследнике
    def assert_title(self, expected_title):  #
        value_title = self.driver.title # Сохранение в переменную title страницы.
        assert value_title == expected_title, f'\nОжидаемый   title: {expected_title}, \nФактический title: {value_title}' # Операция сравнения title
        print(f'Корректное значение title {value_title} на странице')



    """ Метод, создание скриншота на странице """

    def get_screenshot(self, element: WebElement = None):
        """Создание скриншота"""
        timestamp = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        if element:
            # Скриншот конкретного элемента, который передан в аргументы при вызове.
            screenshot_name = f"element_screenshot_{timestamp}.png"
            element.screenshot(f"/Users/unregistreduser/PycharmProjects/PageObjectsModel/Screen/{screenshot_name}")
            print(f"Скриншот элемента выполнен")
        else:
            # Скриншот всей страницы, если в аргументы при вызове ничего не передано.
            screenshot_name = "screenshot " + timestamp + ".png"
            self.driver.save_screenshot(f"/Users/unregistreduser/PycharmProjects/PageObjectsModel/Screen/{screenshot_name}")
            print(f"Скриншот страницы выполнен")






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
    #     # print('Сравнивает товары в корзине с добавленными')
    #     # print("Имена товаов совпадают" if float(
    #     #     driver.find_element(By.CLASS_NAME, "inventory_item_price").text.split('$')[
    #     #         1]) in item_price else "Имена товаров не совпадают")
    #     # print("Стоимость товаров совпадает" if float(
    #     #     driver.find_element(By.CLASS_NAME, "inventory_item_price").text.split('$')[
    #     #         1]) in item_price else "Стоимость товаров не совпадает")
    #     #
    #
    #     #
    #     # print('Переходит к подтверждению заказа')
    #     # button_continue = driver.find_element(By.ID, "continue").click()
    #     # print('Убеждается, что переход к подтверждению заказа выполнен')
    #     # assert driver.find_element(By.CSS_SELECTOR,
    #     #                            '[class="cart_quantity_label"]').text == 'QTY', f'Переход на сраниу с подтверждению заказа не выполнен'
    #     # time.sleep(2)


    #     # print('Сравнивает товары в корзине с добавленными')
    #     # print("Имена товаов совпадают" if float(
    #     #     driver.find_element(By.CLASS_NAME, "inventory_item_price").text.split('$')[
    #     #         1]) in item_price else "Имена товаров не совпадают")
    #     # print("Стоимость товаров совпадает" if float(
    #     #     driver.find_element(By.CLASS_NAME, "inventory_item_price").text.split('$')[
    #     #         1]) in item_price else "Стоимость товаров не совпадает")
    #     #
    #     # print('Убеждается, что сумма товаров корректна')
    #     # assert sum(item_price) == float(
    #     #     driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text.split('$')[1]), f'Сумма товаров не корректна'
    #     # print(f'{sum(item_price)}')
    #     # time.sleep(5)
    #     #
    #     # print('находит и нажимает кнопку "Finish" для завершения заказа')
    #     # button_finish = driver.find_element(By.ID, "finish").click()
    #     #
    #     # print('Убеждается, что форма отправлена успешно')
    #     # assert self.driver.find_element(By.CLASS_NAME,'complete-header').text == 'Thank you for your order!', f'Ошибка: форма не отправлена, не найден элемнт с подтверждающим текстом или текст был изменен'
    #     # time.sleep(2)
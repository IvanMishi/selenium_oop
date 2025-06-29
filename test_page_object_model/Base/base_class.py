import datetime

class Base(): # Базовый класс в котором хранится драйвер, он будет родительским, для всех наших последующих страниц Pages
    """ Базовый класс, содержащий универсальные методы """ # Класс будет содержать универсальные методы, которые будут использоваться в классах наследниках.

    def __init__(self, driver): # Передает драйвер который хранит экземпляр драйвера chrome
        self.driver = driver
        self.url = 'https://www.saucedemo.com/'  # Обращение к URL из той страницы на которой она находится (Используется по дефолту без set_up)

    """ Метод, проверки текущего URL """
    # Метод вызывается в классе LoginPage
    def get_current_url(self):
        """Метод проверки url"""
        get_url = self.driver.current_url # Переменная которая получает url в текущей сессии
        print(f"Перешел на страницу {get_url} ") # Вывод значения переменной

    """ Метод, проверки значения текста на странице """
    # Метод вызывается в классе LoginPage
    def assert_word(self, word, result):  # Word - элемент со страницы, который подлежит проверке (например заголовок страниц)
        value_word = word.text # Сохранение в переменную значения данного элемента
        assert value_word == result #Операция сравнения текста с результатом
        print(f'Корректное значение {value_word}')

    """ Метод, создание скриншота на странице """
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%H.%M.%S-%Y.%m.%d")
        name_screenshot = "screenshot " + now_date + ".png"
        self.driver.find_element(By.ID, "this_pic").screenshot('Screen/' + name_screenshot)

    def assert_url(self, result):
        """Проверка корректности URL"""
        get_url = self.driver.current_url
        print(get_url)
        assert result == get_url
        print("Корректная URL")



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
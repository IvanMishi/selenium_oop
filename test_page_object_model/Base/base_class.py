import datetime


class Base(): # Базовый класс в котором хранится драйвер, он будет родительским, для всех наших последующих страниц Pages
    # Класс будет содержать универсальные методы, которые будут использоваться в классах наследниках.
    """ Базовый класс, содержащий универсальные методы """

    def __init__(self, driver): # Передает драйвер который хранит экземпляр драйвера chrome
        self.driver = driver
        self.url = 'https://www.saucedemo.com/'  # Обращение к URL из той страницы на которой она находится


    """ Метод, проверки текущего URL """
    # Метод вызывается в классе LoginPage
    def get_current_url(self):
        get_url = self.driver.current_url # Переменная которая получает url в текущей сессии
        print(f'Переходит по ссылке {get_url}') # Вывод значения переменной
        print('Убеждается, что URL корректный.')
        assert self.url == self.driver.current_url, f'Ожидаемый URL: {self.url}, Фактический URL: {self.driver.current_url}'


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
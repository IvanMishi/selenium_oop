


class Base(): # Базовый класс в котором хранится драйвер он будет родительским, для всех наших последующих страниц Pages и будет содержать универсальные методы, которые мы будем в них использовать.
    """ Базовый класс, содержащий универсальные методы """

    def __init__(self, driver): # Передает драйвер который хранит экземпляр драйвера chrome
        self.driver = driver
        self.url = 'https://www.saucedemo.com/'  # Обращение к URL из той страницы на которой она находится

    """ Метод, проверки текущего URL """
    def get_current_url(self): # Метод вызывается в классе LoginPage
        get_url = self.driver.current_url # Переменная которая получает url в текущей сессии
        print(f'Переходит по ссылке {get_url}') # Вывод значения переменной
        print('Убеждается, что URL корректный.')
        assert self.url == self.driver.current_url, f'Ожидаемый URL: {self.url}, Фактический URL: {self.driver.current_url}'


    """ Метод, проверка по ключевому слову """
    def assert_word(self, word, result):  # Метод вызывается в классе LoginPage
        value_word = word.text # Сохранение в переменную
        assert value_word == result #Операция сравнения текста с результатом
        print(f'Корректное значение {value_word}')



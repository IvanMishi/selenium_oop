



class Base(): # Базовый класс в котором хранится драйвер он будет родительским, для всех наших последующих страниц Pages и будет содержать универсальные методы, которые мы будем в них использовать.
    """ Базовый класс, содержащий универсальные методы """

    def __init__(self, driver): # Передает драйвер который хранит экземпляр драйвера chrome
        self.driver = driver

    """ Метод, который возвращает URL """
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Переходит по ссылке {get_url}')


        # print('Ожидает загрузку страницы.')
        # WebDriverWait(self.driver, 60).until(EC.url_to_be(self.link))
        # print('Убеждается, что URL корректный.')
        # assert self.link == self.driver.current_url, f'Ожидаемый URL: {self.link}, Фактический URL: {self.driver.current_url}'
        # fake = Faker("ru_Ru")  # Создаём экземпляр класса Faker, указывая, что хотим генерировать данные на (ru_Ru - русский язык)

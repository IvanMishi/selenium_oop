

# Базовый класс в котором хранится драйвер
# Так-же в базовом классе может хранится универсальные методы которые могут быть вызваны в каждом тесте
class Base():

    def __init__(self, driver): # Передает драйвер который хранит экземпляр драйвера chrome
        self.driver = driver
        # print('Ожидает загрузку страницы.')
        # WebDriverWait(self.driver, 60).until(EC.url_to_be(self.link))
        # print('Убеждается, что URL корректный.')
        # assert self.link == self.driver.current_url, f'Ожидаемый URL: {self.link}, Фактический URL: {self.driver.current_url}'
        # fake = Faker("ru_Ru")  # Создаём экземпляр класса Faker, указывая, что хотим генерировать данные на (ru_Ru - русский язык)

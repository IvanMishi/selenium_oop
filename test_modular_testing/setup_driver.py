class Setup_driver():
    def setup_driver(self):
    """Метод создает экземпляр драйвера и открывает браузер по требуемой URL."""
    self.driver = webdriver.Chrome()
    self.link = 'https://www.saucedemo.com/'
    self.driver.get(self.link)  # Переходит по указанной ссылке.
    print('Ожидает загрузку страницы.')
    WebDriverWait(self.driver, 60).until(EC.url_to_be(self.link))
    print('Убеждается, что URL корректный.')
    assert self.link == self.driver.current_url, f'Ожидаемый URL: {self.link}, Фактический URL: {self.driver.current_url}'
    self.fake = Faker(
        "ru_Ru")  # Создаём экземпляр класса Faker, указывая, что хотим генерировать данные на (ru_Ru - русский язык)
    time.sleep(5)
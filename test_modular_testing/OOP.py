import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице


class TestAuthentification:  # Общий класс, который будет содержать методы для работы в данном тесте.
    """Класс включающий сценарий о проверке авторизации в системе"""

    def setup_driver(self):
        """Создает экземпляр драйвера и открывает браузер по требуемой URL."""
        self.driver = webdriver.Chrome()
        self.link = 'https://www.saucedemo.com/'
        self.driver.get(self.link)  # Переходит по указанной ссылке.
        time.sleep(1)  # Ожидает загрузки страницы.

    def close_driver(self):
        """Закрывает драйвер браузера."""
        self.driver.quit()

    def test_autorisation(self):
        """Тест успешной авторизации, включая проверку URL."""
        self.setup_driver()  # Инициализация драйвера и переход на страницу
        assert self.link == self.driver.current_url, f'Ожидаемый URL: {self.link}, Фактический URL: {self.driver.current_url}'
        self.test_успешная_авторизация()  # Вызов метода для успешной авторизации
        self.close_driver()  # Закрытие драйвера

    # def test_успешная_авторизация(self):
    #     """Метод для выполнения успешной авторизации."""
    #     print('Получает данные для авторизации.')
    #     # Находит на странице данные для авторизации, берет первое значение
    #     login = self.driver.find_element(By.ID, 'login_credentials').text.splitlines()[1]
    #     password = self.driver.find_element(By.CLASS_NAME, 'login_password').text.splitlines()[1]
    #     print('Логинится в системе')
    #
    #     input_username = self.driver.find_element(By.ID, "user-name").send_keys(login)
    #     input_password = self.driver.find_element(By.ID, "password").send_keys(password)
    #     button_login = self.driver.find_element(By.ID, "login-button").click()
    #
    #     print('Авторизуется успешно')
    #     time.sleep(5)
    #
    # def test_негативный_авторизация_1(self):
    #     """Тест на неуспешную авторизацию с некорректным логином."""
    #     self.setup_driver()  # Открытие браузера и переход на URL
    #     print('Проверка неуспешной авторизации с некорректным логином.')
    #     self.driver.find_element(By.ID, "user-name").send_keys('некорректный_логин')
    #     self.driver.find_element(By.ID, "password").send_keys('correct_password')
    #     self.driver.find_element(By.ID, "login-button").click()
    #
    #     # Добавьте здесь проверку на наличие ошибки (можно использовать текст ошибки на странице)
    #     # Например
    #     time.sleep(2)
    #     error_message = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Epic sadface')]").text
    #     assert "Epic sadface" in error_message, f"Ошибка ожидалась, но не была найдена. Текст ошибки: {error_message}"
    #
    #     self.close_driver()  # Закрытие браузера
    #
    # def test_негативный_авторизация_2(self):
    #     """Тест на неуспешную авторизацию с некорректным паролем."""
    #     self.setup_driver()
    #     print('Проверка неуспешной авторизации с некорректным паролем.')
    #     self.driver.find_element(By.ID, "user-name").send_keys('correct_username')
    #     self.driver.find_element(By.ID, "password").send_keys('некорректный_пароль')
    #     self.driver.find_element(By.ID, "login-button").click()
    #
    #     time.sleep(2)
    #     error_message = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Epic sadface')]").text
    #     assert "Epic sadface" in error_message, f"Ошибка ожидалась, но не была найдена. Текст ошибки: {error_message}"
    #
    #     self.close_driver()
    #
    # def test_негативный_авторизация_3(self):
    #     """Тест на неуспешную авторизацию с пустыми полями."""
    #     self.setup_driver()
    #     print('Проверка неуспешной авторизации с пустыми полями.')
    #     self.driver.find_element(By.ID, "login-button").click()  # Пытаемся войти без ввода логина и пароля
    #
    #     time.sleep(2)
    #     error_message = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Epic sadface')]").text
    #     assert "Epic sadface" in error_message, f"Ошибка ожидалась, но не была найдена. Текст ошибки: {error_message}"
    #
    #     self.close_driver()


# Создаем экземпляр класса и вызываем его методы:
start_test = TestAuthentification()
start_test.test_autorisation()  # Успешная авторизация, используя корректные данные
# start_test.test_негативный_авторизация_1()  # Неуспешная авторизация, используя некорректный логин
# start_test.test_негативный_авторизация_2()  # Неуспешная авторизация, используя некорректный пароль
# start_test.test_негативный_авторизация_3()  # Неуспешная авторизация, используя пустые поля
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class AuthTestBase:  # Абстракция: базовый класс для всех тестов
    """Базовый класс для тестов авторизации"""

    def setup_driver(self):  # Инкапсуляция: скрывает детали инициализации драйвера
        """Создает экземпляр драйвера и открывает браузер"""
        self.driver = webdriver.Chrome()
        self.link = 'https://www.saucedemo.com/'
        self.driver.get(self.link)
        time.sleep(1)

    def close_driver(self):  # Инкапсуляция: скрывает детали закрытия драйвера
        """Закрывает драйвер браузера"""
        self.driver.quit()


class PositiveAuthTest(AuthTestBase):  # Наследование: расширяет базовый класс
    """Класс для позитивных тестов авторизации"""

    def test_successful_auth(self):  # Абстракция: представляет конкретный тест-кейс
        """Тест успешной авторизации"""
        self.setup_driver()

        # Проверка URL (инкапсуляция: использование self.link)
        assert self.link == self.driver.current_url, f'Ожидаемый URL: {self.link}, Фактический URL: {self.driver.current_url}'

        # Получение учетных данных
        login = self.driver.find_element(By.ID, 'login_credentials').text.splitlines()[1]
        password = self.driver.find_element(By.CLASS_NAME, 'login_password').text.splitlines()[1]

        # Выполнение авторизации
        self.driver.find_element(By.ID, "user-name").send_keys(login)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

        print('Авторизация прошла успешно')
        time.sleep(2)

        # Проверка успешной авторизации
        assert "inventory" in self.driver.current_url, "Не удалось авторизоваться"
        self.close_driver()


class NegativeAuthTest(AuthTestBase):  # Наследование: расширяет базовый класс
    """Базовый класс для негативных тестов"""

    def _perform_auth(self, username: str, password: str):  # Инкапсуляция: внутренний метод
        """Выполняет попытку авторизации (полиморфизм: будет переиспользован)"""
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

    def _check_error(self):  # Инкапсуляция: скрывает детали проверки ошибки
        """Проверяет наличие сообщения об ошибке"""
        error_message = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Epic sadface')]").text
        assert "Epic sadface" in error_message, f"Ожидалась ошибка, но найдено: {error_message}"


class InvalidLoginTest(NegativeAuthTest):  # Наследование: специализированный тест
    """Тест авторизации с некорректным логином"""

    def test_invalid_login(self):  # Абстракция: конкретный тест-кейс
        self.setup_driver()
        self._perform_auth('некорректный_логин', 'correct_password')  # Полиморфизм: использование базового метода
        self._check_error()  # Инкапсуляция: использование внутреннего метода
        self.close_driver()


class InvalidPasswordTest(NegativeAuthTest):  # Наследование
    """Тест авторизации с некорректным паролем"""

    def test_invalid_password(self):
        self.setup_driver()
        self._perform_auth('correct_username', 'некорректный_пароль')  # Полиморфизм
        self._check_error()
        self.close_driver()


class EmptyFieldsTest(NegativeAuthTest):  # Наследование
    """Тест авторизации с пустыми полями"""

    def test_empty_fields(self):
        self.setup_driver()
        # Полиморфизм: особый случай использования базового метода
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        self._check_error()
        self.close_driver()


# Использование

# Позитивный тест
success_test = PositiveAuthTest()
success_test.test_successful_auth()

# Негативные тесты
invalid_login_test = InvalidLoginTest()
invalid_login_test.test_invalid_login()

invalid_password_test = InvalidPasswordTest()
invalid_password_test.test_invalid_password()

empty_fields_test = EmptyFieldsTest()
empty_fields_test.test_empty_fields()

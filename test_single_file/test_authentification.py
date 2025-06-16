import time
from selenium import webdriver
from selenium.webdriver.common.by import By




# ================== АБСТРАКЦИЯ ==================
# AuthTestBase - абстракция: определяет общую концепцию теста авторизации,
# выделяя существенные характеристики (настройка драйвера, получение данных)
# и игнорируя детали реализации конкретных тестов
class AuthTestBase:
    """Базовый класс для тестов авторизации"""

    # =========== ИНКАПСУЛЯЦИЯ ===========
    # Скрывает сложность инициализации драйвера
    # Метод(инструкция) инициализации драйвера - функция внутри класса	принадлежит классу
    def setup_driver(self):  # Инкапсуляция: скрывает детали настройки драйвера
        """Создает экземпляр драйвера и открывает браузер"""
        # self - ссылка на текущий экземпляр класса (объект), для которого вызван метод (инкапсуляция состояния)
        self.driver = webdriver.Chrome()  # Инкапсуляция: атрибут драйвера принадлежит созданному объекту
        self.link = 'https://www.saucedemo.com/'  # Инкапсуляция: атрибут URL принадлежит созданному объекту
        self.driver.get(self.link)  # Использование инкапсулированного атрибута - создаются как атрибуты созданного объекта, для которого вызван метод.
        time.sleep(1)  # Ожидание загрузки, временная операция не сохраняются в объекте.

    # =========== Инкапсулирует логику завершения работы ===========
    def close_driver(self):  # Метод(инструкция) закрытия драйвера - функция внутри класса	принадлежит классу.
        """Закрывает драйвер браузера"""
        self.driver.quit()  # Использование инкапсулированного атрибута driver.

    # =========== Инкапсулирует получение тестовых данных ===========
    def get_credentials(self):  # Метод для получения учетных данных
        """Возвращает корректные логин и пароль со страницы"""
        login = self.driver.find_element(By.ID, 'login_credentials').text.splitlines()[1]
        password = self.driver.find_element(By.CLASS_NAME, 'login_password').text.splitlines()[1]
        return login, password




# ================== НАСЛЕДОВАНИЕ ==================
# Класс позитивных тестов PositiveAuthTest наследует функциональность AuthTestBase (is-a relationship)
class PositiveAuthTest(AuthTestBase):  # Наследование: расширяет функциональность базового класса
    """Класс для позитивных тестов авторизации"""

    # ================== Абстракция: конкретный тест-кейс успешной авторизации ==================
    def test_successful_auth(self):   # Метод(инструкция) успешная авторизация - функция внутри класса	принадлежит классу.
        """Тест успешной авторизации"""
        # self указывает на экземпляр PositiveAuthTest
        self.setup_driver()  # Наследование: метод базового класса инициализации драйвера унаследован от AuthTestBase

        # Проверка URL
        # self.link унаследован от AuthTestBase
        assert self.link == self.driver.current_url  # Инкапсуляция: доступ к атрибутам объекта

        # Используем метод get_credentials() для получения учетных данных
        login, password = self.get_credentials()  # Получаем данные со страницы

        # Выполнение авторизации
        self.driver.find_element(By.ID, "user-name").send_keys(login)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

        print('Авторизация прошла успешно')
        time.sleep(2)

        # Проверка результата
        assert "inventory" in self.driver.current_url, "Не удалось авторизоваться"
        self.close_driver()  # Наследование: метод базового класса




# ================== НАСЛЕДОВАНИЕ + ПОЛИМОРФИЗМ ==================
# NegativeAuthTest наследует от AuthTestBase и расширяет функциональность
class NegativeAuthTest(AuthTestBase):  # Наследование: специализирует базовый класс для негативных сценариев
    """Базовый класс для негативных тестов"""

    # =========== ИНКАПСУЛЯЦИЯ ===========
    # Защищенный метод (реализация скрыта от внешнего использования)
    def _perform_auth(self, username: str, password: str):  # Инкапсуляция: внутренняя реализация
        """Выполняет попытку авторизации"""
        # self указывает на экземпляр NegativeAuthTest или его потомков
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

    # Защищенный метод проверки ошибки (детали проверки скрыты)
    def _check_error(self):  # Инкапсуляция: скрывает детали проверки ошибки
        """Проверяет наличие сообщения об ошибке"""
        error_message = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Epic sadface')]").text
        assert "Epic sadface" in error_message  # Использование инкапсулированного драйвера




# ================== НАСЛЕДОВАНИЕ + ПОЛИМОРФИЗМ ==================
# Класс теста с неверным логином (наследуется от NegativeAuthTest)
class InvalidLoginTest(NegativeAuthTest):  # Наследование: расширяет функциональность для конкретного случая
    """Тест авторизации с некорректным логином"""

    # ПОЛИМОРФИЗМ: уникальная реализация теста
    def test_invalid_login(self):
        """Тест с неверным логином"""
        # self указывает на экземпляр InvalidLoginTest
        self.setup_driver()  # Наследование: метод из AuthTestBase


        # Наследование: метод из AuthTestBase
        # Получаем корректные учетные данные со страницы
        login, password  = self.get_credentials()  # Используем только логин

        # ПОЛИМОРФИЗМ: использование метода родителя с измененными параметрами
        self._perform_auth('некорректный_логин', password)  # Наследование: защищенный метод

        self._check_error()  # Наследование: защищенный метод
        self.close_driver()  # Наследование: метод из AuthTestBase




# ================== НАСЛЕДОВАНИЕ  ==================
# Класс теста с неверным паролем (наследуется от NegativeAuthTest)
class InvalidPasswordTest(NegativeAuthTest):  # Наследование
    """Тест авторизации с некорректным паролем"""

    def test_invalid_password(self):  # Полиморфизм: уникальная реализация теста
        self.setup_driver()
        # Получаем корректные учетные данные со страницы
        login, password = self.get_credentials()  # Используем только пароль

        # Полиморфизм: использование метода родителя с другими параметрами
        self._perform_auth(login, 'некорректный_пароль')
        self._check_error() # Наследование: защищенный метод
        self.close_driver() # Наследование: метод из AuthTestBase




# ================== НАСЛЕДОВАНИЕ  ==================
# Класс теста с пустыми полями (наследуется от NegativeAuthTest)
class EmptyFieldsTest(NegativeAuthTest):  # Наследование
    """Тест авторизации с пустыми полями"""

    # ПОЛИМОРФИЗМ: особое поведение (переопределение стандартного сценария)
    def test_empty_fields(self):  # Полиморфизм: переопределение поведения
        """Особый случай негативного теста"""
        self.setup_driver()
        # Полиморфизм: особый вариант авторизации (без ввода данных)
        self.driver.find_element(By.ID, "login-button").click()  # Прямой вызов без _perform_auth
        time.sleep(2)
        self._check_error()  # Наследование: защищенный метод
        self.close_driver()  # Наследование: метод из AuthTestBase



# ======== ИСПОЛНЯЕМЫЙ КОД: СОЗДАНИЕ ОБЪЕКТОВ И ВЫЗОВ МЕТОДОВ ========

# 1. СОЗДАНИЕ ОБЪЕКТА И ВЫЗОВ МЕТОДА (ПОЗИТИВНЫЙ ТЕСТ)
# Создание объекта экземпляра класса PositiveAuthTest на основании Конструктора (Создаётся пустой объект в памяти Python автоматически вызывает конструктор (если бы он был определён))
success_test = PositiveAuthTest()
# Вызов публичного метода, Python преобразует этот вызов в PositiveAuthTest.test_successful_auth(success_test)
# первым аргументом автоматически передаётся сам объект (success_test) как self
# Когда мы вызываем метод для объекта, все операции с self. внутри этого метода применяются именно к этому конкретному объекту.
success_test.test_successful_auth()



# 2. НЕГАТИВНЫЕ ТЕСТЫ
# Инкапсуляция: каждый объект имеет собственное состояние
invalid_login_test = InvalidLoginTest()  # Создание объекта
# Наследование: объект имеет методы NegativeAuthTest и AuthTestBase
invalid_login_test.test_invalid_login()  # Вызов метода (self = invalid_login_test)

invalid_password_test = InvalidPasswordTest()  # Создание объекта
invalid_password_test.test_invalid_password()  # Вызов метода

empty_fields_test = EmptyFieldsTest()  # Создание объекта
empty_fields_test.test_empty_fields()  # Вызов метода
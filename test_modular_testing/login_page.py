import time  # Импорт модуля для работы со временем (паузы, задержки)
from selenium.webdriver.common.by import By  # Импорт класса для указания способов поиска элементов (ID, CLASS_NAME и т.д.)
from selenium.webdriver.support.ui import WebDriverWait  # Импорт класса для реализации явных ожиданий
from selenium.webdriver.support import expected_conditions as EC  # Импорт набора предопределенных условий для ожидания
from selenium.common.exceptions import NoSuchElementException  # Импорт исключения для обработки отсутствия элементов


class LoginPage:
    """Класс, описывающий страницу авторизации и её функциональность."""

    def __init__(self, driver):  # Конструктор класса
        self.driver = driver  # Инициализация экземпляра веб-драйвера

    def authorization(self, user):
        """Метод выполнения процедуры авторизации."""

        print('Незарегистрированный пользователь авторизуется в системе')
        print('Вводит имя пользователя')
        # Ожидает 10 секунд до появления элемента с ID "user-name"
        input_username = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))
        input_username.send_keys(user.username)  # Ввод логина из объекта пользователя

        print('Вводит пароль')
        # Ожидает 10 секунд до появления элемента с ID "password"
        input_password = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
        input_password.send_keys(user.password)  # Ввод пароля из объекта пользователя

        print('Нажимает кнопку отправки формы авторизации')
        # Ожидает 10 секунд до кликабельности кнопки с ID "login-button"
        button_login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))
        button_login.click()  # Выполнение клика


        # Проверка результата авторизации
        try:
            # Поиск элемента с классом 'title' (заголовок страницы)
            title_element = self.driver.find_element(By.CLASS_NAME, 'title')
            # Проверка двух условий: элемент отображается И текст соответствует 'Products'
            if title_element.is_displayed() and title_element.text == 'Products':
                print('Авторизация прошла успешно')
                return True  # Успешная авторизация
        except NoSuchElementException:  # Обработка случая, когда элемент не найден
            # Проверка наличия элемента ошибки (кнопка закрытия ошибки)
            if self.driver.find_element(By.CLASS_NAME, 'error-button').is_displayed():
                print('Авторизация не выполнена — неверное имя пользователя или пароль')
                return False  # Авторизация не выполнена
import time
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями
from selenium.common.exceptions import NoSuchElementException


class LoginPage:
    """Метод для авторизации на сайте."""
    def __init__(self, driver):  # Передает драйвер как параметр
        self.driver = driver  # Инициализирует драйвер

    def authorization(self, user):
        """Метод для авторизации на сайте."""
        print('Незарегистрированный пользователь авторизуется в системе')
        print('Вводит имя пользователя')
        input_username = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))
        input_username.send_keys(user.username)
        print('Вводит пароль')
        input_password = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
        input_password.send_keys(user.password)
        print('Нажимает кнопку отправки формы авторизации')
        button_login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))
        button_login.click()
        time.sleep(2)
        # Проверяет успешность авторизации.
        try:
            # Если элемент найден, то переход на страницу сайта выполнил
            if self.driver.find_element(By.CLASS_NAME, 'title').is_displayed() and self.driver.find_element(By.CLASS_NAME, 'title').text == 'Products':
                print('Авторизация прошла успешно')
                return True
        except NoSuchElementException:
            # Если появился элемент оповещающий об ошибке, то авторизация не пройдена
            if self.driver.find_element(By.CLASS_NAME, 'error-button').is_displayed():
                print('Авторизация не выполнена — неверное имя пользователя или пароль')
                return False
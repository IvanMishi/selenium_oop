import time

from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями

class LoginPage:
    def __init__(self, driver):  # Передаем драйвер как параметр
        self.driver = driver  # Инициализируем драйвер

    def authorization(self, user):  # Метод для выполнения авторизации
        """Метод для авторизации на сайте."""
        try:
            print('Логинится в системе')
            # Вводим имя пользователя
            input_username = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))
            input_username.send_keys(user.username)
            # Вводим пароль
            input_password = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
            input_password.send_keys(user.password)
            # Кликаем по кнопке логина
            button_login = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))
            button_login.click()
            time.sleep(2)

            if self.driver.find_element(By.CLASS_NAME, 'title').text == 'Products':
                print('Авторизация прошла успешно')
            elif self.driver.find_element(By.CLASS_NAME, 'error-button').is_displayed():
                print('Авторизация не выполнена')



            # Дополнительные проверки или действия после успешного входа могут быть добавлены здесь
        except Exception as e:
            print(f'Произошла ошибка при авторизации: {e}')
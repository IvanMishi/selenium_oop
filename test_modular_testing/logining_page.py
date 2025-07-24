import time  # Импорт модуля времени
from selenium.webdriver.common.by import By  # Импорт стратегий поиска
from selenium.webdriver.support.ui import WebDriverWait  # Импорт явного ожидания
from selenium.webdriver.support import expected_conditions as EC  # Импорт условий ожидания
from selenium.common.exceptions import NoSuchElementException  # Импорт исключения

class LoginPage:  # Класс страницы авторизации
    def __init__(self, driver):  # Конструктор класса.
        self.driver = driver # Сохраняет экземпляр драйвера.

    def authorization(self, user):  # Абстрактный интерфейс, метод авторизации
	# Скрывает:
        # - Локаторы элементов
        # - Ожидания
        # - Обработку ошибок
 
	
        print(f'Авторизация {user.username} пользователя')
	# Инкапсуляция логики авторизации - детали скрыты.
        try:
            # Ожидает и очищает поле логина.
            username_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "user-name"))). 
            username_field.clear() 
            username_field.send_keys(user.username) 

            # Ожидает и очищает поле пароля.
            password_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "password"))) 
            password_field.clear() 
            password_field.send_keys(user.password) 

            # Нажимает на кнопку входа.
            login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button"))) 
            login_button.click() 
            time.sleep(1)  # Пауза после авторизации

            # Убеждается в успешной авторизации
            try:
                title_element = self.driver.find_element(By.CLASS_NAME, 'title')
                if title_element.is_displayed() and title_element.text == 'Products':
                    print('Авторизация прошла успешно')
                    return True
            except NoSuchElementException:
                pass  # Элемент не найден

            # Проверка ошибки авторизации
            if self.driver.find_element(By.CLASS_NAME, 'error-button').is_displayed():
                print('Ошибка авторизации: неверные данные')
                return False

        except Exception as e:  # Обработка исключений
            print(f'Ошибка при авторизации: {str(e)}')
            return False
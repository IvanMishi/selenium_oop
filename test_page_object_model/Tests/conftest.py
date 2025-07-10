import time
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.support.ui import WebDriverWait  # Импорт явного ожидания
from selenium.webdriver.support import expected_conditions as EC  # Импорт условий ожидания

import pytest


@pytest.fixture()
def set_up(): # Передается в аргументы при запуске теста.
    print("\nЗапуск фикстуры до выполнения теста")    #перед тестом
    driver = webdriver.Chrome()
    url = 'https://www.saucedemo.com/'  # Обращение к URL из той страницы на которой она находится
    driver.get(url)
    WebDriverWait(driver, 60).until(EC.url_to_be(url)) # Ждет загрузку сайта
    driver.maximize_window() # Указывает на локатор вне метода через self.
    time.sleep(5)

    yield driver    # Разделяет код на до/после теста

    print("\nТест завершен, запуск фикстуры после выполнения теста!")    #после теста
    driver.quit()
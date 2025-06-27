import time

import pytest
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами

@pytest.fixture()
def set_up(): # Передается в аргументы при запуске теста.
    print("\nЗапуск фикстуры до выполнения теста")    #перед тестом
    driver = webdriver.Chrome()
    url = 'https://www.saucedemo.com/'  # Обращение к URL из той страницы на которой она находится
    driver.get(url)
    time.sleep(5)

    yield driver    # Разделяет код на до/после теста

    print("\nТест завершен, запуск фикстуры после выполнения теста!")    #после теста
    driver.quit()
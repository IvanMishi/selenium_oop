import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами

import pytest
from Pages.login_page import LoginPage
from Pages.main_page import MainPage
from Pages.cart_page import CartPage
from Pages.client_Info_page import ClientInfoPage
from Pages.finish_page import FinishPage
from Pages.payment_page import PaymentPage
from Tests.conftest import set_up

# Для запуска всех тестов из директории Tests использует python -m pytest -s -v
# Для запуска теста из директории Tests использует python -m pytest -s -v test_buy_products.py
# Для запуска тестового метода из теста test_buy_products.py из директории Tests использует python -m pytest -s -v -k test_buy_products_1

@pytest.mark.run(order=3) # Фикстура: Маркировка очередности запуска теста  ((Запустится третьим))
def test_buy_products_1(set_up): # Тест выбора продукта по сценарию в тестовом методе и покупки его
    print('Тест выбора и покупки продукта 1 запущен')
    # driver = webdriver.Chrome() # Запускает драйвер по дефолту
    driver = set_up # Запускает драйвер через conftest, фикстура передаётся как аргумент
    # Тест авторизации на сайте на странице login_page
    login_page = LoginPage(driver) # Создает экземпляр родительского класса
    login_page.authorization_user() # Вызывает его метод
    time.sleep(3)
    # Тест выбора товара на странице main_page и добавления в корзину
    main_page = MainPage(driver) # Создает экземпляр родительского класса
    main_page.select_products_to_cart_1() # Вызывает его метод
    time.sleep(3)
    # Тест подтверждения товаров в корзине на странице cart_page
    cart_page = CartPage(driver) # Создает экземпляр родительского класса
    cart_page.product_confirmation() # Вызывает его метод
    time.sleep(3)
    # Тест заполнения данными о клиенте
    client_info_page = ClientInfoPage(driver) # Создает экземпляр родительского класса
    client_info_page.input_client_information() # Вызывает его метод
    time.sleep(3)
    # Тест подтверждения оплаты
    payment_page = PaymentPage(driver) # Создает экземпляр родительского класса
    payment_page.click_button_finish()# Вызывает отдельную функцию из метода
    time.sleep(3)
    # Тест скриншот
    finish_page = FinishPage(driver) # Создает экземпляр родительского класса
    finish_page.get_screenshot() # Вызывает отдельную функцию из метода
    print('Тест 1 завершен')
#     driver.quit() # Закрывает  браузер по дефолту

@pytest.mark.run(order=2) # Фикстура: Маркировка очередности запуска теста Фикстура ((Запустится вторым))
def test_buy_products_2():
    print('Тест выбора и покупки продукта 2 запущен')
    print('здесь может быть выполнен запрос API до запуска теста')
    driver = webdriver.Chrome() # Запускает драйвер по дефолту
    # driver = set_up # Запускает драйвер через conftest, фикстура передаётся как аргумент
    # Тест авторизации на сайте на странице login_page
    login_page = LoginPage(driver)  # Создает экземпляр родительского класса
    login_page.authorization_user()  # Вызывает его метод
    time.sleep(3)
    # Тест выбора товара на странице main_page и добавления в корзину
    main_page = MainPage(driver)  # Создает экземпляр родительского класса
    main_page.select_products_to_cart_2()  # Вызывает его метод
    time.sleep(3)
    # Тест подтверждения товаров в корзине на странице cart_page
    cart_page = CartPage(driver)  # Создает экземпляр родительского класса
    cart_page.product_confirmation()  # Вызывает его метод
    time.sleep(3)
    # Тест заполнения данными о клиенте
    client_info_page = ClientInfoPage(driver)  # Создает экземпляр родительского класса
    client_info_page.input_client_information()  # Вызывает его метод
    time.sleep(3)
    # Тест подтверждения оплаты
    payment_page = PaymentPage(driver)  # Создает экземпляр родительского класса
    payment_page.click_button_finish()  # Вызывает его метод
    time.sleep(3)
    # Тест скриншот
    finish_page = FinishPage(driver)
    finish_page.get_screenshot()
    print('Тест 2 завершен')
    driver.quit() # Закрывает  браузер по дефолту

@pytest.mark.run(order=1) # Фикстура: Маркировка очередности запуска теста Фикстура ((Запустится первым))
def test_buy_products_3(set_up):
    print('Тест выбора и покупки продукта 3 запущен')
    # driver = webdriver.Chrome() # Запускает драйвер по дефолту
    driver = set_up # Запускает драйвер через conftest, фикстура передаётся как аргумент
    # Тест авторизации на сайте на странице login_page
    login_page = LoginPage(driver)  # Создает экземпляр родительского класса
    login_page.authorization_user()  # Вызывает его метод
    time.sleep(3)
    # Тест выбора товара на странице main_page и добавления в корзину
    main_page = MainPage(driver)  # Создает экземпляр родительского класса
    main_page.select_products_to_cart_3()  # Вызывает его метод
    time.sleep(3)
    # Тест подтверждения товаров в корзине на странице cart_page
    cart_page = CartPage(driver)  # Создает экземпляр родительского класса
    cart_page.product_confirmation()  # Вызывает его метод
    time.sleep(3)
    # Тест заполнения данными о клиенте
    client_info_page = ClientInfoPage(driver)  # Создает экземпляр родительского класса
    client_info_page.input_client_information()  # Вызывает его метод
    time.sleep(3)
    # Тест подтверждения оплаты
    payment_page = PaymentPage(driver)  # Создает экземпляр родительского класса
    payment_page.click_button_finish()  # Вызывает его метод
    time.sleep(3)
    # Тест скриншот
    finish_page = FinishPage(driver)
    finish_page.get_screenshot()
    print('Тест 3 завершен')
#     driver.quit() # Закрывает  браузер по дефолту


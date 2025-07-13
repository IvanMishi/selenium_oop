import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями
import pytest

# Импорт классов страниц и базового класса
from Base.base_class import Base
from Pages.cart_page import CartPage
from Pages.client_Info_page import ClientInfoPage
from Pages.finish_page import FinishPage
from Pages.login_page import LoginPage
from Pages.main_page import MainPage
from Pages.payment_page import PaymentPage
from Tests.conftest import set_up  # Импорт фикстуры из conftest



# Для запуска теста из директории Tests используйте команду:
# python -m pytest -s -v test_main_page_menu_to_link_about.py
def test_main_page_menu_to_link_about(): #Тест запускается дефолтно, без использования фикстуры conftest в параметры теста.
    """
        Тест проверяет переход по ссылке 'About' в бургер-меню после авторизации
        Шаги:
        1. Авторизация пользователя
        2. Открытие бургер-меню
        3. Переход по ссылке 'About'
        4. Проверка перехода на целевую страницу
        """

    driver = webdriver.Chrome() # Создает экземпляр драйвера.

    # Тест авторизации на сайте на странице login_page
    login_page = LoginPage(driver) # Создает экземпляр родительского класса
    login_page.authorization_user() # Вызывает его метод

    # Тест выбора бургер меню на странице main_page
    mp = MainPage(driver) # Создает экземпляр родительского класса
    mp.select_menu_about() # Вызывает его метод






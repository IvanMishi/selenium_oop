import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями
import pytest

from Base.base_class import Base
from Pages.cart_page import CartPage
from Pages.client_Info_page import ClientInfoPage
from Pages.finish_page import FinishPage
from Pages.login_page import LoginPage
from Pages.main_page import MainPage
from Pages.payment_page import PaymentPage
from Tests.conftest import set_up


# Тестовый сценарий перехода авторизованного пользователя по ссылке 'about' в 'бургер меню' на странице 'main_page'.
# для запуска теста из директории Tests использует python -m pytest -s -v test_main_page_menu_to_link_about.py
def test_main_page_menu_to_link_about(): #Тест запускается дефолтно, без использования conftest.
    driver = webdriver.Chrome()

    # Тест авторизации на сайте на странице login_page
    login_page = LoginPage(driver) # Создает экземпляр родительского класса
    login_page.authorization_user() # Вызывает его метод

    # Тест выбора бургер меню на странице main_page
    mp = MainPage(driver) # Создает экземпляр родительского класса
    mp.select_menu_about() # Вызывает его метод






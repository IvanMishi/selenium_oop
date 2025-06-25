import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами
from selenium.webdriver.common.by import By  # Модуль для определения способов поиска элементов на странице
from selenium.webdriver.support.ui import WebDriverWait  # Модуль для реализации явно-ожидаемых условий
from selenium.webdriver.support import expected_conditions as EC  # Модуль для работы с ожидаемыми условиями



import pytest

from Pages.cart_page import CartPage
from Pages.client_Info_page import ClientInfoPage
from Pages.finish_page import FinishPage
from Pages.login_page import LoginPage
from Pages.main_page import MainPage
from Pages.payment_page import PaymentPage


def test_main_page_menu_to_link_about():
    driver = webdriver.Chrome()


    # Тест авторизации на сайте
    login = LoginPage(driver) # Создает экземпляр родительского класса
    login.authorization_user() # Вызывает его метод

    # Тест выбора товаров на главной странице и добавления в корзину
    mp = MainPage(driver) # Создает экземпляр родительского класса
    mp.select_menu_about() # Вызывает его метод






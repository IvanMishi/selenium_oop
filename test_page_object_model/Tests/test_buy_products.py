import time  # Модуль для работы с функцией ожидания
from selenium import webdriver  # Модуль для взаимодействия с веб-браузерами


import pytest
from Pages.login_page import LoginPage
from Pages.main_page import MainPage
from Pages.cart_page import CartPage

from Pages.client_Info_page import ClientInfoPage
from Pages.finish_page import FinishPage


from Pages.payment_page import PaymentPage
from Tests.conftes import set_up



# @pytest.mark.run(order=3) # Маркировка очередности запуска теста Фикстура ((Запустится третьим))
def test_buy_products_1(set_up):
    print('Тест выбора и покупки продукта 1 запущен')
    # driver = webdriver.Chrome() # Запускает драйвер по дефолту
    driver = set_up # Запускает драйвер через conftest

    # Тест авторизации на сайте на странице login_page
    login_page = LoginPage(driver) # Создает экземпляр родительского класса
    login_page.authorization_user() # Вызывает его метод

    # # Тест выбора товара на странице main_page и добавления в корзину
    # main_page = MainPage(driver) # Создает экземпляр родительского класса
    # main_page.select_products_to_cart_1() # Вызывает его метод
    #
    # # Тест подтверждения товаров в корзине на странице cart_page
    # cart_page = CartPage(driver) # Создает экземпляр родительского класса
    # cart_page.product_confirmation() # Вызывает его метод
    #
    # # Тест заполнения данными о клиенте
    # client_info_page = ClientInfoPage(driver) # Создает экземпляр родительского класса
    # client_info_page.input_client_information() # Вызывает его метод


#     # # Тест подтверждения оплаты
#     # pp = PaymentPage(driver)
#     # pp.click_button_finish()
#     #
#     # # Тест скриншот
#     # fp = FinishPage(driver)
#     # fp.get_screenshot()
#
#     print('Тест 1 завершен')
#     driver.quit()
#

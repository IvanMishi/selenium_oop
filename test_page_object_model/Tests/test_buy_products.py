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


def test_buy_products():
    driver = webdriver.Chrome()


    # Тест авторизации на сайте
    login = LoginPage(driver) # Создает экземпляр родительского класса
    login.authorization_user() # Вызывает его метод

    # Тест выбора товаров на главной странице и добавления в корзину
    mp = MainPage(driver) # Создает экземпляр родительского класса
    mp.click_item_list_product() # Вызывает его метод

    # Тест подтверждения товаров в корзине
    cp = CartPage(driver) # Создает экземпляр родительского класса
    cp.product_confirmation() # Вызывает его метод

    # Тест заполнения данными о клиенте
    cip = ClientInfoPage(driver) # Создает экземпляр родительского класса
    cip.input_client_information() # Вызывает его метод

    # Тест подтверждения оплаты
    pp = PaymentPage(driver)
    pp.click_button_finish()

    # Тест скриншот
    fp = FinishPage(driver)
    fp.get_screenshot()








    #
    # print('Сравнивает товары в корзине с добавленными')
    # print("Имена товаов совпадают" if float(
    #     driver.find_element(By.CLASS_NAME, "inventory_item_price").text.split('$')[
    #         1]) in item_price else "Имена товаров не совпадают")
    # print("Стоимость товаров совпадает" if float(
    #     driver.find_element(By.CLASS_NAME, "inventory_item_price").text.split('$')[
    #         1]) in item_price else "Стоимость товаров не совпадает")
    #

    #
    # print('Переходит к подтверждению заказа')
    # button_continue = driver.find_element(By.ID, "continue").click()
    # print('Убеждается, что переход к подтверждению заказа выполнен')
    # assert driver.find_element(By.CSS_SELECTOR,
    #                            '[class="cart_quantity_label"]').text == 'QTY', f'Переход на сраниу с подтверждению заказа не выполнен'
    # time.sleep(2)
    #
    # print('Сравнивает товары в корзине с добавленными')
    # print("Имена товаов совпадают" if float(
    #     driver.find_element(By.CLASS_NAME, "inventory_item_price").text.split('$')[
    #         1]) in item_price else "Имена товаров не совпадают")
    # print("Стоимость товаров совпадает" if float(
    #     driver.find_element(By.CLASS_NAME, "inventory_item_price").text.split('$')[
    #         1]) in item_price else "Стоимость товаров не совпадает")
    #
    # print('Убеждается, что сумма товаров корректна')
    # assert sum(item_price) == float(
    #     driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text.split('$')[1]), f'Сумма товаров не корректна'
    # print(f'{sum(item_price)}')
    # time.sleep(5)
    #
    # print('находит и нажимает кнопку "Finish" для завершения заказа')
    # button_finish = driver.find_element(By.ID, "finish").click()
    #
    # print('Убеждается, что форма отправлена успешно')
    # assert self.driver.find_element(By.CLASS_NAME,'complete-header').text == 'Thank you for your order!', f'Ошибка: форма не отправлена, не найден элемнт с подтверждающим текстом или текст был изменен'
    # time.sleep(2)

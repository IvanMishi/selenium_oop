# Single-file test(Тест в одном файле):

## test_authentification
[AuthTestBase]  (Базовый класс)
       △
       |
+------+------+
|             |
[PositiveAuthTest]   [NegativeAuthTest]  (Абстрактные классы)
       △                   △
       |                   |
+------+------+      +-----+-----+
|             |      |           |
[SuccessTest]        [InvalidLoginTest]  [InvalidPasswordTest]  [EmptyFieldsTest]  (Конкретные тест-кейсы)
### Абстракция
Создан класс TestAuthentification, который абстрагирует процесс тестирования авторизации. 
Методы класса (test_autorisation, test_успешная_авторизация и др.) инкапсулируют логику тестов, скрывая детали реализации.

### Инкапсуляция
Атрибуты класса (driver, link) и методы объединены в единую сущность.
- (private): Атрибуты driver и link принадлежат экземпляру класса (доступ через self).
Внутренние методы (напр. setup_driver(), close_driver()) используются только внутри класса.
Данные (веб-драйвер, URL) защищены областью видимости объекта (self).
+ (public): Все методы публичны и вызываются извне (напр. start_test.test_autorisation()).

### Наследование
Прямое наследование отсутствует (класс не наследует другие классы), но неявно используется наследование от object (стандартно в Python).
Можно  унаследовать класс от unittest.TestCase для интеграции с фреймворком.
### Полиморфизм
Явно не реализован. Отсутствует переопределение методов или работа с интерфейсами.
Можно  реализовать общий метод для негативных тестов, принимающий параметры (логин/пароль).
class User:  # Класс пользователей
    def __init__(self, username, password='secret_sauce'):  # Конструктор
        self.username = username # Инициализация логина
        self.password = password # Инициализация пароля (значение по умолчанию)

# Список тестовых пользователей
users = [
    User(username='standard_user'),      # Стандартный
    User(username='locked_out_user'),    # Заблокированный
    User(username='problem_user'),       # Проблемный
    User(username='performance_glitch_user')  # С замедлениями
]
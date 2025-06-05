class User:
    """
    Класс для представления пользователя системы.
    Хранит учетные данные: имя пользователя и пароль.
    """
    def __init__(self, username, password):
        # Инициализация объекта пользователя
        self.username = username  # Логин пользователя
        self.password = password  # Пароль пользователя

# Создание тестовых пользователей с разными характеристиками:

# Стандартный пользователь с валидными данными
standard_user = User(username='standard_user', password='secret_sauce')

# Заблокированный в системе пользователь
locked_out_user = User(username='locked_out_user', password='secret_sauce')

# Пользователь с проблемными данными (специфичные баги)
problem_user = User(username='problem_user', password='secret_sauce')

# Пользователь с задержками отклика системы
performance_glitch_user = User(username='performance_glitch_user', password='secret_sauce')

# Пользователь с ошибками визуализации
error_user = User(username='error_user', password='secret_sauce')

# Пользователь для тестирования визуальных элементов
visual_user = User(username='visual_user', password='secret_sauce')
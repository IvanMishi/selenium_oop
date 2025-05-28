class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


# Определение пользователей
standard_user = User(username='standard_user', password='secret_sauce')
locked_out_user = User(username='locked_out_user', password='secret_sauce')
problem_user = User(username='problem_user', password='secret_sauce')
performance_glitch_user = User(username='performance_glitch_user', password='secret_sauce')
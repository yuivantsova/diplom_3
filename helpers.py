import random
import string

import allure


@allure.step('Получение email')
def generator_email(self):
    return f'{self.generator_str()}@ya.ru'

@allure.step('Получение рандомной строки')
def generator_str(self):
    characters = string.ascii_letters + string.ascii_lowercase
    random_str = ''.join(random.choice(characters) for _ in range(5))
    return random_str

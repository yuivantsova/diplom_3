from selenium.webdriver.common.by import By


class LoginPageLocators:

    INPUT_EMAIL = (By.XPATH, '//input[@name = "name"]')  # Поле ввода E-mail
    INPUT_PASS = (By.XPATH, '//input[@name = "Пароль"]')  # Поле ввода Пароля
    BUTTON_ENTER = (By.XPATH, '//button[contains(text(),"Войти")]')  # Кнопка Входа
    BUTTON_RECOVER_PASSWORD = (By.LINK_TEXT, 'Восстановить пароль')  # Кнопка "Восстановить пароль"

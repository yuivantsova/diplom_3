from selenium.webdriver.common.by import By


class RecoverPageLocators:

    INPUT_EMAIL = (By.XPATH, '//input[@name="name"]')  # Поле ввода Email
    BUTTON_RECOVER = (By.XPATH, '//button[contains (text(), "Восстановить")]')  # Кнопка восстановить
    INPUT_NEW_PASSWORD = (By.XPATH, '//input[@name="Введите новый пароль"]')  # ввод нового пароля
    BUTTON_VISIBILITY = (By.XPATH, '//div[contains(@class, "icon")]')  # Кнопка видимости пароля
    FIELD_NEW_PASSWORD = (By.XPATH, '//input[@name="Введите новый пароль"]/parent::div')  # Поле ввода нового пароля
    HEADER_PAGE = (By.XPATH, '//h2[contains(text(), "Восстановление пароля")]') # Заголовок страницы Востановления пароля
    BUTTON_SAVE = (By.XPATH, '//button[contains (text(), "Сохранить")]') # Кнопка Сохранить
from selenium.webdriver.common.by import By


class PersonalPageLocators:

    BUTTON_HISTORY_ORDER = (By.XPATH, '//a[@href="/account/order-history"]')  # Кнопка истории заказов
    ID_ORDER = (By.XPATH, '//div[contains(@class, "textBox")]/p[contains(@class, "digits")]')  # в чем разница если в этом пути указать child вот так: //div[contains(@class, "textBox")]/child::p[contains(@class, "digits")]
    BUTTON_EXIT = (By.XPATH, '//button[contains(text(), "Выход")]')  # Кнопка выхода
    INPUT_PASS_CHANGE = (By.XPATH, '//input[@type = "password"]')   # Поле изменения пароля


from selenium.webdriver.common.by import By


class HeaderLocators:

    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[contains(text(), 'Конструктор')]")  # Кнопка "Конструктор"
    BUTTON_ORDER_FEED = (By.XPATH, "//a[@href='/feed']")  # Кнопка "Лента заказов"
    BUTTON_MY_ACCOUNT = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")  # Кнопка "Личный кабинет"
from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    HEADER_ORDER_FEED_PAGE = (By.XPATH, '//h1[text()="Лента заказов"]')  # Заголовок страницы "Лента заказов"
    PATTERN_ORDER_BOX = (By.XPATH, '//p[contains(text(), "#0")]')  # Блок заказа на станице "Лента заказов"
    ORDER_BOX = (By.XPATH, '//div[contains(@class, orderBox)]')  # Всплывающее окно заказа
    TEXT_IN_ORDER_BOX = (By.XPATH, '//p[text() = "Cостав"]') # Проверочный текст в всплывающем окне заказа
    PROGRESS_BLOCK = (By.XPATH, '//ul[contains(@class,"orderListReady")]/li') # блок в "В работе"
    COUNT_ALL_TIME = (By.XPATH, '//p[contains(text(), "Выполнено за все время")]/following-sibling::p')  # счетчик заказы за все время
    COUNT_TODAY = (By.XPATH, '//p[contains(text(), "Выполнено за сегодня")]/following-sibling::p') # Счетчик заказов за сегодня
    ORDER_PROGRESS = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[1]/ul[2]/li[contains(text(), "0")]') # заказы в работе



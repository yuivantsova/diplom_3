from selenium.webdriver.common.by import By


class MainPageLocators:

    HEADER_ORDER_FEED_PAGE = (By.XPATH, '//h1[text()="Лента заказов"]')  # Заголовок страницы "Лента заказов"
    HEADER_CONSTRUCTOR_PAGE = (By.XPATH, '//h1[text()="Соберите бургер"]') # Заголовок вкладки Контруктор
    BUN_FL = (By.XPATH, '//p[contains(text(), "Флюоресцентная булка R2-D3")]') # Название игредиента Флюоресцентная булка R2-D3
    HEADER_INGR_BOX = (By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]") # Заголовок в всплывающем окне ингредиентов
    BUTTON_CROSS = (By.XPATH, '//button[contains(@class, "close")]') # кнопка закрытия всплывающего окна ингредиентов
    SOURCE = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]') # ингредиент Флюоресцунтной булки (то что перетаскиваем)
    TARGET = (By.XPATH, '//section[contains(@class, basket)]/ul[contains(@class, basket)]') # Корзина (цель куда нужно перетянуть ингредиент)
    COUNT = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]/div[1]/p[contains(@class, num)]') # счетчик добавления ингредиента в корзину
    BUTTON_CREATE_ORDER = (By.XPATH, '//button[contains(text(),"Оформить заказ")]') # Кнопка оформления заказа
    TEXT_SUCCESS_ORDER = (By.XPATH, '//p[contains(text(), "идентификатор заказа")]') # Идентификатор заказа, признак успешно созданного заказа
    ID_ORDER = (By.XPATH, '//div/div[contains(@class, contentBox)]/h2[contains(@class, large)]')

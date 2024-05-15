from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.header_locators import *
from locators.main_page_locators import *
import allure


class MainPage(BasePage):

    @allure.step('Нажать на кнопку Личный кабинет')
    def click_button_personal_area(self):
        self.click_virt_mouse(HeaderLocators.BUTTON_MY_ACCOUNT)

    @allure.step('Нажать на кнопку Конструктор')
    def click_constructor_button(self):
        self.click_element(HeaderLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Нажать на кнопку Лента заказов')
    def click_order_feed_button(self):
        self.click_virt_mouse(HeaderLocators.BUTTON_ORDER_FEED)

    @allure.step('Заголовок вкладки Ленты заказов')
    def return_text_header_order_feed(self):
        return self.get_text_to_element(MainPageLocators.HEADER_ORDER_FEED_PAGE)

    @allure.step('Заголовок вкладки Конструктор')
    def return_text_header_constructor(self):
        return self.get_text_to_element(MainPageLocators.HEADER_CONSTRUCTOR_PAGE)

    @allure.step('Нажать на ингредиент')
    def click_ingredient(self):
        self.click_element(MainPageLocators.BUN_FL)

    @allure.step('Заголовок бокса про ингредиент')
    def return_header_ingr_box(self):
        return self.get_text_to_element(MainPageLocators.HEADER_INGR_BOX)

    @allure.step('Закрыть всплывающее окно')
    def click_close_button(self):
        WebDriverWait(self.driver,20).until(expected_conditions.visibility_of_element_located(MainPageLocators.BUTTON_CROSS))
        self.click_element(MainPageLocators.BUTTON_CROSS)
        return self.return_text_header_constructor()

    @allure.step('Перетаскивание ингредиента в корзину')
    def move_ingredients(self):
        self.scroll_to_bun()
        self.move_element(MainPageLocators.SOURCE, MainPageLocators.TARGET)

    @allure.step('Получить количество ингредиента в заказе')
    def get_count(self):
        return self.get_text_to_element(MainPageLocators.COUNT)

    @allure.step('Пролистать до Ингредиента')
    def scroll_to_bun(self):
        self.scroll_to_element(MainPageLocators.TARGET)

    @allure.step('Нажать на кнопку и вернуть текст успешного заказа')
    def click_create_button_and_return_text(self):
        self.click_element(MainPageLocators.BUTTON_CREATE_ORDER)
        return self.get_text_to_element(MainPageLocators.TEXT_SUCCESS_ORDER)




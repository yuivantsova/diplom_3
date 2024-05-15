from pages.base_page import BasePage
import allure
from locators.main_page_locators import *
from locators.order_feed_page_locators import *
from locators.header_locators import *


class OrderFeedPage(BasePage):

    @allure.step('Нажать на кнопку Лента заказов в хедере')
    def click_button_order_feed(self):
        self.click_virt_mouse(HeaderLocators.BUTTON_ORDER_FEED)

    @allure.step('Нажать на блок заказа')
    def click_order_box(self):
        self.click_element(OrderFeedPageLocators.PATTERN_ORDER_BOX)

    @allure.step('Получить проверочный текст в всплывающем окне')
    def return_text_in_order_box(self):
        return self.get_text_to_element(OrderFeedPageLocators.TEXT_IN_ORDER_BOX)

    @allure.step('Получить id заказа со страницы Лента заказов')
    def return_id(self):
        return self.get_text_to_element(OrderFeedPageLocators.PATTERN_ORDER_BOX)

    @allure.step('Получить колчество заказов за все время и за сегодня')
    def return_count_order(self, locator):
        return self.get_text_to_element(locator)

    @allure.step('Получить id заказа в работе')
    def return_order_in_progress(self):
        return self.get_text_to_element(OrderFeedPageLocators.ORDER_PROGRESS)[1:]

from pages.base_page import BasePage
from locators.personal_page_locators import *
import allure


class PersonalPage(BasePage):

    @allure.step('Возврат кнопки История заказов')
    def visible_button(self):
        return self.return_element(PersonalPageLocators.BUTTON_HISTORY_ORDER)

    @allure.step('Клик по кнопке история заказов')
    def click_history_of_order_button_and_return_element(self):
        self.click_element(PersonalPageLocators.BUTTON_HISTORY_ORDER)
        return self.return_element(PersonalPageLocators.ID_ORDER)

    @allure.step('Клик по кнопке история заказов')
    def click_history_of_order_button(self):
        self.click_element(PersonalPageLocators.BUTTON_HISTORY_ORDER)

    @allure.step('Клик по кнопке Выход из акаунта')
    def click_exit_button(self):
        self.click_element(PersonalPageLocators.BUTTON_EXIT)

    @allure.step('Получение id заказа')
    def return_id_order_from_history_order(self):
        return self.get_text_to_element(PersonalPageLocators.ID_ORDER)

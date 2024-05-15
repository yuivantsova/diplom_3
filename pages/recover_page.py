import allure
from locators.recover_page_locators import *
from pages.base_page import BasePage


class RecoverPage(BasePage):

    @allure.step('Ввести email')
    def input_email(self):
        self.input_text_to_element(RecoverPageLocators.INPUT_EMAIL, self.generator_email())

    @allure.step('Нажать на кнопку Восстановить пароль')
    def go_to_page_reset_password(self):
        self.click_element(RecoverPageLocators.BUTTON_RECOVER)

    @allure.step('Получение заголовка страницы Восстановить пароль')
    def get_text_header_recover_page(self):
        return self.get_text_to_element(RecoverPageLocators.HEADER_PAGE)

    @allure.step('Видимость кнопки Сохранить')
    def visible_button_save(self):
        return self.return_element(RecoverPageLocators.BUTTON_SAVE)

    @allure.step('Нажать на кнопку скрыть/показать пароль')
    def click_visibility_button(self):
        self.click_element(RecoverPageLocators.BUTTON_VISIBILITY)

    @allure.step('Активность поля пароль')
    def field_password_active(self):
        self.click_visibility_button()
        return self.return_element(RecoverPageLocators.FIELD_NEW_PASSWORD)

    @allure.step('Ввести email и нажать на кнопку Восстановить')
    def input_email_and_click_recover_button(self):
        self.input_email()
        self.go_to_page_reset_password()

import allure
from locators.login_page_locators import *
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Заполнить поле email')
    def input_email(self, email):
        self.input_text_to_element(LoginPageLocators.INPUT_EMAIL, email)

    @allure.step('Запоняем поле пароль')
    def input_password(self, password):
        self.input_text_to_element(LoginPageLocators.INPUT_PASS, password)

    @allure.step('Нажать кнопку Войти')
    def click_button_enter(self):
        self.click_element(LoginPageLocators.BUTTON_ENTER)

    @allure.step('Получить кнопку Войти')
    def return_login_button(self):
        return self.return_element(LoginPageLocators.BUTTON_ENTER)

    @allure.step('Вход зарегестрированного пользователя')
    def login_to_site(self, email, password):
        self.input_email(email)
        self.input_password(password)
        self.click_button_enter()

    @allure.step('Нажать на кнопку Воостановить пароль')
    def click_button_recover_password(self):
        self.click_element(LoginPageLocators.BUTTON_RECOVER_PASSWORD)
import allure
from data import *
import pytest
from conftest import *
from pages.login_page import *
from pages.recover_page import *


class TestRecoverPage:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_reset_password_page(self, login_page, recover_page, main_page, driver):

        main_page.click_button_personal_area()
        login_page.click_button_recover_password()
        assert recover_page.get_text_header_recover_page() == HEADER_RECOVER_PAGE # в FF тест иногда падает (а иногда не падает) из-за перекрытия элемента

    @allure.title('Проверка ввода почты и клик по кнопке Восстановить')
    def test_input_email_and_click_button(self, recover_page, driver, login_page, main_page):
        main_page.click_button_personal_area()
        login_page.click_button_recover_password()
        recover_page.input_email_and_click_recover_button()
        assert recover_page.visible_button_save() # в FF тест иногда падает (а иногда не падает) из-за перекрытия элемента

    @allure.title('Проверка подсвечивания поля пароль')
    def test_click_on_visibility_button(self, recover_page, driver, login_page, main_page):
        main_page.click_button_personal_area()
        login_page.click_button_recover_password()
        recover_page.input_email_and_click_recover_button()
        result = recover_page.field_password_active()
        assert ATTRIBUTE_ACTIVE_FIELD in result.get_attribute('class') # в FF тест иногда падает (а иногда не падает) из-за перекрытия элемента


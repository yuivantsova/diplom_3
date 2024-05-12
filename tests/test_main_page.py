import allure
from data import *
from conftest import *


class TestMainPage:

    @allure.title('Переход по клику на «Лента заказов»')
    def test_click_order_feed(self,main_page,login_page,create_test_user):

        main_page.click_order_feed_button()
        assert main_page.return_text_header_order_feed() == HEADER_ORDER_FEED_PAGE

    @allure.title('переход по клику на «Конструктор»')
    def test_click_constructor(self, main_page, login_page, create_test_user):

        main_page.click_order_feed_button()
        main_page.click_constructor_button()
        assert main_page.return_text_header_constructor() == HEADER_CONSTRUCTOR_PAGE

    @allure.title('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient(self, main_page, create_test_user, login_page):

        main_page.click_ingredient()
        assert main_page.return_header_ingr_box() == HEADER_INGREDIENT_BOX

    @allure.title('всплывающее окно закрывается кликом по крестику')
    def test_click_cross(self, main_page, create_test_user, login_page):
        main_page.click_ingredient()
        assert main_page.click_close_button() == HEADER_CONSTRUCTOR_PAGE

    @allure.title('при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_add_ingredient(self, main_page):

        main_page.move_ingredients()
        assert main_page.get_count() == '2'

    @allure.title('залогиненный пользователь может оформить заказ')
    def test_create_order_user(self, main_page,login_page,create_test_user):
        main_page.click_button_personal_area()
        login_page.login_to_site(create_test_user['email'], create_test_user['password'])
        main_page.move_ingredients()
        assert main_page.click_create_button_and_return_text() == 'идентификатор заказа'



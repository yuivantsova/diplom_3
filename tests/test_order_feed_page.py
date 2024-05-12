import requests
from locators.order_feed_page_locators import OrderFeedPageLocators
import allure
import pytest
from data import *
from conftest import *


class TestOrderFeedPage:

    @allure.step('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_open_window(self, order_feed_page):
        order_feed_page.click_button_order_feed()
        order_feed_page.click_order_box()

        assert order_feed_page.return_text_in_order_box() == TEXT_IN_ORDER_BOX

    @allure.step('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_orders_by_user_displeyed_in_order_feed(self, create_test_order, create_test_user,
                                                    personal_page, order_feed_page, main_page, login_page):
        main_page.click_button_personal_area()
        login_page.login_to_site(create_test_user['email'], create_test_user['password'])

        main_page.click_button_personal_area()
        personal_page.click_history_of_order_button()
        main_page.click_order_feed_button()
        id_order_history = personal_page.return_id_order_from_history_order()

        assert order_feed_page.return_id() == id_order_history

    @allure.step('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    @allure.step('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    @pytest.mark.parametrize('count_locator',[OrderFeedPageLocators.COUNT_ALL_TIME,
                                              OrderFeedPageLocators.COUNT_TODAY])
    def test_increase_count_all_time(self,create_test_user,main_page,login_page,order_feed_page, count_locator):
        main_page.click_button_personal_area()
        login_page.login_to_site(create_test_user['email'], create_test_user['password'])
        main_page.click_order_feed_button()
        count_1 = int(order_feed_page.return_count_order(count_locator))
        requests.post('https://stellarburgers.nomoreparties.site/api/orders',
                      headers={'Authorization': create_test_user['token']},
                      data={"ingredients": '61c0c5a71d1f82001bdaaa6d'}, timeout=10)
        count_2 = int(order_feed_page.return_count_order(count_locator))
        assert count_2 == (count_1+1)

    @allure.step('после оформления заказа его номер появляется в разделе В работе')
    def test_display_order_in_box_work(self, create_test_order, create_test_user,main_page,login_page,order_feed_page):
        main_page.click_button_personal_area()
        login_page.login_to_site(create_test_user['email'], create_test_user['password'])
        id_order = create_test_order
        main_page.click_order_feed_button()

        assert order_feed_page.return_order_in_progress() == id_order




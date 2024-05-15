import allure
import requests


class TestPersonalPage:

    @allure.title('переход по клику на «Личный кабинет»')
    def test_click_button_my_account(self, main_page, login_page, personal_page, create_test_user):
        main_page.click_button_personal_area()
        login_page.login_to_site(create_test_user['email'], create_test_user['password'])
        main_page.click_button_personal_area()
        assert personal_page.visible_button()

    @allure.title('переход в раздел «История заказов»')
    def test_click_button_history_of_order(self,main_page,login_page,
                                           personal_page,create_test_user):
        main_page.click_button_personal_area()
        login_page.login_to_site(create_test_user['email'], create_test_user['password'])
        main_page.click_button_personal_area()
        requests.post('https://stellarburgers.nomoreparties.site/api/orders',
                      headers={'Authorization': create_test_user['token']},
                      data={"ingredients": '61c0c5a71d1f82001bdaaa6d'}, timeout=10)
        assert personal_page.click_history_of_order_button_and_return_element()

    @allure.title('выход из аккаунта')
    def test_click_exit_button(self, main_page,login_page,personal_page,driver,create_test_user):
        main_page.click_button_personal_area()
        login_page.login_to_site(create_test_user['email'], create_test_user['password'])
        main_page.click_button_personal_area()
        personal_page.click_exit_button()
        assert login_page.return_login_button()


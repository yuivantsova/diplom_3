import pytest
import requests
import string
import random
from selenium import webdriver
from pages.base_page import BasePage
from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage
from pages.recover_page import RecoverPage
from pages.personal_page import PersonalPage
from pages.main_page import MainPage
from data import *


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox(options=options)
    elif request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
    driver.get(Url.MAIN_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def personal_page(driver):
    personal_page = PersonalPage(driver)
    return personal_page


@pytest.fixture(scope='function')
def login_page(driver):
    login_page = LoginPage(driver)
    return login_page


@pytest.fixture(scope='function')
def recover_page(driver):
    recover_page = RecoverPage(driver)
    return recover_page


@pytest.fixture(scope='function')
def main_page(driver):
    main_page = MainPage(driver)
    return main_page


@pytest.fixture(scope='function')
def order_feed_page(driver):
    order_feed_page = OrderFeedPage(driver)
    return order_feed_page


@pytest.fixture(scope='function')
def create_test_user():

    data_user = {}
    email_and_password = {}

    def generator_str():
        characters = string.ascii_letters + string.ascii_lowercase
        random_str = ''.join(random.choice(characters) for _ in range(8))
        return random_str

    email = f'{generator_str()}@yandex.ru'
    password = generator_str()
    name = generator_str()

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(f'{Url.CREATE_USER_URL}', data=payload, timeout=10)

    email_and_password['email'] = payload['email']
    email_and_password['password'] = payload['password']
    response_login = requests.post(f'{Url.LOGIN_USER}', data=payload, timeout=10)
    if response_login.status_code == 200:
        token = response_login.json()['accessToken']
        data_user['token'] = token
        data_user['email'] = payload['email']
        data_user['password'] = payload['password']
    yield data_user
    requests.delete(f'{Url.DELETE_USER}', headers={'Authorization': token})


@pytest.fixture(scope='function')
def create_test_order(create_test_user):
    order_payload = {"ingredients": '61c0c5a71d1f82001bdaaa6d'}
    response = requests.post(f'{Url.CREATE_ORDER}',
                             headers={'Authorization': create_test_user['token']}, data=order_payload, timeout=10)
    number = response.json()['order']['number']
    return str(number)

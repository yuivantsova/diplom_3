from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure
import string
import random
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from conftest import *


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажать на эдемент')
    def click_element(self, locator):
        WebDriverWait(self.driver,20).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).click()

    @allure.step('Ввод данных в поле')
    def input_text_to_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получение текста с элемента')
    def get_text_to_element(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    @allure.step('Получить элемент')
    def return_element(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Получение рандомной строки')
    def generator_str(self):
        characters = string.ascii_letters + string.ascii_lowercase
        random_str = ''.join(random.choice(characters) for _ in range(5))
        return random_str

    @allure.step('Получение email')
    def generator_email(self):
        return f'{self.generator_str()}@ya.ru'

    @allure.step('Перетаскивание элемента')
    def move_element(self, locator_source, locator_target):
        source = self.driver.find_element(*locator_source)
        target = self.driver.find_element(*locator_target)
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).pause(5).perform()
    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_virt_mouse(self,locator):

        action = ActionChains(self.driver)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))

        element = self.driver.find_element(*locator)
        action.click(on_element=element).perform()








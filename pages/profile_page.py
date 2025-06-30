import allure

from data import Data
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from urls import Urls
from locators.profile_page_locators import ProfilePageLocators

class  ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = Urls.profile_page_url
        self.locators = ProfilePageLocators()
       # self.locators_login_page = LoginPageLocators()

    @allure.step("Проверка текста на странице профиля")
    def is_profile_info_text_correct(self): # Проверяет, что текст в профиле соответствует ожидаемому
        self.wait_visibility_of_element(self.locators.ACCOUNT_TEXT_IN_PROFILE)
        actual_text = self.get_text_element(self.locators.ACCOUNT_TEXT_IN_PROFILE)
        return  actual_text == Data.info_text_in_profile_page

    @allure.step("Клик по кнопке 'История заказов'")
    def click_on_history_order_button(self): # клик по кнопке истории заказов
        self.wait_visibility_of_element(self.locators.PROFILE_MENU)
        self.scroll_to_and_click(self.locators.HISTORY_ORDER_BUTTON_IN_PROFILE)

    @allure.step("Клик по кнопке 'Выход' из аккаунта")
    def click_on_logout_button(self): # клик по кнопке выхода из аккаунта
        self.click_on_element(self.locators.BUTTON_LOGOUT_PROFILE)



    @allure.step("Получение номера последнего заказа в истории")
    def get_last_order_number_in_history_user(self): # получаем последний заказ пользователя
        self.wait_visibility_of_element(self.locators.ALL_ORDERS_IN_HISTORY_USER)
        numbers = self.get_texts_from_elements(self.locators.ALL_ORDERS_IN_HISTORY_USER)
        number_last_order =  numbers[0].lstrip('#0') # взяли первый и убрали #0
        return number_last_order
import allure

from data import Data
from pages.base_page import BasePage
from urls import Urls
from locators.order_feed_page_locators import OrderFeedPageLocators

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Urls.order_feed_page_url
        self.locators = OrderFeedPageLocators()

    @allure.step("Проверка появления заголовка формы ленты заказов")
    def check_text_on_feed_title(self): # проверить появление заголовка на странице заказов
        self.wait_visibility_of_element(self.locators.FEED_TITLE)
        tex_title_form_feed = self.get_text_element(self.locators.FEED_TITLE)
        return  tex_title_form_feed == Data.text_title_on_feed_form

    @allure.step("Клик по карточке заказа")
    def click_on_order_card(self): # клик на карточку заказа
        self.click_on_element(self.locators.FIRS_ORDER_CARD_IN_FEED)

    @allure.step("Проверка текста в модальном окне заказа")
    def check_text_order_in_modal(self): # Проверяем текст в модальном окне
        self.wait_modal_opened(self.locators.ORDER_MODAL) # перед проверкой ждем появление модалки
        order_text =  self.get_text_element(self.locators.ORDER_TEXT_IN_ORDER_MODAL)
        return  order_text == Data.text_module_feed

    @allure.step("Получение общего количества заказов")
    def get_total_orders_count(self): # получить общее число заказов
        self.wait_visibility_of_element(self.locators.TOTAL_ORDERS_COUNTER)
        return int(self.get_text_element(self.locators.TOTAL_ORDERS_COUNTER))

    @allure.step("Получение количества заказов за сегодня")
    def get_today_orders_count(self): # получить число заказов за сегодня
        self.wait_visibility_of_element(self.locators.TODAY_ORDERS_COUNTER)
        return  int(self.get_text_element(self.locators.TODAY_ORDERS_COUNTER))

    @allure.step("Получение списка номеров заказов в ленте заказов")
    def get_all_order_numbers_feed(self): # получить весь список заказов в ленте
        self.wait_visibility_of_element(self.locators.ALL_ORDERS_IN_FEED)
        raw_numbers = self.get_texts_from_elements(self.locators.ALL_ORDERS_IN_FEED)
        cleaned_numbers = []
        for text in raw_numbers:
            if text.startswith("#"):
                text = text[1:]  # Удаляем "#"
            cleaned_numbers.append(text.lstrip('0')) # удаляем ведущие нули при добавлении
        return cleaned_numbers

    @allure.step("Получение списка номеров заказов в работе")
    def get_all_order_numbers_in_progress(self):  # получить весь список заказов в работе
        self.wait_visibility_of_element(self.locators.ALL_ORDERS_IN_PROGRESS)
        raw_numbers = self.get_texts_from_elements(self.locators.ALL_ORDERS_IN_PROGRESS)
        cleaned_numbers = []
        for text in raw_numbers:
            cleaned_numbers.append(text.lstrip('0'))  # удаляем ведущие нули при добавлении
        return cleaned_numbers
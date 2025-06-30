import allure
from selenium.webdriver import ActionChains
from data import Data
from pages.base_page import BasePage
from urls import Urls
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Urls.main_page_url
        self.locators = MainPageLocators()

    @allure.step("Клик по кнопке 'Личный кабинет'")
    def click_on_button_profile_page(self): # переход в личный кабинет
        self.click_on_element(self.locators.BUTTON_PROFILE_ACCOUNT)

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_on_constructor_button(self): # переход в констуктор
        self.click_on_element(self.locators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_on_feed_order_button(self): # переход в ленту заказов
        self.click_on_element(self.locators.FEED_BUTTON)

    @allure.step("Клик по ингредиенту в конструкторе")
    def click_on_ingredient_in_constructor(self): # клик по булочке
        self.click_on_element(self.locators.INGREDIENT_IN_CONSTRUCTOR)

    @allure.step("Закрытие модального окна ингредиента")
    def click_on_close_modal(self):# закрытие модального окна с информацией о булочке
        self.wait_modal_opened(self.locators.MODAL_OPENED)
        self.click_on_element(self.locators.CLOSE_BUN_TITLE_IN_MODAL)

    @allure.step("Клик по кнопке 'Оформить заказ' и ждем анимацию оформления")
    def click_on_button_order(self): # нажимаем на кнопку оформления заказа и ждем все анимации
        self.click_on_element(self.locators.BUTTON_ORDER)
        self.wait_visibility_of_element(self.locators.LOADING_ORDER_INDICATOR)  # ждем иконки с анимацией оформления
        self.wait_invisibility_of_element(self.locators.MODAL_OVERLAY_WHEN_ORDER_PROCESS)  # ждем исчезновения оверлея оформления заказа
        self.wait_visibility_of_element(self.locators.SUCCESS_ORDER_INDICATOR)  # ждем иконки с анимацией успешного заказ

    @allure.step("Проверка заголовка формы конструктора")
    def check_text_on_constructor_title(self): # проверить появление информационного текста на странице профиля
        self.wait_visibility_of_element(self.locators.CONSTRUCTOR_TITLE)
        tex_title_form_constructor =  self.get_text_element(self.locators.CONSTRUCTOR_TITLE)
        return tex_title_form_constructor == Data.text_title_on_constructor_form

    @allure.step("Проверка уведомления о принятии заказа")
    def check_text_order_acceptance_notification(self):
        self.wait_modal_opened(self.locators.MODAL_OPENED) # перед проверкой ждем появление модалки
        notification_text =  self.get_text_element(self.locators.ORDER_ACCEPTANCE_NOTIFICATION)
        return  notification_text == Data.text_order_acceptance_notification

    @allure.step("Проверка появления изображения ингредиента в модальном окне")
    def is_image_bun_in_module_window_visible(self): # проверка появления картинки булочки в модальном окне
        self.wait_modal_opened(self.locators.MODAL_OPENED)
        return self.is_element_visible(self.locators.BUN_STATS_IN_MODAL)

    @allure.step("Проверка закрытия модального окна заказа")
    def is_modal_bun_closed(self): # проверка, что модально окно булочки закрыто
        return self.is_modal_closed(self.locators.MODAL_OPENED)

    @allure.step("Перетаскивание ингредиента в конструктор")
    def drag_ingredient_to_constructor(self): # перетаскиваем булочку в констуктор
        self.wait_visibility_of_element(self.locators.BURGER_CONSTRUCTOR_ZONE)
        self.wait_visibility_of_element(self.locators.INGREDIENT_IN_CONSTRUCTOR)
        ingredient = self.driver.find_element(*self.locators.INGREDIENT_IN_CONSTRUCTOR)
        constructor_zone = self.driver.find_element(*self.locators.BURGER_CONSTRUCTOR_ZONE)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, constructor_zone).perform()

    @allure.step("Проверка значения счётчика ингредиента после перетаскивания ингредиента")
    def check_value_counter_buns(self):
        value = self.get_text_element(self.locators.BUN_COUNTER)
        return value == '2'

    @allure.step("Закрытие модального окна заказа")
    def close_order_modal(self): # закрываем окно заказа
        self.click_on_element(self.locators.CLOSE_ORDER_MODAL)
        self.wait_modal_closed(self.locators.MODAL_OPENED) # ждем закрытия попапа уже самого модального окна

    @allure.step("Создание заказа и закрытие модального окна")
    def create_order_and_close_modal(self): # создать заказ и закрыть модальное окно заказа
        self.drag_ingredient_to_constructor()
        self.click_on_button_order()
        self.close_order_modal()

    @allure.step("Создание заказа на главной странице и переход в ленту заказов")
    def create_order_on_main_and_return_to_feed(self): # переход на главную, создание  заказа в конструкторе и возврат в ленту заказов.
        self.click_on_constructor_button()
        self.create_order_and_close_modal()
        self.click_on_feed_order_button()

    @allure.step("Получение номера заказа из модального окна")
    def get_number_order_from_modal_window(self):
        return self.get_text_element(self.locators.NUMBER_ORDER_IN_MODAL) # забрали номер заказа
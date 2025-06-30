import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestMainPage:

    @allure.title("Проверка перехода в раздел 'Конструктор'")
    def test_navigate_to_constructor(self, driver):  # переход по клику на «Конструктор», со страницы логина
        login_page = LoginPage(driver)
        login_page.open()
        main_page = MainPage(driver)
        main_page.click_on_constructor_button()

        assert main_page.check_text_on_constructor_title(), 'Не появился заголовок страницы конструктор - соберите бургер'

    @allure.title("Проверка открытия модального окна ингредиента")
    def test_open_modal_window_bun(self, driver): # проверяет открытие модального окна булочки кликом по ингредиенту
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_on_ingredient_in_constructor()

        assert main_page.is_image_bun_in_module_window_visible(), 'Не появился состав ингредиента в модальном окне'

    @allure.title("Проверка закрытия модального окна ингредиента")
    def test_open_close_window_bun(self, driver): # проверяет, что модальное окно можно закрыть
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_on_ingredient_in_constructor()
        main_page.click_on_close_modal()

        assert main_page.is_modal_bun_closed(), "Модальное окно с булочкой не закрылось"

    @allure.title("Проверка добавления ингредиента в заказ")
    def test_add_ingredient_in_order_drag_and_drop(self, driver): # проверяет добавление ингредиента в заказ
        main_page = MainPage(driver)
        main_page.open()
        main_page.drag_ingredient_to_constructor()

        assert main_page.check_value_counter_buns(), "Каунтер ингредиента не изменился"

    @allure.title("Проверка оформления заказа залогиненным пользователем")
    def test_placing_order_logged_user(self, login_user_via_localStorage, driver): # проверяет, что залогиненый пользователь может оформить заказ
        main_page = MainPage(driver)
        main_page.drag_ingredient_to_constructor()
        main_page.click_on_button_order()

        assert main_page.check_text_order_acceptance_notification(), 'Окно с подтверждением заказа не появилось'
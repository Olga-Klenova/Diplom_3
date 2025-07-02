import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.profile_page import ProfilePage


class TestOrderFeedPage:
    @allure.title("Проверка перехода в раздел 'Лента заказов'")
    def test_navigate_to_feed_order(self, driver):  # переход по клику на «Лента заказов» сразу с главной страницы
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_on_feed_order_button()
        order_feed_page = OrderFeedPage(driver)  # переходим на страницу ленты заказов

        assert order_feed_page.check_text_on_feed_title(), 'Не появился заголовок страницы ленты заказов - лента заказов'

    @allure.title("Проверка открытия модального окна с заказом")
    def test_order_details_modal_open(self, driver): # при клике на заказ открывается окно с деталями
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open()
        order_feed_page.click_on_order_card()

        assert order_feed_page.check_text_order_in_modal(), 'Модальное окно заказа не открылось'

    @allure.title("Проверка увеличения счётчика общего количества заказов после создания заказа")
    def test_total_orders_counter_increases(self, driver, login_user_via_localStorage): # проверяет что при создании нового заказа счётчик Выполнено за всё время увеличивается,
        # Перешли в ленту заказов, считали текущее значение
        main_page = MainPage(driver)
        main_page.click_on_feed_order_button()
        order_feed_page = OrderFeedPage(driver)
        initial_count =  order_feed_page.get_total_orders_count()
        # Создали заказ на главной
        main_page.create_order_on_main_and_return_to_feed()
        # Вернулись в ленту заказов и проверили счётчик
        final_count = order_feed_page.get_total_orders_count() # получили новое число общих заказов

        assert final_count  > initial_count, "Счётчик заказов за всё время не увеличился"

    @allure.title("Проверка увеличения счётчика заказов за сегодня после создания заказа")
    def test_today_orders_counter_increases(self, driver, login_user_via_localStorage): # проверяет что при создании нового заказа счётчик Выполнено за сегодня увеличивается,
        # Перешли в ленту заказов, считали текущее значение
        main_page = MainPage(driver)
        main_page.click_on_feed_order_button()  # переходим в ленту заказов
        order_feed_page = OrderFeedPage(driver)
        initial_count = order_feed_page.get_today_orders_count()  # получили число сегодняшних заказов
        # Создали заказ на главной
        main_page.create_order_on_main_and_return_to_feed()
        # Вернулись в ленту заказов и проверили счётчик
        final_count = order_feed_page.get_today_orders_count()  # получили новое число сегодняшних заказов

        assert final_count > initial_count, "Счётчик заказов за сегодня не увеличился"

    @allure.title("Проверка появления созданного заказа в разделе 'В работе'")
    def test_order_appears_in_progress_list(self,  driver, login_user_via_localStorage): # проверка того, что  созданный заказ появляется в списке заказов в работе
        # Создали заказ на главной
        main_page = MainPage(driver)
        main_page.drag_ingredient_to_constructor()
        main_page.click_on_button_order()
        order_number = main_page.get_number_order_from_modal_window() # записали номер заказа из модалки
        main_page.close_order_modal()
        main_page.click_on_feed_order_button()
        # вернулись в ленту заказов
        order_feed_page =  OrderFeedPage(driver)
        order_numbers_in_progress = order_feed_page.get_all_order_numbers_in_progress()

        assert order_number in order_numbers_in_progress, f"Заказ {order_number} не найден  в списке заказов в работе"

    @allure.title("Проверка отображения заказа из истории пользователя в ленте заказов")
    def test_user_order_appears_in_feed(self, driver, login_user_via_localStorage): # заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»,
        # Создали заказ на главной
        main_page = MainPage(driver)
        main_page.create_order_and_close_modal()
        main_page.click_on_button_profile_page()
        # перешли в профиль и забрали номер заказа из истории
        profile_page = ProfilePage(driver)
        profile_page.click_on_history_order_button()
        history_order_number = profile_page.get_last_order_number_in_history_user()
        # Вернулись в ленту заказов
        main_page.click_on_feed_order_button()
        order_feed_page =  OrderFeedPage(driver)
        order_numbers_feed = order_feed_page.get_all_order_numbers_feed()

        assert history_order_number in order_numbers_feed, f"Заказ {history_order_number} не найден  в ленте заказов"

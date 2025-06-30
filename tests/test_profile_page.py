import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from urls import Urls


class TestProfilePage:
    @allure.title("Проверка перехода в личный кабинет авторизованного пользователя")
    def test_navigate_to_profile(self, driver, login_user_via_localStorage): # проверяет переход в личный кабинет с авторизацией
        main_page = MainPage(driver)
        main_page.click_on_button_profile_page()
        profile_page = ProfilePage(driver)

        assert profile_page.is_profile_info_text_correct(), 'Не удалось перейти в личный кабинет, ожидаемый текст в профиле не отобразился'

    @allure.title("Проверка перехода в раздел 'История заказов' авторизованного пользователя")
    def test_navigate_to_history_order_profile(self, driver, login_user_via_localStorage): # проверяет переход в историю заказов профиля с авторизацией
        main_page = MainPage(driver)
        main_page.click_on_button_profile_page()
        profile_page = ProfilePage(driver)
        profile_page.click_on_history_order_button()

        current_url = profile_page.get_current_url(Urls.order_history_profile_url)
        assert current_url == Urls.order_history_profile_url, f"Ожидалось '{Urls.order_history_profile_url}', но получили '{current_url}'"
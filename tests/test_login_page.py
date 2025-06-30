import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestLoginPage:
    @allure.title("Проверка выхода из аккаунта c переходом на страницу логина")
    def test_logout_user(self, driver, login_user_via_localStorage): # проверяет выход из аккаунта в личном кабинете с авторизацией
        main_page = MainPage(driver)
        main_page.click_on_button_profile_page()
        profile_page = ProfilePage(driver)
        profile_page.click_on_logout_button()
        login_page = LoginPage(driver)

        assert login_page.is_login_button_visible(), "Кнопка входа не отображается после выхода из профиля"
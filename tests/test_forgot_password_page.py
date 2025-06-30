import allure

from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from urls import Urls
from data import Data

class TestPasswordRecovery:

    @allure.title("Проверка перехода на страницу восстановления пароля")
    def test_navigate_to_password_recovery_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.click_on_forgot_password()
        forgot_password_page = ForgotPasswordPage(driver) # переход на страницу восстановления
        current_url = forgot_password_page.get_current_url()

        assert current_url == Urls.forgot_password_url, f"Ожидалось '{Urls.forgot_password_url}', но получили '{current_url}'"

    @allure.title("Проверка ввода email и отправки формы восстановления пароля")
    def test_submit_email_for_password_recovery(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open()
        forgot_password_page.fill_form_recovery_email(Data.EMAIL_FOR_RECOVERY)
        forgot_password_page.click_on_button_recovery()

        current_url = forgot_password_page.get_current_url(Urls.reset_password_url)

        assert current_url == Urls.reset_password_url, f"Ожидалось '{Urls.reset_password_url}', но получили '{current_url}'"

    @allure.title("Проверка подсветки поля пароля при переключении видимости")
    def test_toggle_password_visibility_and_highlight_input(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open()
        forgot_password_page.click_on_button_recovery()
        forgot_password_page.fill_form_recovery_password(Data.PASSWORD_FOR_RECOVERY)
        forgot_password_page.click_icon_show_password()

        assert forgot_password_page.is_password_input_active(), "Поле пароля не подсвечено после клика по кнопке показать/скрыть"
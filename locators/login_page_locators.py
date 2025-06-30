from selenium.webdriver.common.by import By


class LoginPageLocators:
    FORGOT_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'a[href="/forgot-password"]') # кнопка восстановить пароль

    SUBMIT_BUTTON_LOGIN_TO_ACCOUNT = (
    By.XPATH, ".//button[text() = 'Войти']")  # кнопка входа в аккаунт на странице login
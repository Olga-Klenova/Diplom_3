from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators: # объединяет в себе локаторы страниц forgot-password и reset-password
    TITLE_FORM_FORGOT_PASSWORD = (By.XPATH ,".//h2[text()='Восстановление пароля']") # заголовок формы восстановленяи пароля

    INPUT_EMAIL_FORGOT = (By.XPATH, ".//input[@type='text']")  # поле ввода email на странице восстановления пароля

    SUBMIT_BUTTON_ACCOUNT_RECOVERY = (By.XPATH, ".//button[text() = 'Восстановить']")  # кнопка восстановления пароля на странице восстановления

    SUBMIT_BUTTON_FORGOT_FORM = (By.XPATH, ".//p[text() = 'Вспомнили пароль?']/a")  # Кнопка войти в форме восстановления пароля

    HIDE_AND_SHOW_INPUT_PASSWORD = (By.CSS_SELECTOR, ".input__icon svg") # кнопка скрытия/отображения пароля

    INPUT_PASSWORD_FORGOT = (By.XPATH, ".//input[@type='password']")  # поле ввода пароля на странице восстановления со скрытым паролем

    INPUT_PASSWORD_IS_ACTIVE = (
        By.XPATH, "//div[contains(@class, 'input_status_active')]") # поле ввода пароля в состоянии активно
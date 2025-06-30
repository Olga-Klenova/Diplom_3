class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    # Урлы для ui тестов
    login_page_url = BASE_URL + '/login'
    main_page_url = BASE_URL + '/'
    order_feed_page_url = BASE_URL + '/feed'
    profile_page_url = BASE_URL + '/account/profile' # открывается только если авторизован
    forgot_password_url =  BASE_URL + "/forgot-password"
    reset_password_url =  BASE_URL + "/reset-password"
    order_history_profile_url = BASE_URL + "/account/order-history"
    # Урлы api ручек
    create_user = BASE_URL + "/api/auth/register" # эндпоинт для регистрации пользователя
    user_data_management_url = BASE_URL + "/api/auth/user"
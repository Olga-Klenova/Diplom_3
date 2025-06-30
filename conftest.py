import pytest
import requests
from selenium import webdriver
from data import Data
from urls import Urls

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
@pytest.fixture
def driver(request):  # создание и закрытие драйвера/браузера
    browser = request.config.getoption("browser")
    driver = None
    if browser == "chrome":
        print("\nstart chrome browser for test..")
        driver  = webdriver.Chrome()
    elif browser == "firefox":
        print("\nstart firefox browser for test..")
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser should be chrome or firefox")
    yield driver
    print("\nquit browser..")
    driver.quit()


@pytest.fixture()
def register_new_user_and_return_credentials(): # регистрация и удаление пользователя без установки токена в браузере
    payload = Data.USER_CREDENTIALS # данные пользователя
    email = payload.get('email')
    password = payload.get('password')
    response = requests.post(Urls.create_user, json=payload)
    if response.status_code == 200:
        access_token = response.json()["accessToken"]
        refresh_token = response.json()["refreshToken"]
        yield email, password, access_token, refresh_token   # передаем логин пароль и токены
        headers = {"Authorization": access_token}
        requests.delete(Urls.user_data_management_url, headers=headers)  # удаляем передав токен
    else:
        pytest.fail(f"Не удалось зарегистрировать пользователя: {response.status_code}, {response.text}")


@pytest.fixture()
def login_user_via_localStorage(register_new_user_and_return_credentials, driver): #  установка токена сразу в браузер
    email, password, access_token, refresh_token  = register_new_user_and_return_credentials # забираем креды

    driver.get(Urls.BASE_URL) # открываем главную и ставим токен
    driver.execute_script(f"window.localStorage.setItem('accessToken', '{access_token}');") # пишем  access_token токен в localStorage
    driver.execute_script(f"window.localStorage.setItem('refreshToken', '{refresh_token}');") # пишем  refresh_token токен в localStorage
    driver.refresh() #обновили страницу чтобы токены применились
    return email, password
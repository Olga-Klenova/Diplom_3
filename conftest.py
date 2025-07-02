import pytest
import requests
from selenium import webdriver
from data import Data
from urls import Urls

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
@pytest.fixture
def driver(request):
    browser = request.config.getoption("browser")
    driver = None
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(Urls.BASE_URL)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture()
def register_new_user_and_return_credentials():
    payload = Data.USER_CREDENTIALS
    email = payload.get('email')
    password = payload.get('password')
    response = requests.post(Urls.create_user, json=payload)
    if response.status_code == 200:
        access_token = response.json()["accessToken"]
        refresh_token = response.json()["refreshToken"]
        yield email, password, access_token, refresh_token
        headers = {"Authorization": access_token}
        requests.delete(Urls.user_data_management_url, headers=headers)
    else:
        pytest.fail(f"Не удалось зарегистрировать пользователя: {response.status_code}, {response.text}")


@pytest.fixture()
def login_user_via_localStorage(register_new_user_and_return_credentials, driver):
    email, password, access_token, refresh_token  = register_new_user_and_return_credentials

    driver.get(Urls.BASE_URL)
    driver.execute_script(f"window.localStorage.setItem('accessToken', '{access_token}');")
    driver.execute_script(f"window.localStorage.setItem('refreshToken', '{refresh_token}');")
    driver.refresh()
    return email, password
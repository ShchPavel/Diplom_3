import pytest
from helpers import WebDriverFactory, RegisterUser, DeleteUser
from pages.login_page import LoginPage


@pytest.fixture(scope='function', params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    driver = WebDriverFactory.get_web_driver(browser_name)
    yield driver

    driver.quit()


@pytest.fixture(scope='function', params=["firefox", "chrome"])
def temp_user_logged_in__return_driver(request):
    browser_name = request.param
    driver = WebDriverFactory.get_web_driver(browser_name)
    response, payload = RegisterUser.register_new_random_user()
    page = LoginPage(driver)
    page.go_to_login_page()
    page.to_login(payload['email'], payload['password'])
    yield driver

    driver.quit()
    token = str(response.json()['accessToken']).replace('Bearer ', '')
    DeleteUser.delete_user(token)


@pytest.fixture(scope='function', params=["firefox", "chrome"])
def temp_user_logged_in__return_driver_and_token(request):
    browser_name = request.param
    driver = WebDriverFactory.get_web_driver(browser_name)
    response, payload = RegisterUser.register_new_random_user()
    page = LoginPage(driver)
    page.go_to_login_page()
    page.to_login(payload['email'], payload['password'])
    token = str(response.json()['accessToken']).replace('Bearer ', '')

    yield driver, token

    driver.quit()
    DeleteUser.delete_user(token)

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
def driver_temp_user_logged_in(request):
    browser_name = request.param
    driver = WebDriverFactory.get_web_driver(browser_name)
    response, payload = RegisterUser.register_new_random_user()
    page = LoginPage(driver)
    page.open_login_page()
    page.to_login(payload['email'], payload['password'])
    yield driver

    driver.quit()
    token = str(response.json()['accessToken']).replace('Bearer ', '')
    DeleteUser.delete_user(token)

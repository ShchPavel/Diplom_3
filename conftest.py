import pytest
from helpers import WebDriverFactory, RegisterUser, DeleteUser


@pytest.fixture(scope='function', params=["firefox", "chrome"])
def driver(request):
    browser_name = request.param
    driver = WebDriverFactory.get_web_driver(browser_name)
    yield driver
    driver.quit()


@pytest.fixture(scope='function', params=["firefox", "chrome"])
def temp_user_and_driver(request):
    browser_name = request.param
    driver = WebDriverFactory.get_web_driver(browser_name)
    response, payload = RegisterUser.register_new_random_user()
    yield driver, payload
    driver.quit()
    token = str(response.json()['accessToken']).replace('Bearer ', '')
    DeleteUser.delete_user(token)

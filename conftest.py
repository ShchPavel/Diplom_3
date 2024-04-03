import pytest
from helpers import WebDriverFactory


@pytest.fixture(scope='function', params=["firefox", "chrome"])
def driver(request):
    browser_name = request.param
    driver = WebDriverFactory.get_web_driver(browser_name)
    yield driver
    driver.quit()


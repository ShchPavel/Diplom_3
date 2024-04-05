import time

from selenium.webdriver.common.by import By

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from data import Urls


class TestPersonalCabinet:
    def test_personal_cabinet_button_redirect_correct(self, temp_user_logged_in__return_driver):
        driver = temp_user_logged_in__return_driver
        page = MainPage(driver)
        page.go_to_personal_cabinet()
        assert driver.current_url == Urls.PROFILE_URL

    def test_personal_cabinet_order_history_button_redirect_correct(self, temp_user_logged_in__return_driver):
        driver = temp_user_logged_in__return_driver
        page = MainPage(driver)
        page.go_to_personal_cabinet()

        page = ProfilePage(driver)
        page.go_to_order_history_page()
        assert driver.current_url == Urls.PROFILE_ORDER_HISTORY_URL

    def test_logout_success(self, temp_user_logged_in__return_driver):
        driver = temp_user_logged_in__return_driver
        page = MainPage(driver)
        page.go_to_personal_cabinet()

        page = ProfilePage(driver)
        page.logout()
        assert (driver.current_url == Urls.LOGIN_URL and
                ('accessToken' and 'refreshToken' not in driver.execute_script("return window.localStorage;")))

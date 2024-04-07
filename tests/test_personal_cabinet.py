from helpers import CreateOrder
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
import allure


class TestPersonalCabinet:
    @allure.title('Проверка корректного редиректа после клика на «Личный кабинет»')
    def test_personal_cabinet_button_redirect_correct(self, temp_user_logged_in__return_driver):
        driver = temp_user_logged_in__return_driver
        page = MainPage(driver)
        page.go_to_personal_cabinet()
        assert ProfilePage(driver).get_save_profile_button() is not None

    @allure.title('Проверка корректного редиректа после клика на «История заказов»')
    def test_personal_cabinet_order_history_button_redirect_correct(self, temp_user_logged_in__return_driver_and_token):
        driver, token = temp_user_logged_in__return_driver_and_token
        CreateOrder.create_order(token)
        page = MainPage(driver)
        page.go_to_personal_cabinet()

        page = ProfilePage(driver)
        page.go_to_order_history_page()
        assert ProfilePage(driver).check_if_history_orders_exist() is not None

    @allure.title('Проверка успешного выхода из аккаунта')
    def test_logout_success(self, temp_user_logged_in__return_driver):
        driver = temp_user_logged_in__return_driver
        page = MainPage(driver)
        page.go_to_personal_cabinet()

        page = ProfilePage(driver)
        page.logout()
        assert 'accessToken' and 'refreshToken' not in driver.execute_script("return window.localStorage;")

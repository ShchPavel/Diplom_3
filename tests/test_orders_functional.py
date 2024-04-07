import allure
from selenium.webdriver.common.by import By
from helpers import CreateOrder
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestOrderFunctional:
    @allure.title('Проверка, что при клике на заказ в ленте заказов открывается попап с деталями')
    def test_open_order_details_success(self, temp_user_logged_in__return_driver):
        driver = temp_user_logged_in__return_driver
        page = MainPage(driver)
        page.go_to_order_feed()
        page = FeedPage(driver)
        page.click_first_order()
        assert page.check_popup_opened_in_feed() is True

    @allure.title('Проверка отображения заказов клиента из раздела "История заказов" в общем разделе "Лента заказов"')
    def test_orders_from_history_are_in_feed_success(self, temp_user_logged_in__return_driver_and_token):
        driver, token = temp_user_logged_in__return_driver_and_token

        registered_order_id = CreateOrder.create_order(token).json()["order"]["_id"]
        registered_order_locator_in_history = By.XPATH, f"//a[@href='/account/order-history/{registered_order_id}']/parent::li"

        MainPage(driver).go_to_personal_cabinet()

        page = ProfilePage(driver)
        page.go_to_order_history_page()

        my_orders = page.get_all_my_orders()
        is_registered_order_in_history_list = page.is_order_on_my_history_orders(registered_order_locator_in_history, my_orders)

        MainPage(driver).go_to_order_feed()

        page = FeedPage(driver)
        registered_order_locator_in_feed = By.XPATH, f"//a[@href='/feed/{registered_order_id}']/parent::li"
        all_orders = page.get_all_orders()
        is_registered_order_in_feed_list = page.is_order_in_feed_orders(registered_order_locator_in_feed, all_orders)
        with allure.step('Убеждаемся что заказ был открыт и в ленте заказов и в истории моих заказов'):
            assert is_registered_order_in_history_list and is_registered_order_in_feed_list

    @allure.title('Проверка увеличения счетчика "Выполнено за всё время" при создании нового заказа')
    def test_common_counter_increase_after_creating_order_success(self, temp_user_logged_in__return_driver_and_token):
        driver, token = temp_user_logged_in__return_driver_and_token
        MainPage(driver).go_to_order_feed()
        page = FeedPage(driver)
        value_before_order = page.get_orders_common_counter()
        CreateOrder.create_order(token)
        page.refresh_feed_page()
        value_after_order = page.get_orders_common_counter()
        with allure.step('Проверяем, что счетчик "Выполнено за всё время" увеличился'):
            assert value_after_order > value_before_order

    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня" при создании нового заказа')
    def test_daily_counter_increase_after_creating_order_success(self, temp_user_logged_in__return_driver_and_token):
        driver, token = temp_user_logged_in__return_driver_and_token
        MainPage(driver).go_to_order_feed()
        page = FeedPage(driver)
        value_before_order = page.get_orders_daily_counter()
        CreateOrder.create_order(token)
        page.refresh_feed_page()
        value_after_order = page.get_orders_daily_counter()
        with allure.step('Проверяем, что счетчик "Выполнено за сегодня" увеличился'):
            assert value_after_order > value_before_order

    @allure.title('Проверка появления заказа в разделе "В работе" после его создания')
    def test_created_order_is_on_work(self, temp_user_logged_in__return_driver_and_token):
        driver, token = temp_user_logged_in__return_driver_and_token
        MainPage(driver).go_to_order_feed()
        page = FeedPage(driver)
        order_number = CreateOrder.create_order(token).json()['order']['number']
        assert page.is_order_number_in_work(order_number, 100) is True

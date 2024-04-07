import time

from selenium.webdriver.common.by import By

from helpers import CreateOrder
from locators.feed_page_locators import FeedPageLocators
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from locators.profile_page_locators import ProfilePageLocators

class TestOrderFunctional:
    def test_open_order_details_success(self, temp_user_logged_in__return_driver):
        driver = temp_user_logged_in__return_driver
        page = MainPage(driver)
        page.go_to_order_feed()
        page = FeedPage(driver)
        page.click_first_order()
        assert len(driver.find_elements(*FeedPageLocators.POPUP_ORDER_OPENED)) > 0

    def test_orders_from_history_are_in_feed_success(self, temp_user_logged_in__return_driver_and_token):
        driver, token = temp_user_logged_in__return_driver_and_token

        page = MainPage(driver)
        page.go_to_personal_cabinet()

        page = ProfilePage(driver)
        page.go_to_order_history_page()

        registered_order_id = CreateOrder.create_order(token).json()["order"]["_id"]
        registered_order_locator_in_history = By.XPATH, f"//a[@href='/account/order-history/{registered_order_id}']/parent::li"
        my_orders = page.get_all_my_orders()
        is_registered_order_in_history_list = page.is_order_on_my_history_orders(registered_order_locator_in_history, my_orders)

        MainPage(driver).go_to_order_feed()

        page = FeedPage(driver)
        registered_order_locator_in_feed = By.XPATH, f"//a[@href='/feed/{registered_order_id}']/parent::li"
        all_orders = page.get_all_orders()
        is_registered_order_in_feed_list = page.is_order_in_feed_orders(registered_order_locator_in_feed, all_orders)

        assert is_registered_order_in_history_list and is_registered_order_in_feed_list

    def test_common_counter_increase_after_creating_order_success(self, temp_user_logged_in__return_driver_and_token):
        driver, token = temp_user_logged_in__return_driver_and_token
        MainPage(driver).go_to_order_feed()
        page = FeedPage(driver)
        value_before_order = page.get_orders_common_counter()
        CreateOrder.create_order(token)
        driver.refresh()
        value_after_order = page.get_orders_common_counter()
        assert value_after_order > value_before_order

    def test_daily_counter_increase_after_creating_order_success(self, temp_user_logged_in__return_driver_and_token):
        driver, token = temp_user_logged_in__return_driver_and_token
        MainPage(driver).go_to_order_feed()
        page = FeedPage(driver)
        value_before_order = page.get_orders_daily_counter()
        CreateOrder.create_order(token)
        driver.refresh()
        value_after_order = page.get_orders_daily_counter()
        assert value_after_order > value_before_order

    def test_created_order_is_on_work(self, temp_user_logged_in__return_driver_and_token):
        driver, token = temp_user_logged_in__return_driver_and_token
        MainPage(driver).go_to_order_feed()
        page = FeedPage(driver)
        order_number = CreateOrder.create_order(token).json()['order']['number']
        assert page.is_order_number_in_work(order_number, 10)

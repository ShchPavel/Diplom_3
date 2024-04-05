import time

from selenium.webdriver.common.by import By

from helpers import CreateOrder
from locators.feed_page_locators import FeedPageLocators
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from locators.profile_locators import ProfileLocators

class TestOrderFunctional:
    # def test_open_order_details_success(self, temp_user_logged_in__return_driver):
    #     driver = temp_user_logged_in__return_driver
    #     page = MainPage(driver)
    #     page.go_to_order_feed()
    #     page = FeedPage(driver)
    #     page.click_first_order()
    #     assert len(driver.find_elements(*FeedPageLocators.POPUP_ORDER_OPENED)) > 0

    def test_orders_from_history_are_in_feed_success(self, temp_user_logged_in__return_driver_and_token):
        driver, token = temp_user_logged_in__return_driver_and_token

        page = MainPage(driver)
        page.go_to_personal_cabinet()

        page = ProfilePage(driver)
        page.go_to_order_history_page()

        response = CreateOrder.create_order(token)
        registered_order_id = response.json()["order"]["_id"]
        registered_order_locator = By.XPATH, f"//a[@href='/account/order-history/12{registered_order_id}']/parent::li"
        ul_list_elements = driver.find_elements(*ProfileLocators.LIST_OF_MY_ORDERS)
        link = None
        for _ in ul_list_elements:
            link = driver.find_element(*registered_order_locator)
            print(link)
        assert link is not None

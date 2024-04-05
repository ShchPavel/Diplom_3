import time

import selenium.common

import helpers
from data import Urls
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestMainFunctional:
    def test_redirect_to_constructor_success(self, temp_user_logged_in__return_driver):
        driver = temp_user_logged_in__return_driver
        page = MainPage(driver)
        page.go_to_constructor()
        assert driver.find_element(*MainPageLocators.BUTTON_MAKE_ORDER) is not None

    def test_redirect_to_order_feed_success(self, temp_user_logged_in__return_driver):
        driver = temp_user_logged_in__return_driver
        page = MainPage(driver)
        page.go_to_order_feed()
        assert driver.find_element(*MainPageLocators.TEXT_ORDER_FEED) is not None and driver.current_url == Urls.ORDER_FEED_URL

    def test_choose_ingredient_open_popup_success(self, temp_user_logged_in__return_driver):
        driver = temp_user_logged_in__return_driver
        page = MainPage(driver)
        page.go_to_constructor()
        page.click_on_first_ingredient_in_list()
        assert driver.find_element(*MainPageLocators.POPUP_DETAIL_INGREDIENT) is not None

    def test_ingredient_popup_closing_success(self, temp_user_logged_in__return_driver):
        driver = temp_user_logged_in__return_driver
        page = MainPage(driver)
        page.go_to_constructor()
        page.click_on_first_ingredient_in_list()
        page.close_ingredient_details_popup()
        assert len(driver.find_elements(*MainPageLocators.POPUP_DETAIL_INGREDIENT)) == 0

    def test_add_ingredient_increase_counter_success(self, temp_user_logged_in__return_driver):
        driver = temp_user_logged_in__return_driver
        page = MainPage(driver)
        page.go_to_constructor()
        page.drag_n_drop(helpers.drag_and_drop_script, MainPageLocators.INGREDIENT_FIRST_IN_LIST, MainPageLocators.BURGER_BASKET)
        assert int(driver.find_element(*MainPageLocators.INGREDIENT_FIRST_IN_LIST_COUNTER).text) > 0

    def test_order_registration_success(self, temp_user_logged_in__return_driver):
        driver = temp_user_logged_in__return_driver
        page = MainPage(driver)
        page.go_to_constructor()
        page.drag_n_drop(helpers.drag_and_drop_script, MainPageLocators.INGREDIENT_FIRST_IN_LIST, MainPageLocators.BURGER_BASKET)
        page.make_order()
        assert len(driver.find_elements(*MainPageLocators.TEXT_ORDER_STARTED_TO_COOKING)) > 0

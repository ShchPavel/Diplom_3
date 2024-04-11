import time

from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage
import allure


class FeedPage(BasePage):
    @allure.step('Нажимаем на первый заказ')
    def click_first_order(self):
        self.click_on_element(FeedPageLocators.ORDER_FEED_FIRST_ORDER)
        self.wait_and_find_element(FeedPageLocators.POPUP_ORDER_OPENED)

    @allure.step('Получаем список всех заказов')
    def get_all_orders(self):
        return self.get_orders(FeedPageLocators.LIST_OF_ORDERS)

    @allure.step('Проверяем, есть ли заказ в общем списке заказов')
    def is_order_in_feed_orders(self, order_locator, feed_orders_locator):
        link = None
        for _ in feed_orders_locator:
            link = self.wait_and_find_element(order_locator)

        if link is not None:
            return True
        else:
            return False

    @allure.step('Получаем общее количество заказов')
    def get_orders_common_counter(self):
        return self.get_element_value_using_wait(FeedPageLocators.COUNTER_ALL_ORDERS)

    @allure.step('Получаем количество заказов за день')
    def get_orders_daily_counter(self):
        return self.get_element_value_using_wait(FeedPageLocators.COUNTER_DAILY_ORDERS)

    @allure.step('Проверяем, появился ли заказ в списке взятых в работу заказов')
    def is_order_number_in_work(self, order_number):
        if str(order_number) in self.wait_and_find_element_return_text(FeedPageLocators.ORDER_IN_WORK):
            return True
        else:
            return False

    @allure.step('Проверяем наличие текста "Лента заказов" на странице')
    def get_text_feed_indicator(self):
        return self.wait_and_find_element(FeedPageLocators.TEXT_ORDER_FEED)

    @allure.step('Проверяем, что открывается попап с деталями заказа')
    def check_popup_opened_in_feed(self):
        if len(self.find_elements(FeedPageLocators.POPUP_ORDER_OPENED)) > 0:
            return True
        else:
            return False

    @allure.step('Рефрешим страницу')
    def refresh_feed_page(self):
        self.refresh_page()
        self.wait_and_find_element(FeedPageLocators.COUNTER_DAILY_ORDERS)

    @allure.step('Определяем локатор для блока с зарегистрированным заказом в ленте заказов')
    def get_dynamic_order_locator_in_feed(self, order_id):
        q_method, q_locator = FeedPageLocators.DYNAMIC_ORDER_NUMBER_IN_FEED
        locator = q_method, q_locator.format(order_id)
        return locator

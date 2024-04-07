from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage
import allure


class FeedPage(BasePage):

    def click_first_order(self):
        self.click_on_element(FeedPageLocators.ORDER_FEED_FIRST_ORDER)
        self.wait_and_find_element(FeedPageLocators.POPUP_ORDER_OPENED)

    def is_order_exist_in_feed(self, order_id):
        pass

    def get_all_orders(self):
        return self.get_orders(FeedPageLocators.LIST_OF_ORDERS)

    def is_order_in_feed_orders(self, order_locator, feed_orders_locator):
        link = None
        for _ in feed_orders_locator:
            link = self.wait_and_find_element(order_locator)

        if link is not None:
            return True
        else:
            return False

    def get_orders_common_counter(self):
        return self.get_element_value(FeedPageLocators.COUNTER_ALL_ORDERS)

    def get_orders_daily_counter(self):
        return self.get_element_value(FeedPageLocators.COUNTER_DAILY_ORDERS)

    # def get_order_in_work_value(self):
    #     return self.get_element_value(FeedPageLocators.ORDER_IN_WORK)

    def is_order_number_in_work(self, order_number, counter):
        if counter > 0:
            order_number_in_work = self.get_element_value(FeedPageLocators.ORDER_IN_WORK)

            if str(order_number) in order_number_in_work:
                return True
            else:
                self.is_order_number_in_work(order_number, counter-1)


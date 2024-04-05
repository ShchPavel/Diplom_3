from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):

    def click_first_order(self):
        self.click_on_element(FeedPageLocators.ORDER_FEED_FIRST_ORDER)
        self.wait_and_find_element(FeedPageLocators.POPUP_ORDER_OPENED)

    def is_order_exist_in_feed(self, order_id):
        pass
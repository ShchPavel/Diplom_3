from selenium.webdriver.common.by import By


class FeedPageLocators:
    ORDER_FEED_FIRST_ORDER = By.CSS_SELECTOR, ".OrderFeed_list__OLh59 > .OrderHistory_listItem__2x95r"
    POPUP_ORDER_OPENED = By.CSS_SELECTOR, ".Modal_modal_opened__3ISw4"
    LIST_OF_ORDERS = By.CSS_SELECTOR, ".OrderFeed_list__OLh59"

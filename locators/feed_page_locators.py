from selenium.webdriver.common.by import By


class FeedPageLocators:
    ORDER_FEED_FIRST_ORDER = By.CSS_SELECTOR, ".OrderFeed_list__OLh59 > .OrderHistory_listItem__2x95r"
    POPUP_ORDER_OPENED = By.CSS_SELECTOR, ".Modal_modal_opened__3ISw4"
    LIST_OF_ORDERS = By.CSS_SELECTOR, ".OrderFeed_list__OLh59"
    COUNTER_ALL_ORDERS = By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"
    COUNTER_DAILY_ORDERS = By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    ORDER_IN_WORK = By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class, 'text_type_digits-default')]"
    TEXT_ORDER_FEED = By.XPATH, "//h1[text()='Лента заказов']"
    DYNAMIC_ORDER_NUMBER_IN_FEED = By.XPATH, "//a[@href='/feed/{}']/parent::li"

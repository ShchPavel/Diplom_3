from selenium.webdriver.common.by import By


class ProfilePageLocators:
    BUTTON_SAVE_PROFILE = By.XPATH, "//button[text()='Сохранить']"
    BUTTON_PROFILE_ORDERS_HISTORY = By.XPATH, "//a[@href='/account/order-history']/parent::li"
    BUTTON_PROFILE_LOGOUT = By.XPATH, "//button[text()='Выход']"
    LIST_OF_MY_ORDERS = By.CSS_SELECTOR, ".OrderHistory_profileList__374GU"
    DYNAMIC_ORDER_LOCATOR_IN_HISTORY = By.XPATH, "//a[@href='/account/order-history/{}']/parent::li"


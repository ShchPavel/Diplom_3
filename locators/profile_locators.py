from selenium.webdriver.common.by import By


class ProfileLocators:
    BUTTON_SAVE_PROFILE = By.XPATH, "//button[text()='Сохранить']"
    BUTTON_PROFILE_ORDERS_HISTORY = By.XPATH, "//a[@href='/account/order-history']/parent::li"
    BUTTON_PROFILE_LOGOUT = By.XPATH, "//button[text()='Выход']"


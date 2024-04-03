from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    INPUT_EMAIL = By.XPATH, "//input[contains(@class,'input__textfield')]"
    BUTTON_RESET = By.XPATH, "//button[text() = 'Восстановить']"

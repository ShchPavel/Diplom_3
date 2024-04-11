from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    INPUT_EMAIL = By.XPATH, "//input[contains(@class,'input__textfield')]"
    BUTTON_RESET = By.XPATH, "//button[text() = 'Восстановить']"
    FORGOT_PAGE_INDICATOR = By.XPATH, "//h2[text()='Восстановление пароля']"
from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    BUTTON_RESET = By.XPATH, "//button[text() = 'Сохранить']"
    INPUT_PASSWORD = By.XPATH, "//input[@type = 'password']"
    ICON_EYE = By.XPATH, "//div[contains(@class, 'input_type_password')]/div[contains(@class, 'input__icon')]"
    INPUT_PASSWORD_AFTER_EYE_CLICK = By.CSS_SELECTOR, ".input__container>.input_status_active"

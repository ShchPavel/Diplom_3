from selenium.webdriver.common.by import By


class LoginPageLocators:
    BUTTON_RESET_PASSWORD = By.XPATH, '//a[text()=\'Восстановить пароль\']'
    INPUT_EMAIL = By.CSS_SELECTOR, '.input__textfield[type=\'text\']'
    INPUT_PASSWORD = By.CSS_SELECTOR, '.input__textfield[type=\'password\']'
    BUTTON_LOGIN = By.CSS_SELECTOR, '.button_button__33qZ0'

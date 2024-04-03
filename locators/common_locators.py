from selenium.webdriver.common.by import By


class CommonLocators:
    HEADER_PERSONAL_CABINET = By.CSS_SELECTOR, 'nav>a[href=\'/account\']'
    HEADER_ORDER_LIST = By.CSS_SELECTOR, 'a[href=\'/feed\']'
    HEADER_CONSTRUCTOR = By.XPATH, '//p[text()=\'Конструктор\']/parent::a'
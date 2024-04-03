from selenium.webdriver.common.by import By


class CommonLocators:
    HEADER_PERSONAL_CABINET = By.CSS_SELECTOR, 'nav>a[href=\'/account\']'
    HEADER_ORDER_LIST = By.CSS_SELECTOR, 'a[href=\'/feed\']'
    HEADER_CONSTRUCTOR = By.XPATH, '//p[text()=\'Конструктор\']/parent::a'
    HIDDEN_LOADER = By.CSS_SELECTOR, ".Modal_modal__P3_V5"
    HEADER_BAR = By.CSS_SELECTOR, ".AppHeader_header__nav__g5hnF"

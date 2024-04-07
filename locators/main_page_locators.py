from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_MAKE_ORDER = By.XPATH, "//button[text()= 'Оформить заказ']"
    POPUP_DETAIL_INGREDIENT = By.CSS_SELECTOR, ".Modal_modal_opened__3ISw4 > .Modal_modal__container__Wo2l_"
    INGREDIENT_FIRST_IN_LIST = By.CSS_SELECTOR, ".BurgerIngredient_ingredient__1TVf6"
    ICON_TO_CLOSE_POPUP = By.CSS_SELECTOR, ".Modal_modal__close_modified__3V5XS"
    BURGER_BASKET = By.CSS_SELECTOR, ".constructor-element_pos_top"
    INGREDIENT_FIRST_IN_LIST_COUNTER = By.CSS_SELECTOR, ".counter_counter__num__3nue1"
    POPUP_ORDER_REGISTERED = By.CSS_SELECTOR, ".Modal_modal_opened__3ISw4 > .Modal_modal__container__Wo2l_"
    TEXT_ORDER_STARTED_TO_COOKING = By.XPATH, "//section[contains(@class,'Modal_modal_opened__3ISw4')]//p[text()='Ваш заказ начали готовить']"

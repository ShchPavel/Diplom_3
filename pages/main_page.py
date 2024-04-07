from locators.common_locators import CommonLocators
from locators.main_page_locators import MainPageLocators
from locators.profile_page_locators import ProfilePageLocators
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage
import helpers
import allure


class MainPage(BasePage):
    @allure.step('Нажимаем на кнопку "Личный кабинет" и попадаем на страницу /login')
    def go_to_personal_cabinet(self):
        self.click_on_element(CommonLocators.HEADER_PERSONAL_CABINET)
        self.wait_and_find_element(ProfilePageLocators.BUTTON_PROFILE_ORDERS_HISTORY)

    @allure.step('Нажимаем на кнопку "Конструктор"')
    def go_to_constructor(self):
        self.click_on_element(CommonLocators.HEADER_CONSTRUCTOR)
        self.wait_and_find_element(MainPageLocators.BUTTON_MAKE_ORDER)

    @allure.step('Нажимаем на кнопку "Лента заказов"')
    def go_to_order_feed(self):
        self.click_on_element(CommonLocators.HEADER_ORDER_FEED)
        self.wait_and_find_element(FeedPageLocators.TEXT_ORDER_FEED)

    @allure.step('Нажимаем на первый ингредиент')
    def click_on_first_ingredient_in_list(self):
        self.click_on_element(MainPageLocators.INGREDIENT_FIRST_IN_LIST)
        self.wait_and_find_element(MainPageLocators.POPUP_DETAIL_INGREDIENT)

    @allure.step('Закрываем попап выбранного ингредиента')
    def close_ingredient_details_popup(self):
        self.click_on_element(MainPageLocators.ICON_TO_CLOSE_POPUP)

    @allure.step('Переносим драг энд дропом первый ингридиент на конструктор бургера ')
    def drag_n_drop_first_ingredient_to_burger_constructor(self):
        self.drag_n_drop(helpers.drag_and_drop_script, MainPageLocators.INGREDIENT_FIRST_IN_LIST, MainPageLocators.BURGER_BASKET)

    @allure.step('Нажимаем на кнопку "Оформить заказ"')
    def make_order(self):
        self.click_on_element(MainPageLocators.BUTTON_MAKE_ORDER)
        self.wait_and_find_element(MainPageLocators.POPUP_ORDER_REGISTERED)

    @allure.step('Проверяем наличие кнопки "Оформить заказ" на странице')
    def get_button_make_order(self):
        return self.wait_and_find_element(MainPageLocators.BUTTON_MAKE_ORDER)

    @allure.step('Проверяем наличие попап окна с деталями ингредиентта')
    def get_ingredient_popup(self):
        return self.wait_and_find_element(MainPageLocators.POPUP_DETAIL_INGREDIENT)

    @allure.step('Проверяем, закрылся ли попап')
    def check_ingredient_popup_closed(self):
        popup = self.find_elements(MainPageLocators.POPUP_DETAIL_INGREDIENT)
        if len(popup) == 0:
            return True
        else:
            return False

    @allure.step('Проверяем, что счетчик ингредиента увеличился')
    def has_counter_increased(self):
        element_text = self.find_element(MainPageLocators.INGREDIENT_FIRST_IN_LIST_COUNTER).text
        if int(element_text) > 0:
            return True
        else:
            return False

    @allure.step('Проверяем начало приготовления по наличию текста "Ваш заказ начали готовить"')
    def has_order_started_to_cook(self):
        if len(self.find_elements(MainPageLocators.TEXT_ORDER_STARTED_TO_COOKING)) > 0:
            return True
        else:
            return False

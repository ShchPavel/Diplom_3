from locators.common_locators import CommonLocators
from locators.main_page_locators import MainPageLocators
from locators.profile_locators import ProfileLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def go_to_personal_cabinet(self):
        self.click_on_element(CommonLocators.HEADER_PERSONAL_CABINET)
        self.wait_and_find_element(ProfileLocators.BUTTON_PROFILE_ORDERS_HISTORY)

    def go_to_constructor(self):
        self.click_on_element(CommonLocators.HEADER_CONSTRUCTOR)
        self.wait_and_find_element(MainPageLocators.BUTTON_MAKE_ORDER)

    def go_to_order_feed(self):
        self.click_on_element(CommonLocators.HEADER_ORDER_FEED)
        self.wait_and_find_element(MainPageLocators.TEXT_ORDER_FEED)

    def click_on_first_ingredient_in_list(self):
        self.click_on_element(MainPageLocators.INGREDIENT_FIRST_IN_LIST)
        self.wait_and_find_element(MainPageLocators.POPUP_DETAIL_INGREDIENT)

    def close_ingredient_details_popup(self):
        self.click_on_element(MainPageLocators.ICON_TO_CLOSE_POPUP)

    def drag_n_drop_element(self, script, element_locator, target_locator):
        self.drag_n_drop(script, element_locator, target_locator)

    def make_order(self):
        self.click_on_element(MainPageLocators.BUTTON_MAKE_ORDER)
        self.wait_and_find_element(MainPageLocators.POPUP_ORDER_REGISTERED)



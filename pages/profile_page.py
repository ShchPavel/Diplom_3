from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
from locators.login_page_locators import LoginPageLocators
import allure


class ProfilePage(BasePage):
    @allure.step('Нажимаем на кнопку "История заказов" и попадаем на страницу /account/order-history')
    def go_to_order_history_page(self):
        self.click_on_element(ProfilePageLocators.BUTTON_PROFILE_ORDERS_HISTORY)
        self.wait_and_find_element(ProfilePageLocators.LIST_OF_MY_ORDERS)

    @allure.step('Нажимаем на кнопку "Выход" для выхода из профиля')
    def logout(self):
        self.click_on_element(ProfilePageLocators.BUTTON_PROFILE_LOGOUT)
        self.wait_and_find_element(LoginPageLocators.BUTTON_RESET_PASSWORD)

    @allure.step('Получаем список моих заказов')
    def get_all_my_orders(self):
        return self.get_orders(ProfilePageLocators.LIST_OF_MY_ORDERS)

    @allure.step('Проверяем находится ли зарегистрированный заказ в списке моих заказов')
    def is_order_on_my_history_orders(self, order_locator, history_orders):
        link = None
        for _ in history_orders:
            link = self.wait_and_find_element(order_locator)

        if link is not None:
            return True
        else:
            return False

    @allure.step('Проверяем наличие кнопки "Сохранить"')
    def get_save_profile_button(self):
        return self.find_element(ProfilePageLocators.BUTTON_SAVE_PROFILE)

    @allure.step('Проверяем, есть ли на странице блок с моими заказами')
    def check_if_history_orders_exist(self):
        return self.find_element(ProfilePageLocators.LIST_OF_MY_ORDERS)

    @allure.step('Определяем локатор для блока с зарегистрированным заказом в истории заказов')
    def get_dynamic_order_locator_in_history(self, order_id):
        q_method, q_locator = ProfilePageLocators.DYNAMIC_ORDER_LOCATOR_IN_HISTORY
        locator = q_method, q_locator.format(order_id)
        return locator

from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
from locators.login_page_locators import LoginPageLocators
import allure

class ProfilePage(BasePage):
    @allure.step('Нажимаем на кнопку "История заказов" и попадаем на страницу /account/order-history')
    def go_to_order_history_page(self):
        self.click_on_element(ProfilePageLocators.BUTTON_PROFILE_ORDERS_HISTORY)

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

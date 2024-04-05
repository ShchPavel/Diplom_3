from pages.base_page import BasePage
from locators.profile_locators import ProfileLocators
from locators.login_page_locators import LoginPageLocators


class ProfilePage(BasePage):
    def go_to_order_history_page(self):
        self.click_on_element(ProfileLocators.BUTTON_PROFILE_ORDERS_HISTORY)

    def logout(self):
        self.click_on_element(ProfileLocators.BUTTON_PROFILE_LOGOUT)
        self.wait_and_find_element(LoginPageLocators.BUTTON_RESET_PASSWORD)

    def open_order_history(self):
        self.click_on_element(ProfileLocators.BUTTON_PROFILE_ORDERS_HISTORY)

    def is_order_exist_in_history(self, locator):
        self.has_element_in_list(locator, ProfileLocators.LIST_OF_MY_ORDERS)





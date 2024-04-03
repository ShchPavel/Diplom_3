from locators.common_locators import CommonLocators
from locators.profile_locators import ProfileLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def go_to_personal_cabinet(self):
        self.click_on_element(CommonLocators.HEADER_PERSONAL_CABINET)
        self.wait_and_find_element(ProfileLocators.BUTTON_PROFILE_ORDERS_HISTORY)


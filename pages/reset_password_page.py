from pages.base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordPageLocators
from helpers import DataGenerator
import allure

class ResetPasswordPage(BasePage):
    def fill_password_by_random_text_and_return_text(self):
        password = DataGenerator.generate_random_string()
        self.set_element_input(ResetPasswordPageLocators.INPUT_PASSWORD, password)
        return password

    def click_on_eye_icon(self):
        self.click_on_element(ResetPasswordPageLocators.ICON_EYE)

    def is_email_input_changed_after_clicking_on_eye(self):
        if self.wait_and_find_element(ResetPasswordPageLocators.INPUT_PASSWORD_AFTER_EYE_CLICK) is not None:
            return True

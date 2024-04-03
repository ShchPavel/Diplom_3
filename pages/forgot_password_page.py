from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from locators.reset_password_page_locators import ResetPasswordPageLocators
from data import Urls
from helpers import DataGenerator


class ForgotPasswordPage(BasePage):

    def fill_email(self):
        self.click_on_element(ForgotPasswordPageLocators.INPUT_EMAIL)
        self.set_element_input(ForgotPasswordPageLocators.INPUT_EMAIL, DataGenerator.generate_random_email())

    def click_reset_button(self):
        self.click_on_element(ForgotPasswordPageLocators.BUTTON_RESET)
        self.wait_and_find_element(ResetPasswordPageLocators.BUTTON_RESET)
from pages.base_page import BasePage
from data import Urls
from locators.login_page_locators import LoginPageLocators
from locators.forgot_password_page_locators import ForgotPasswordPageLocators


class LoginPage(BasePage):

    def open_login_page(self):
        self.open_page(Urls.LOGIN_URL)
        self.wait_and_find_element(LoginPageLocators.BUTTON_RESET_PASSWORD)

    def go_to_reset_password_page(self):
        self.click_on_element(LoginPageLocators.BUTTON_RESET_PASSWORD)
        self.wait_and_find_element(ForgotPasswordPageLocators.INPUT_EMAIL)

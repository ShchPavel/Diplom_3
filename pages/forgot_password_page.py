from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from locators.reset_password_page_locators import ResetPasswordPageLocators
from helpers import DataGenerator
import allure


class ForgotPasswordPage(BasePage):
    @allure.step('Заполняем поле Email')
    def fill_email(self):
        self.click_on_element(ForgotPasswordPageLocators.INPUT_EMAIL)
        self.set_element_input(ForgotPasswordPageLocators.INPUT_EMAIL, DataGenerator.generate_random_email())

    @allure.step('Нажимаем на кнопку "Восстановить"')
    def click_reset_button(self):
        self.click_on_element(ForgotPasswordPageLocators.BUTTON_RESET)
        self.wait_and_find_element(ResetPasswordPageLocators.BUTTON_RESET)

    @allure.step('Проверяем что на странице есть текст "Восстановление пароля"')
    def get_forgot_password_page_indicator_text(self):
        return self.get_element_value_using_wait(ForgotPasswordPageLocators.FORGOT_PAGE_INDICATOR)

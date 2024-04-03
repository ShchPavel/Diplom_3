import time
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from data import Urls


class TestResetPassword:

    def test_reset_password_button_redirect(self, driver):
        page = LoginPage(driver)
        page.open_login_page()
        page.go_to_reset_password_page()
        assert driver.current_url == Urls.FORGOT_PASSWORD_URL

    def test_reset_password_fill_email_redirect(self, driver):
        page = LoginPage(driver)
        page.open_login_page()
        page.go_to_reset_password_page()

        page = ForgotPasswordPage(driver)
        page.fill_email()
        page.click_reset_button()
        assert driver.current_url == Urls.RESET_PASSWORD_URL

    def test_new_input_password_visible_and_colored(self, driver):
        page = LoginPage(driver)
        page.open_login_page()
        page.go_to_reset_password_page()

        page = ForgotPasswordPage(driver)
        page.fill_email()
        page.click_reset_button()

        page = ResetPasswordPage(driver)
        page.fill_password_by_random_text_and_return_text()
        page.click_on_eye_icon()
        assert page.is_email_input_changed_after_clicking_on_eye() is True

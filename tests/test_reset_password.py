from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
import allure


class TestResetPassword:
    @allure.title('Проверка успешного перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_reset_password_button_redirect(self, driver):
        page = LoginPage(driver)
        page.go_to_login_page()
        page.click_on_reset_password_button()
        assert ForgotPasswordPage(driver).get_forgot_password_page_indicator_text() == 'Восстановление пароля'

    @allure.title('Проверка корректно редиректа после ввода почты и клика по кнопке «Восстановить»,')
    def test_reset_password_fill_email_redirect(self, driver):
        page = LoginPage(driver)
        page.go_to_login_page()
        page.click_on_reset_password_button()
        page = ForgotPasswordPage(driver)
        page.fill_email()
        page.click_reset_button()

        assert ResetPasswordPage(driver).get_reset_password_page_save_button() is not None

    @allure.title('Проверка, что при клике по кнопке "показать/скрыть пароль" поле email подсвечивается.')
    def test_new_input_password_visible_and_colored(self, driver):
        page = LoginPage(driver)
        page.go_to_login_page()
        page.click_on_reset_password_button()

        page = ForgotPasswordPage(driver)
        page.fill_email()
        page.click_reset_button()

        page = ResetPasswordPage(driver)
        page.fill_password_by_random_text()
        page.click_on_eye_icon()
        assert page.is_email_input_changed_after_clicking_on_eye() is True

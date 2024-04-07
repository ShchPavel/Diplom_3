import allure
from data import Urls
from pages.main_page import MainPage
from pages.feed_page import FeedPage


class TestMainFunctional:
    @allure.title('Проверка успешного редиректа при клике на "Конструктор"')
    def test_redirect_to_constructor_success(self, temp_user_logged_in__return_driver):
        driver = temp_user_logged_in__return_driver
        page = MainPage(driver)
        page.go_to_constructor()
        assert page.get_button_make_order() is not None

    @allure.title('Проверка успешного редиректа при клике на "Лента заказов"')
    def test_redirect_to_order_feed_success(self, temp_user_logged_in__return_driver):
        driver = temp_user_logged_in__return_driver
        page = MainPage(driver)
        page.go_to_order_feed()
        assert FeedPage(driver).get_text_feed_indicator() is not None

    @allure.title('Проверка появления всплывающего окна с деталями при клике на ингредиент')
    def test_choose_ingredient_open_popup_success(self, temp_user_logged_in__return_driver):
        driver = temp_user_logged_in__return_driver
        page = MainPage(driver)
        page.go_to_constructor()
        page.click_on_first_ingredient_in_list()
        assert page.get_ingredient_popup() is not None

    @allure.title('Проверка корректного закрытия всплывающего окна с деталями при нажатии на крестик')
    def test_ingredient_popup_closing_success(self, temp_user_logged_in__return_driver):
        driver = temp_user_logged_in__return_driver
        page = MainPage(driver)
        page.go_to_constructor()
        page.click_on_first_ingredient_in_list()
        page.close_ingredient_details_popup()
        assert page.check_ingredient_popup_closed() is True

    @allure.title('Проверка увеличения счетчика ингредиента при добавлении ингредиента в заказ')
    def test_add_ingredient_increase_counter_success(self, temp_user_logged_in__return_driver):
        driver = temp_user_logged_in__return_driver
        page = MainPage(driver)
        page.go_to_constructor()
        page.drag_n_drop_first_ingredient_to_burger_constructor()
        assert page.has_counter_increased() is True

    @allure.title('Проверка возможности оформления заказа')
    def test_order_registration_success(self, temp_user_logged_in__return_driver):
        driver = temp_user_logged_in__return_driver
        page = MainPage(driver)
        page.go_to_constructor()
        page.drag_n_drop_first_ingredient_to_burger_constructor()
        page.make_order()
        assert page.has_order_started_to_cook() is True


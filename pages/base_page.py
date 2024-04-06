from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """ Класс, описывающий взаимодействия с элементами. """

    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).perform()
        return element

    def click_on_element(self, locator):
        element = self.wait_and_find_element(locator)
        element.click()

    def set_element_input(self, locator, text):
        self.click_on_element(locator)
        element = self.wait_and_find_element(locator)
        element.send_keys(text)

    def open_page(self, url):
        self.driver.get(url)

    def drag_n_drop(self, drag_and_drop_script, element, target_element):
        element = self.driver.find_element(*element)
        target_element = self.driver.find_element(*target_element)
        self.driver.execute_script(drag_and_drop_script, element, target_element)

    def get_orders(self, locator):
        return self.driver.find_elements(*locator)

    def get_element_value(self, locator):
        self.wait_and_find_element(locator)
        value = self.driver.find_element(*locator).text
        return value

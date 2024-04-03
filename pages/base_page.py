from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import selenium

class BasePage:
    """ Класс, описывающий взаимодействия с элементами. """

    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
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

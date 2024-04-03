import random
import string

from selenium import webdriver


class WebDriverFactory:
    @staticmethod
    def get_web_driver(browser_name):
        if browser_name == 'firefox':
            return webdriver.Firefox()
        elif browser_name == 'chrome':
            return webdriver.Chrome()
        else:
            raise ValueError('Unknown browser name, you can use only "firefox" or "chrome"')


class DataGenerator:
    @staticmethod
    def generate_random_string():
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(5))
        return random_string

    @staticmethod
    def generate_random_email():
        return f'{DataGenerator.generate_random_string()}@{DataGenerator.generate_random_string()}.{DataGenerator.generate_random_string()}'

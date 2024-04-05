import random
import string

import requests
from selenium import webdriver

from data import Urls, Ingredient


class WebDriverFactory:
    @staticmethod
    def get_web_driver(browser_name):
        if browser_name == 'firefox':
            driver = webdriver.Firefox()
            driver.set_window_size(1920, 1080)
            return driver
        elif browser_name == 'chrome':
            driver = webdriver.Chrome()
            driver.set_window_size(1920, 1080)
            return driver
        else:
            raise ValueError('Unknown browser name, you can use only "firefox" or "chrome"')


class DataGenerator:
    @staticmethod
    def generate_random_string():
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(6))
        return random_string

    @staticmethod
    def generate_random_email():
        return f'{DataGenerator.generate_random_string()}@{DataGenerator.generate_random_string()}.{DataGenerator.generate_random_string()}'


class RegisterUser:
    @staticmethod
    def register_new_random_user():
        payload = {
            "email": DataGenerator.generate_random_email(),
            "password": DataGenerator.generate_random_string(),
            "name": DataGenerator.generate_random_string()
        }

        response = requests.post(Urls.API_REGISTER_USER, data=payload)
        return response, payload


class DeleteUser:
    @staticmethod
    def delete_user(token):
        bearer_token = f'Bearer {token}'
        headers = {"Authorization": bearer_token}
        response = requests.delete(Urls.API_USER_BASIC, headers=headers)
        return response


class CreateOrder:
    @staticmethod
    def create_order(token):
        bearer_token = f'Bearer {token}'
        headers = {"Authorization": bearer_token}
        payload = {"ingredients": Ingredient.KNOWN_INGREDIENT}
        response = requests.post(Urls.API_CREATE_ORDER, headers=headers, data=payload)
        return response


drag_and_drop_script = """
var source = arguments[0];
var target = arguments[1];
var event = document.createEvent('MouseEvent');
event.initMouseEvent('dragstart', true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
source.dispatchEvent(event);
event = document.createEvent('MouseEvent');
event.initMouseEvent('dragenter', true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
target.dispatchEvent(event);
event = document.createEvent('MouseEvent');
event.initMouseEvent('dragover', true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
target.dispatchEvent(event);
event = document.createEvent('MouseEvent');
event.initMouseEvent('drop', true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
target.dispatchEvent(event);
event = document.createEvent('MouseEvent');
event.initMouseEvent('dragend', true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
source.dispatchEvent(event);
"""
import random
import string

import requests
from selenium import webdriver
from data import Urls


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

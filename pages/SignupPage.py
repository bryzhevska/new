from selenium.webdriver.common.by import By
from webium import Find, Finds, BasePage


class SignUpPage(BasePage):
    path = "/"
    def __init__(self, url, driver):
        super(SignUpPage, self).__init__(url, driver)



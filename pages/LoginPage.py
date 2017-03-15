from selenium.webdriver.common.by import By
from webium import Find, Finds, BasePage
import ConfigParser
from hamcrest import *

class LoginPage(BasePage):
    path = "/"
    config = ConfigParser.ConfigParser()
    config.read('default.cfg')
    login_field = Find(by=By.NAME, value="_username")
    password_field = Find(by=By.NAME, value="_password")
    submit_login_form_button = Find(by=By.CSS_SELECTOR, value="div.login-buttons > button")
    forgot_password_link = Find(by=By.CSS_SELECTOR,value='href="/account/forgot-password"')
    create_account_link = Find(by=By.CSS_SELECTOR, value='href="/account/registration"')
    some_field = Find(by=By.CSS_SELECTOR,value="#sidebar > div > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > form > div > input")
    page_title = "Roxot | Publisher panel"

    def login(self,login,password):
        self.login_field.send_keys(login)
        self.password_field.send_keys(password)
        self.submit_login_form_button.click()

    def check_login_form_is_displayed(self):
        assert_that(self.login_field.is_displayed())
        assert_that(self.password_field.is_displayed())
        assert_that(self.submit_login_form_button.is_displayed())
        assert_that(self._driver.title == self.page_title)


    def __init__(self, url, driver):
        super(LoginPage, self).__init__(url=url, driver=driver)



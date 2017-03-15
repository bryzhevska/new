from selenium.webdriver.common.by import By
from webium import Find, Finds, BasePage


class SignUpPage(BasePage):
    path = "/account/registration"

    email_field = Find(by=By.ID, value="email")
    password_field = Find(by=By.ID, value="password_first")
    password_confirmation_field = Find(by=By.ID, value="password_second")
    sign_up_submit_button = Find(by=By.ID, value="submit")
    page_title = "Roxot | Publisher panel"

    def check_i_am_on_sign_up_page(self):
        assert (self._driver.current_url == self.path)
        assert (self._driver.title == self.page_title)

    def check_sign_up_form_displayed(self):
        assert (self.email_field.is_displayed())
        assert (self.password_field.is_displayed())
        assert (self.password_confirmation_field.is_displayed())
        assert (self.sign_up_submit_button.is_displayed())

    def __init__(self, url, driver):
        super(SignUpPage, self).__init__(url=url, driver=driver)

    def sign_up_to_system(self, email, password):
        self.email_field.send_keys(email)
        self.password_field.send_keys(password)
        self.password_confirmation_field.send_keys(password)
        self.sign_up_submit_button.click()

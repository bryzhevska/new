from selenium.webdriver.common.by import By
from webium import Find, Finds, BasePage

class ForgotPasswordPage(BasePage):
    path = "/account/registration"

    email_field = Find(by=By.ID, value="email")
    recover_password_submit_button = Find(by=By.ID, value="submit")
    page_title = "Roxot | Publisher panel"

    def check_i_am_on_sign_up_page(self):
        assert (self._driver.current_url == self.path)
        assert (self._driver.title == self.page_title)

    def check_recover_password_form_displayed(self):
        assert (self.email_field.is_displayed())
        assert (self.recover_password_submit_button.is_displayed())

    def __init__(self, url, driver):
        super(ForgotPasswordPage, self).__init__(url=url, driver=driver)

    def fill_recover_password_form(self,email):
        self.email_field.send_keys(email)
        self.recover_password_submit_button.click()


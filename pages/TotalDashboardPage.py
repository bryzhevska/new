from selenium.webdriver.common.by import By
from webium import Find, Finds, BasePage


# from hamcrest import *


class TotalDashboardPage(BasePage):
    path = "/"
    page_title = "Total Dashboard"
    username = Find(by=By.CLASS_NAME, value="hidden-xs")
    down_arrow = Find(by=By.CSS_SELECTOR, value="#header > div > ul > li.dropdown.navbar-user > a > b")
    log_out_link = "Log Out"

    def assert_page_is_displayed(self):
        print(self._driver.title)
        assert (self._driver.title == self.page_title), "Page title %r does not correspond Total Dashboard" % str(
            self._driver.title)

    def __init__(self, url, driver):
        super(TotalDashboardPage, self).__init__(url=url, driver=driver)

    def assert_username_is_displayed(self, displayed_name):
        assert (self.username.text == displayed_name), "Displayed username %r does not correspond root" % str(
            displayed_name)

    def sign_out(self):
        self.down_arrow.click()
        self._driver.find_element_by_partial_link_text(self.log_out_link).click()

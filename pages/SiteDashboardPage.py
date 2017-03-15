from selenium.webdriver.common.by import By
from webium import Find, Finds, BasePage


class SiteDashboardPage(BasePage):
    path = "/"
    def __init__(self, url, driver):
        super(SiteDashboardPage, self).__init__(url=url, driver=driver)



from selenium.webdriver.common.by import By
from webium import Find, Finds, BasePage


class BidderDashboardPage(BasePage):
    path = "/"
    def __init__(self, url, driver):
        super(BidderDashboardPage, self).__init__(url=url, driver=driver)



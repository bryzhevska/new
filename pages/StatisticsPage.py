from selenium.webdriver.common.by import By
from webium import Find, Finds, BasePage


class StatisticsPage(BasePage):
    path = "/"
    def __init__(self, url, driver):
        super(StatisticsPage, self).__init__(url, driver)



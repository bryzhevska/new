from pip.utils import logging
from selenium import webdriver
import ConfigParser


def before_all(context):
    config = ConfigParser.ConfigParser()
    config.read('default.cfg')
    context.url = config.get('basic', 'base_url')
    context.driver = webdriver.Chrome()
    #context.driver.maximize_window()
    if not context.config.log_capture:
        logging.basicConfig(level=logging.DEBUG)


#def after_all(context):
#    context.driver.quit()
def after_scenario(context,scenario):
    context.driver.quit()

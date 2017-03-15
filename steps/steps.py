from behave import given, when, then
import ConfigParser
from pages.LoginPage import LoginPage
from pages.TotalDashboardPage import TotalDashboardPage

config = ConfigParser.ConfigParser()
config.read('default.cfg')


@given(u'I am registered "{user}"')
def step_impl(context, user):
    pass


@given(u'I am signed in to system as "{user}"')
@when(u'I sign in to system as "{user}"')
def step_impl(context, user):
    context.user_name = config.get(user, 'user')
    login = config.get(user, 'user')
    password = config.get(user, 'password')
    page = LoginPage(context.url, context.driver)
    page.open()
    page.login(login, password)


@then(u'I should be signed in as "{user}" successfully')
def step_impl(context, user):
    page = TotalDashboardPage(context.url, context.driver)
    page.assert_page_is_displayed()
    page.assert_username_is_displayed(context.user_name)


@when(u'I signed out from the system')
def step_impl(context):
    page = TotalDashboardPage(context.url, context.driver)
    page.sign_out()


@then(u'I should be signed out successfully')
def step_impl(context):
    page = LoginPage(context.url, context.driver)
    page.check_login_form_is_displayed()

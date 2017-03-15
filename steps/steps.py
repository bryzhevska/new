from behave import given, when, then
import ConfigParser
from pages.LoginPage import LoginPage
from pages.TotalDashboardPage import TotalDashboardPage
from pages.SignUpPage import SignUpPage
from pages.ForgotPasswordPage import ForgotPasswordPage

config = ConfigParser.ConfigParser()
config.read('default.cfg')


@given(u'I am registered "{user}"')
def step_impl(context, user):
    context.email = config.get('publisher', 'email')

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

@given(u'I am unregistered user')
def step_impl(context):
    email = config.get('new_user', 'email')
    password = config.get('new_user', 'password')
    context.email = email
    context.password =password

@when(u'I sign up to the system')
def step_impl(context):
    page=LoginPage(context.url,context.driver)
    page.sign_up()
    page = SignUpPage(context.url, context.driver)
    page.open()
    page.sign_up_to_system(context.email,context.password)
    page.check_i_am_on_sign_up_page()
    page.check_sign_up_form_displayed()

@then(u'I should be signed up successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should be signed up successfully')

@when(u'I forgot password')
def step_impl(context):
    page = LoginPage(context.url,context.driver)
    page.restore_password()

@when(u'I follow restore password instructions')
def step_impl(context):
    page=ForgotPasswordPage(context.url,context.driver)
    page.fill_recover_password_form(context.email)

@then(u'I should get my new password')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should get my new password')


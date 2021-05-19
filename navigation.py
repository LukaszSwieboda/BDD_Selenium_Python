from behave import *
from selenium import webdriver

use_step_matcher('re')

@given('I am on the homepage')
def step_impl(context):
    context.browser = webdriver.Chrome('/use/your/Chrome/driver/path')
    context.browser.get('http://zero.webappsecurity.com/index.html')
    
@then('I am on the login page')
def step_impl(context):
    expected_url = 'http://zero.webappsecurity.com/login.html'
    assert context.browser.current_url == expected_url

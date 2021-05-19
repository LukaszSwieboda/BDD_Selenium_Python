from behave import *

use_step_matcher('re')

@when('I click on sign in button')
def step_impl(context):
    link = context.browser.find_element_by_id("signin_button")
    link.click()

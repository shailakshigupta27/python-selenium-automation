from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target.com')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when('Click on cart icon')
def cart(context):
    context.driver.find_element(By.CSS_SELECTOR,'[aria-label="cart 0 items"]').click()
    sleep(3)

@then('“Your cart is empty” message is shown')
def message(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.XPATH,"//h1[contains(@class, 'styles_ndsHeading')]").text
    assert expected_text in actual_text, f'Error, expected {expected_text} not in actual {actual_text}'

@when('Click account drop-down')
def account_dropdown(context):
    context.driver.find_element(By.CSS_SELECTOR, '#account-sign-in').click()
    sleep(3)

@when('Click sign in or create account')
def create_account(context):
    context.driver.find_element(By.CSS_SELECTOR,'[data-test="accountNav-signIn"]').click()
    sleep(3)


@then('"Enter your email or mobile number to continue" message is shown')
def account_creation_msg(context):
    expected_text = 'Enter your email or mobile number to continue'
    actual_text = context.driver.find_element(By.XPATH, "//p[@class='h-margin-b-x6 h-text-md h-text-center']").text
    assert expected_text in actual_text, f'Error, expected {expected_text} not in actual {actual_text}'





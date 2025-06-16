from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on cart icon')
def cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '[aria-label="cart 0 items"]').click()
    sleep(3)


@when('Click account drop-down')
def account_dropdown(context):
    context.driver.find_element(By.CSS_SELECTOR, '#account-sign-in').click()
    sleep(3)


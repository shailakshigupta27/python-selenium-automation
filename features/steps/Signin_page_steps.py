from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click sign in or create account')
def create_account(context):
    context.driver.find_element(By.CSS_SELECTOR,'[data-test="accountNav-signIn"]').click()
    sleep(3)
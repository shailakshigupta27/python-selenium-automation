from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_SUBMIT = (By.CSS_SELECTOR, "button[data-test*='@web/Search/SearchButton']")
SEARCH_INPUT = (By.ID, 'search')


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(5)


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    #search.clear()
    search.send_keys(search_word)
    sleep(4)
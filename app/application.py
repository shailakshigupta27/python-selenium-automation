from selenium.webdriver.support.wait import WebDriverWait

from pages.cart_page import Cart
from pages.main_page import MainPage
from pages.base_page import Page
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from selenium.webdriver.support import expected_conditions as EC


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.header = Header(driver)
        self.cart_page = Cart(driver)
        self.wait = WebDriverWait(driver, 10)





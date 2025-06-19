from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class Cart(Page):
    Empty_cart_msg = (By.XPATH, "//h1[contains(@class, 'styles_ndsHeading')]")

    def empty_cart(self):
        expected_text = 'Your cart is empty'
        actual_text = self.find_element(*self.Empty_cart_msg).text
        #sleep(5)
        assert expected_text in actual_text, f'Error, expected {expected_text} not in actual {actual_text}'





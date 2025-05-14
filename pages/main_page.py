from .base_page import BasePage
from locators import MainPageLocators
import time


class MainPage(BasePage):
    def confirm_region(self):
        self.click(MainPageLocators.REGION_CONFIRM_BUTTON)

    def open_search(self):
        self.click(MainPageLocators.SEARCH_CONTAINER)
        time.sleep(1)  # Ждем анимацию

    def search_for_product(self, product_name):
        self.send_keys(MainPageLocators.SEARCH_INPUT, product_name)
        self.click(MainPageLocators.SEARCH_BUTTON)

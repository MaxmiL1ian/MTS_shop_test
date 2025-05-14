from pages.base_page import BasePage
from locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def is_loaded(self):
        return self.wait_for_element(ProductPageLocators.PRODUCT_CONTAINER)

    def take_screenshot(self, filename):
        time.sleep(1)  # Даем время для загрузки
        self.driver.save_screenshot(filename)

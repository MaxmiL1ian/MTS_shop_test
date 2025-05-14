from .base_page import BasePage
from locators import ProductListingPageLocators


class ProductListingPage(BasePage):
    def click_first_product(self):
        self.click(ProductListingPageLocators.FIRST_PRODUCT)

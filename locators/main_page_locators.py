from selenium.webdriver.common.by import By


class MainPageLocators:
    REGION_CONFIRM_BUTTON = (By.CSS_SELECTOR, "button.confirm-region__btn")
    SEARCH_CONTAINER = (By.CSS_SELECTOR, "div.header-block__search-container > div > div")
    SEARCH_INPUT = (By.CSS_SELECTOR, "#search-popup-field")
    SEARCH_BUTTON = (By.CSS_SELECTOR,
                     "#modals-container > div > div > div.v--modal-box.v--modal-box--search > div > div > div.search-popup-result-block__header > form > button > span")

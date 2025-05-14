import undetected_chromedriver as UC
from pages import MainPage
from pages import ProductListingPage
from pages import ProductPage
import os


def main():
    driver = None
    try:
        driver = UC.Chrome()

        # Инициализация страниц
        main_page = MainPage(driver)
        product_listing_page = ProductListingPage(driver)
        product_page = ProductPage(driver)

        # Открытие сайта
        driver.get("https://shop.mts.ru/")

        # Подтверждение региона
        main_page.confirm_region()

        # Поиск товара
        main_page.open_search()
        main_page.search_for_product("AirPods 4")

        # Открытие карточки товара
        product_listing_page.click_first_product()

        # Скриншот
        product_page.is_loaded()
        product_page.take_screenshot("airpods_4_mts.png")
        print("Скриншот сохранен как airpods_4_mts.png")


    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        if driver is not None:
            try:
                driver.quit()
            except Exception as e:
                print(f"Ошибка при закрытии драйвера:  {e}")
            os._exit(0)


if __name__ == "__main__":
    main()

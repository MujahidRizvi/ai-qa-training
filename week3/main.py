from playwright.sync_api import sync_playwright

from test_toolshop_week3 import (
    test_products_display_correct_quantity,
    api_test_category_search,
)

from helpers import read_quantities, open_website


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        try:
            # Run quantity tests
            open_website(page)
            for quantity in read_quantities("data.csv"):
                try:
                    test_products_display_correct_quantity(page, quantity)
                    print(f"PASS: quantity test ({quantity})")
                except Exception as error:
                    print(f"FAIL: quantity test ({quantity}) - {error}")

            # Run API category search using the same page
            try:
                print("CALLING API TEST")
                api_test_category_search(page)
                print("PASS: api_test_category_search")
            except Exception as error:
                print(f"FAIL: api_test_category_search - {error}")

        finally:
            browser.close()


if __name__ == "__main__":
    main()

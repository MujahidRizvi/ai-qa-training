from playwright.sync_api import sync_playwright
from toolshop_tests_week1 import test_browse_category, test_product_details


def main():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        try:
            test_browse_category(page)
            print("PASS: test_browse_category")
        except Exception as error:
            print(f"FAIL: test_browse_category - {error}")

        try:
            test_product_details(page)
            print("PASS: test_product_details")
        except Exception as error:
            print(f"FAIL: test_product_details - {error}")

        finally:
            browser.close()


if __name__ == "__main__":
    main()

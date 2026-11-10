from playwright.sync_api import sync_playwright
from toolshop_tests_week2 import (
    TC_001_test_search_functionality,
    TC_004_test_search_validation_msg,
    TC_009_test_sorting_high_to_low,
    TC_0012_test_cart_manual_input,
    TC_0014_test_cart_updation,
    TC_0017_test_contact_us_mandatory_fields,
)


def main():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        try:
            TC_001_test_search_functionality(page)
            print("PASS: TC_001_test_search_functionality")
        except Exception as error:
            print(f"FAIL: TC_001_test_search_functionality - {error}")

        try:
            TC_004_test_search_validation_msg(page)
            print("PASS: TC_004_test_search_validation_msg")
        except Exception as error:
            print(f"FAIL: TC_004_test_search_validation_msg - {error}")

        try:
            TC_009_test_sorting_high_to_low(page)
            print("PASS: test_sorting_high_to_low")
        except Exception as error:
            print(f"FAIL: test_sorting_high_to_low - {error}")

        try:
            TC_0012_test_cart_manual_input(page)
            print("PASS: test_cart_manual_input")
        except Exception as error:
            print(f"FAIL: test_cart_manual_input - {error}")

        try:
            TC_0014_test_cart_updation(page)
            print("PASS: test_cart_updation")
        except Exception as error:
            print(f"FAIL: test_cart_updation - {error}")

        try:
            TC_0017_test_contact_us_mandatory_fields(page)
            print("PASS: test_contact_us_mandatory_fields")
        except Exception as error:
            print(f"FAIL: test_contact_us_mandatory_fields - {error}")

        finally:
            browser.close()


if __name__ == "__main__":
    main()

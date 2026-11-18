# The web addresses, and the two steps every page test repeats.
# This site marks its elements with data-test attributes, so that is how we find them.

from playwright.sync_api import expect, sync_playwright
import csv
from pathlib import Path
from test_data import testData

SHOP_URL = testData["BASE_URL"]
API_URL = testData["API_URL"]


def initialize_browser():
    playwright = sync_playwright().start()
    browser = None
    try:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        return playwright, browser, page
    except Exception:
        cleanup_browser(playwright, browser)
        raise


def cleanup_browser(playwright, browser):
    try:
        if browser is not None:
            browser.close()
    finally:
        playwright.stop()


def initialize_api():
    playwright = sync_playwright().start()
    api = None
    try:
        api = playwright.request.new_context(base_url=API_URL)
        return playwright, api
    except Exception:
        cleanup_api(playwright, api)
        raise


def cleanup_api(playwright, api):
    try:
        if api is not None:
            api.dispose()
    finally:
        playwright.stop()


def open_website(page):

    max_retries = 3

    for attempt in range(1, max_retries + 1):

        try:
            print(f"Opening website - Attempt {attempt}")

            page.goto(SHOP_URL, wait_until="domcontentloaded")

            pliers_image = page.locator(testData["IMG_NAME"])

            expect(pliers_image).to_be_visible(timeout=15000)

            print(testData["IMG_VISIBLE_MSG"])

            return

        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")

            if attempt == max_retries:
                raise Exception("Website failed to load after 3 attempts") from e


def read_quantities(file_name):
    file_path = Path(__file__).parent / file_name

    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [int(row["quantity"]) for row in reader]

prompt = """
*You as a senior automation tester, write test that runs once per row with parametrize like test_2 below:*

`import csv
from pathlib import Path
import pytest
from playwright.sync_api import expect

from helpers import cleanup_browser, initialize_browser, open_website, search_product, read_search_words

@pytest.mark.parametrize("search_word", read_search_words("search_words.csv"))
def test_search_shows_only_matching_products(search_word):
    playwright, browser, page = initialize_browser()
    try:
        open_website(page)
        search_product(page, search_word)

        product_names = page.locator('[data-test="product-name"]')
        expect(product_names.first).to_be_visible()
        expect(product_names.filter(has_not_text=search_word)).to_have_count(0)
    finally:
        cleanup_browser(playwright, browser)`

"""

**AI Response:**

# 1. helpers.py – CSV reader

*Add this function to your existing helpers file:
python*

`import csv
from pathlib import Path


def read_quantities(file_name):
    file_path = Path(__file__).parent / file_name

    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [int(row["quantity"]) for row in reader]`

# 2. test_quantity_ui.py

*This test runs once per CSV row (five executions).
python*

`import pytest
from playwright.sync_api import expect

from helpers import (
    cleanup_browser,
    initialize_browser,
    open_website,
    read_quantities,
)


@pytest.mark.parametrize("quantity", read_quantities("data.csv"))
def test_products_display_correct_quantity(quantity):
    playwright, browser, page = initialize_browser()

    try:
        open_website(page)

        quantity_input = page.locator('[data-test="quantity"]')
        quantity_input.fill(str(quantity))

        page.locator('[data-test="submit"]').click()

        product_names = page.locator('[data-test="product-name"]')

        expect(product_names.first).to_be_visible()

        expect(
            page.locator('[data-test="product-count"]')
        ).to_have_text(str(quantity))

    finally:
        cleanup_browser(playwright, browser)`
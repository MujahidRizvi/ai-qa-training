import requests

from playwright.sync_api import expect
from test_data import testData
from helpers import open_website


def test_products_display_correct_quantity(page, quantity):

    open_website(page)

    page.click(testData["PROD_NAME"])

    page.locator(testData["QTY"]).clear()

    page.locator(testData["QTY"]).fill(str(quantity))

    expect(page.locator(testData["QTY"])).to_have_value(str(quantity))


def api_test_category_search(page):
    response = requests.get(testData["API_SEARCH_URL"], timeout=15)

    assert response.status_code == 200
    print("API RESPONSE:", response.status_code)
    data = response.json()

    assert data[0]["name"] == testData["EXPECTED_NAME"]
    assert data[0]["slug"] == testData["EXPECTED_SLUG"]

    open_website(page)

    mypliers = page.locator(testData["PROD_NAME"]).nth(1)

    expect(mypliers).to_be_visible()

    actual_text = mypliers.inner_text().strip()
    expected_text = data[0]["name"].strip()

    print("Actual:", actual_text)
    print("Expected:", expected_text)

    assert actual_text == expected_text

    print("API test PASSED successfully")

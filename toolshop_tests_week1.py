from playwright.sync_api import sync_playwright, expect
from test_data import testData


def test_browse_category(page):

    page.goto(testData["BASE_URL"])
    page.click(testData["CATEGORY_MENU"])
    page.click(testData["HAND_TOOLS"])
    expect(page).to_have_title(testData["TITLE_TEXT"])
    print(testData["SUCCESS_TEXT_1"])
    product_count = page.locator(testData["PRODUCT_NAME"]).count()
    if product_count > 0:
        print(testData["SUCCESS_TEXT_2"])
        product_names = page.locator(testData["PRODUCT_NAME"])
        for name in product_names.all_inner_texts():
            product_name = name.strip()

            if not product_name:
                print(testData["FAILURE_MSG_1"])

                print(testData["ASSERT_TEXT"])


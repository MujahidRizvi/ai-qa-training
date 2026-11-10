from playwright.sync_api import expect
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


def test_product_details(page):

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
                print(testData["FAILURE_MSG_2"])

                print(testData["ASSERT_TEXT"])
        for name in product_names.all_inner_texts():
            product_name1 = name.strip()
            if name == testData["EXPECTED_PROD_TITLE"]:
                page.get_by_text(product_name1).click()
                expect(page.locator(testData["PDP_HEADING"])).to_have_text(
                    testData["EXPECTED_PROD_TITLE"]
                )
                expect(page.locator(testData["UNIT_PRICE"])).to_be_visible()
                expect(page.locator(testData["ADD_TO_CART"])).to_be_visible()
                print(testData["SUCCESS_TEXT_3"])


def test_add_to_cart(page):

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
                print(testData["FAILURE_MSG"])
            else:
                print(f"{product_name}")
        for name in product_names.all_inner_texts():
            product_name1 = name.strip()
            if name == testData["EXPECTED_PROD_TITLE"]:
                page.get_by_text(product_name1).click()
                expect(page.locator(testData["PDP_HEADING"])).to_have_text(
                    testData["EXPECTED_PROD_TITLE"]
                )
                expect(page.locator(testData["UNIT_PRICE"])).to_be_visible()
                expect(page.locator(testData["ADD_TO_CART"])).to_be_visible()
                print(testData["SUCCESS_TEXT_3"])
                expect(page.locator(testData["UNIT_PRICE"])).to_have_text(
                    testData["EXPECTED_PRICE"]
                )
                print(testData["SUCCESS_TEXT_4"])
                page.click(testData["ADD_TO_CART"])
                expect(page.locator(testData["CART_QNTY"])).to_have_text(
                    testData["EXPECTED_QNTY"]
                )
                print(testData["SUCCESS_TEXT_5"])
                page.click(testData["CART"])
                expect(page.locator(testData["PROD_TITLE"])).to_have_text(
                    testData["EXPECTED_PROD_TITLE"]
                )
                expect(page.locator(testData["PROD_QTY"])).to_have_value(
                    testData["EXPECTED_QNTY"]
                )
                expect(page.locator(testData["TOTAL_PRICE"])).to_have_text(
                    testData["EXPECTED_TOTAL_PRICE"]
                )
                print(testData["SUCCESS_TEXT_6"])

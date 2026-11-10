from playwright.sync_api import expect
from test_data import testData


def TC_001_test_search_functionality(page):

    page.goto(testData["BASE_URL"])
    page.click(testData["SEARCH_BOX"])
    page.locator(testData["SEARCH_BOX"]).fill(testData["SEARCH_KEYWORD"])
    page.click(testData["SEARCH_BUTTON"])

    product_names = page.locator(testData["PROD_NAME"])

    for product_name in product_names.all():
        expect(product_name).to_contain_text(testData["EXPECTED_PROD_NAME"])

    print(testData["SUCCESS_TEXT_1"])


def TC_004_test_search_validation_msg(page):

    page.goto(testData["BASE_URL"])
    page.click(testData["SEARCH_BOX"])
    page.locator(testData["SEARCH_BOX"]).fill(testData["INVALID_SEARCH_KEYWORD"])
    page.click(testData["SEARCH_BUTTON"])
    expect(page.locator(testData["NO_RESULT"])).to_have_text(testData["ASSERT_TEXT"])

    print(testData["SUCCESS_TEXT_2"])


def TC_009_test_sorting_high_to_low(page):

    page.goto(testData["BASE_URL"])
    page.locator(testData["SORT_DD"]).select_option(testData["HIGH_TO_LOW"])
    prices = page.locator(testData["PROD_PRICE"]).all_text_contents()

    price_list = []

    for price in prices:
        price_list.append(float(price.replace("$", "").strip()))
    if price_list == sorted(price_list, reverse=True):
        print("All prices are arranged in High to Low Order")
    else:
        print("Prices are NOT arranged in High to Low Order")


def TC_0012_test_cart_manual_input(page):

    page.goto(testData["BASE_URL"])
    page.click(testData["PROD_NAME"])
    page.locator(testData["QTY"]).clear()
    page.locator(testData["QTY"]).fill(testData["QTY_NUM"])
    page.click(testData["ADD_TO_CART"])
    expect(page.locator(testData["CART_QNTY"])).to_have_text(testData["QTY_NUM"])
    print(testData["SUCCESS_TEXT_3"])
    page.click(testData["CART"])
    page.click(testData["CART_REMOVE"])


def TC_0014_test_cart_updation(page):

    page.goto(testData["BASE_URL"])

    products = page.locator(testData["PROD_NAME"])
    count = 0

    for i in range(products.count()):

        products.nth(i).click()

        add_button = page.locator(testData["ADD_TO_CART"])

        if add_button.count() > 0 and add_button.is_enabled():

            add_button.click()
            count += 1

            if count == 2:
                break

        page.go_back()

    page.click(testData["CART"])
    qty = int(page.locator(testData["CART_QNTY"]).inner_text())
    page.click(testData["CART_REMOVE"])
    expect(page.locator(testData["CART_QNTY"])).to_have_text(str(qty - 1))
    print(testData["SUCCESS_TEXT_4"])


def TC_0017_test_contact_us_mandatory_fields(page):

    page.goto(testData["BASE_URL"])
    page.click(testData["CONTACT_US"])
    page.locator(testData["SEND_BTN"]).click()
    expect(page.locator(testData["FNAME_ERR"])).to_be_visible()
    expect(page.locator(testData["LNAME_ERR"])).to_be_visible()
    expect(page.locator(testData["EMAIL_ERR"])).to_be_visible()
    expect(page.locator(testData["SUB_ERR"])).to_be_visible()
    expect(page.locator(testData["MSG_ERR"])).to_be_visible()
    print(testData["SUCCESS_TEXT_5"])
    page.locator(testData["F_NAME"]).fill(testData["F_NAME_TXT"])
    expect(page.locator(testData["FNAME_ERR"])).to_be_hidden()
    expect(page.locator(testData["LNAME_ERR"])).to_be_visible()
    expect(page.locator(testData["EMAIL_ERR"])).to_be_visible()
    expect(page.locator(testData["SUB_ERR"])).to_be_visible()
    expect(page.locator(testData["MSG_ERR"])).to_be_visible()
    print(testData["SUCCESS_TEXT_6"])

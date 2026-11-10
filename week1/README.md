# ai-qa-training

## Playwright E-Commerce UI Automation
**Project Overview**

This project is an automated UI testing project built using Python and Playwright. It tests the basic shopping functionality of an e-commerce website through browser automation.

The purpose of this project is to verify that users can browse product categories, view product details, and successfully add products to their shopping cart.

The tests run in a Chromium browser using Playwright's synchronous API.

**Test Scenarios**

The project includes the following three test scenarios:

**1. Browse Category (test_browse_category)**

    Opens the e-commerce website.
    Navigates to the Category menu.
    Selects the Hand Tools category.
    Verifies that the expected page title is displayed.
    Checks that products are available in the selected category.
    Checks product names for empty values.

**2. Product Details (test_product_details)**

    Navigates to the Hand Tools category.
    Verifies that the product listing is displayed.
    Searches for the expected product.
    Opens the selected product.
    Verifies the product heading, unit price, and Add to Cart button.

**3. Add to Cart (test_add_to_cart)**

    Navigates to the Hand Tools category.
    Opens the expected product.
    Verifies the product details and expected unit price.
    Adds the product to the shopping cart.
    Verifies the cart quantity.
    Opens the shopping cart.
    Checks the product name, quantity, and total price.

**Technologies Used**

    Python – Programming language.
    Playwright – Browser automation and UI testing framework.
    Chromium – Browser used to execute automated tests.
    Pytest-style assertions – Playwright's expect() assertions for validating UI elements.

**Project Structure**

```text
Playwright-Project/
│
├── main.py
│   └── Contains the test functions and main execution logic.
│
├── test_data.py
│   └── Contains test data, URLs, locators, expected values,
│       and success/failure messages.
│
└── README.md
    └── Project documentation.
```
    

**Prerequisites**

Before running the project, make sure you have:

    Python 3.9 or later installed.
    pip package manager.
    A stable internet connection.
    Visual Studio Code or another Python IDE (optional).

**Installation and Setup**

**Step 1: Clone or Download the Project**

Download the project files and open the project folder in your preferred IDE or terminal.

**Step 2: Install Playwright**

Run the following command:
bash

pip install playwright

**Step 3: Install Playwright Browsers**

Install the Chromium browser:
bash

playwright install chromium

**Step 4: Verify Project Files**

Make sure both Python files are in the same project directory:

    main.py
    test_data.py

Also ensure that test_data.py contains all the required test data keys and values referenced in the test scripts.

**How to Run the Project**

Open a terminal in the project directory and execute:
bash

python main.py

The Chromium browser will launch in headed mode, and the tests will execute sequentially.

The terminal displays the execution status of each test:
text

PASS: test_browse_category
PASS: test_product_details
PASS: test_add_to_cart

If a test fails, the exception message is displayed:
text

FAIL: test_product_details - Error message

**Challenge Faced During Development**

One challenge I faced was handling multiple test scenarios independently.

Initially, I had difficulty organizing the try-except blocks correctly. When one test failed, I wanted the remaining tests to continue executing instead of stopping the entire test execution.

I resolved this by placing each test function inside its own try-except block. This allowed each test to report its individual PASS or FAIL status while allowing the remaining tests to execute.

Another important part of the implementation was using Playwright's expect() assertions to verify product details, prices, cart quantities, and total prices.

**Conclusion**

This project demonstrates basic e-commerce UI automation using Python and Playwright. It covers important shopping workflows, including category navigation, product validation, and cart functionality.

It also provides practical experience with browser automation, locators, assertions, test data management, and exception handling.
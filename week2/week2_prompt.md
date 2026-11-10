prompt = """
You as a senior SQA engineer, write testcases for the following Search Requirements.

The output should be a table with following columns:

ID
Req. No
Test Case
Pre Conditions
Steps
Expected Results
Priority

And here are the Search Requirements for which you have to write test cases:

Search

1.1 Customers can search by typing a word and clicking the search button, or by pressing Enter. Both should give the same products.

1.2 If nothing matches, the page should say so and show no products.

1.3 There's a small clear button next to the search box. Clicking it should empty the box and bring back the full list of products.
"""
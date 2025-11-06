
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage

def test_daraz_automation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Initialize page objects
        home = HomePage(page)
        results = SearchResultsPage(page)
        product = ProductPage(page)

        # Steps
        home.navigate()
        home.search_product("electronics")
        # results.apply_brand_filter()
        results.apply_price_filter(500, 5000)
        results.count_products()
        results.open_first_product()
        product.verify_free_shipping()

        browser.close()

if __name__ == "__main__":
    test_daraz_automation()

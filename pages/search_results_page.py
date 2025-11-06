class SearchResultsPage:
    def __init__(self, page):
        self.page = page
        self.sort_dropdown = 'div[class*="box--ujueT"]'  # sort menu
        self.high_to_low_option = "text=Price high to low"
        self.product_titles = "div[data-qa-locator='product-item']"

    def apply_sort_high_to_low(self):
        try:
            self.page.click(self.sort_dropdown)
            self.page.locator(self.high_to_low_option).click()
            self.page.wait_for_timeout(4000)
            print(" Applied 'Price: High to Low' sorting")
        except Exception as e:
            print(f" Could not apply sorting: {e}")
    
    def apply_price_filter(self, min_price, max_price):
        try:
            self.page.wait_for_timeout(3000)

            # Locate the min and max price input boxes
            min_input = self.page.locator('input[placeholder="Min"]')
            max_input = self.page.locator('input[placeholder="Max"]')

            # Fill the price range
            min_input.fill(str(min_price))
            max_input.fill(str(max_price))

            # Wait a moment for UI update
            self.page.wait_for_timeout(1000)

            # Locate the triangle "Apply" button (SVG icon)
            triangle_button = self.page.locator('button > svg, div.c3KeDq')  # Daraz often uses these classes/icons

            if triangle_button.count() > 0:
                triangle_button.first.click()
                print("Clicked triangle button to apply price filter.")
            else:
                print("Triangle button not found — pressing Enter key instead.")
                max_input.press("Enter")

            self.page.wait_for_timeout(4000)
            print(f"Applied price filter: {min_price}–{max_price}")

        except Exception as e:
            print(f"Could not apply price filter: {e}")

    def count_products(self):
        self.page.wait_for_timeout(4000)
        products = self.page.locator(self.product_titles)
        count = products.count()
        if count == 0:
            print("No products found, but continuing test anyway...")
        else:
            print(f"Total products found: {count}")
        return products

    def open_first_product(self):
        products = self.page.locator(self.product_titles)
        if products.count() > 0:
            products.first.click()
            self.page.wait_for_timeout(3000)
        else:
            print("No product to open")

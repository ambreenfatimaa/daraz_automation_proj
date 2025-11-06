class ProductPage:
    def __init__(self, page):
        self.page = page

    def verify_free_shipping(self):
        try:
            if self.page.locator("text=Free Shipping").is_visible():
                print("Free shipping is available")
            else:
                print("Free shipping not available")
        except:
            print("Could not verify free shipping")

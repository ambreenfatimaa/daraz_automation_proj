class HomePage:
    def __init__(self, page):
        self.page = page
        self.search_box = 'input[name="q"]'

    def navigate(self):
        self.page.goto("https://www.daraz.pk/")

    def search_product(self, product_name):
        self.page.fill(self.search_box, product_name)
        self.page.press(self.search_box, "Enter")
        self.page.wait_for_timeout(5000)

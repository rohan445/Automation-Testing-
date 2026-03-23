class product_page:
    def __init__(self,page):
        self.page = page 
        self.product =  page.get_by_role("link", name="Sample Shirt Name").first.click()
        self.add_to_cart = page.get_by_role("button", name="Add to Cart").click()
        self.remove_from_cart = page.get_by_role("button", name="Remove from Cart").click()
        self.cart = page.get_by_role("link", name="Cart").click()

    def add_product_to_cart(self,add_to_cart,page):
        self.add_to_cart = page.get_by_role("button", name="Add to Cart").click()
        self.page.wait_for_url("https://practice.qabrains.com/ecommerce")

    def remove_product_from_cart(self,remove_from_cart,page):
        self.remove_from_cart = page.get_by_role("button", name="Remove from Cart").click()
        self.page.wait_for_url("https://practice.qabrains.com/ecommerce")

    def go_to_cart_page(self,cart,page):
        self.cart = page.get_by_role("link", name="Cart").click()
        self.page.wait_for_url("https://practice.qabrains.com/ecommerce/cart")

    def select_product(self,product,page):
        self.product =  page.get_by_role("link", name="Sample Shirt Name").first.click()
        self.page.wait_for_url("https://practice.qabrains.com/ecommerce/product/1")
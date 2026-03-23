class specific_product_page:
    def __init__(self,page):
        self.page = page 
        self.add_to_cart = page.get_by_role("button", name="Add to Cart").click()
        self.increase_quantity = page.get_by_role("button", name="Increase quantity").click()
        self.decrease_quantity = page.get_by_role("button", name="Decrease quantity").click()
        self.checkout = page.get_by_role("link", name="Checkout").click()
        self.quantity = page.get_by_role("spinbutton", name="Quantity").input_value()
        self.cart = page.get_by_role("link", name="Cart").click()

    def add_product_to_cart(self,add_to_cart,page):
        self.add_to_cart = page.get_by_role("button", name="Add to Cart").click()
        self.page.wait_for_url("https://practice.qabrains.com/ecommerce")

    def go_to_cart_page(self,cart,page):
        self.cart = page.get_by_role("link", name="Cart").click()
        self.page.wait_for_url("https://practice.qabrains.com/ecommerce/cart")

    def increase_product_quantity(self,increase_quantity,page):
        self.increase_quantity = page.get_by_role("button", name="Increase quantity").click()
        self.page.wait_for_url("https://practice.qabrains.com/ecommerce/cart")

    def decrease_product_quantity(self,decrease_quantity,page): 
        self.decrease_quantity = page.get_by_role("button", name="Decrease quantity").click()
        self.page.wait_for_url("https://practice.qabrains.com/ecommerce/cart")
    
    def check_product_quantity(self,quantity):
        self.quantity = quantity
        assert self.quantity == 2, f"Expected quantity to be 2 but got {self.quantity}"

    def go_to_checkout_page(self,checkout,page): 
        self.checkout = page.get_by_role("link", name="Checkout").click()
        self.page.wait_for_url("https://practice.qabrains.com/ecommerce/checkout")
class cart:
    def __init__(self,page):
        self.cart = page.locator("#cart_contents_container")
        self.increment = page.get_role("#cart_contents_container .cart_quantity_button").click()
        self.decrement = page.get_role("#cart_contents_container .cart_quantity_button").click()
        self.remove = page.get_role("#cart_contents_container .cart_button").click()
        self.checkout = page.get_role("#cart_contents_container .checkout_button").click()
        self.continue_shopping = page.get_role("#cart_contents_container .continue_shopping_button").click()

    def increment_item(self):
        self.increment.click()  
    
    def decrement_item(self):
        self.decrement.click()

    def remove_item(self):
        self.remove.click()

    def checkout_cart(self):
        self.checkout.click()

    def continue_shopping_cart(self):
        self.continue_shopping.click()

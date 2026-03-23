class checkout:
    def __init__(self,finish,page):
        self.page = page
        self.finsh = page.get_by_role("button", name="Finish").click()
        self.cancel = page.get_by_role("button", name="Cancel").click()

    def finish_checkout(self,page):
        self.page = page
        self.finsh = page.get_by_role("button", name="Finish").click().wait_for_url("https://practice.qabrains.com/ecommerce/checkout-complete")

    def cancel_checkout(self,page):
        self.page = page
        self.cancel = page.get_by_role("button", name="Cancel").click().wait_for_url("https://practice.qabrains.com/ecommerce/checkout")      
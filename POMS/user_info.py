class checkout_user_info:
    def __init__(self, name, email, pin,page,continue_button):
        self.page = page
        self.name = page.get_by_role("textbox", name="Name on card").fill(name)
        self.email = page.get_by_role("textbox", name="Email").fill(email)
        self.pin = page.get_by_role("spinbutton", name="PIN").fill(pin)
        self.continue_button = page.get_by_role("button", name="Continue").click()

    def continue_checkout(self):
        self.continue_button

    def get_checkout_user_info(self):
        return self.name, self.email, self.pin
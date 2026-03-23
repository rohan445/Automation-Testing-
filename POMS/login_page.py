class loginpage:
    def __init__(self,page):
        self.page = page 
        self.email = page.get_by_role("textbox", name="Email*").click()
        self.password = page.get_by_role("textbox", name="Password*").click()
        self.login_button = page.get_by_role("button", name="Login").click()
        self.back_to_home = page.get_by_role("link", name="Back to Home").click()

    def back_to_home_page(self,back_to_home,page):
        self.back_to_home = page.get_by_role("link", name="Back to Home").click()
        self.page.wait_for_url("https://practice.qabrains.com/")

    def login(self,email,password,page):
        self.email = page.get_by_role("textbox", name="Email*").fill(email)
        self.password = page.get_by_role("textbox", name="Password*").fill(password)
        self.login_button = page.get_by_role("button", name="Login").click()
        self.page.wait_for_url("https://practice.qabrains.com/ecommerce")

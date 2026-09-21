class LoginPage:
    def __init__(self, page):
        self.page = page

    def goto(self, base_url):
        self.page.goto(f"{base_url}/#practice")

    def login(self, email, password):
        self.page.once("dialog", lambda dialog: dialog.dismiss())
        self.page.get_by_placeholder("Email").click()
        self.page.get_by_placeholder("Email").fill(email)
        self.page.get_by_placeholder("Password").click()
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()
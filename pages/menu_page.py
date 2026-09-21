class MenuPage:
    def __init__(self, page):
        self.page = page

    def open_menu(self):
        self.page.locator("button.user-pill").click()

    def click_my_profile(self):
        self.page.get_by_role("button", name="👤 My Profile").click()
class ProfilePage:
    def __init__(self, page):
        self.page = page

    def open_menu(self):
        self.page.locator("button.user-pill").click()

    def click_edit_profile(self):
        self.page.get_by_role("button", name="✏️ Edit Profile").click()

    def upload_profile_picture(self, file_path):
        with self.page.expect_file_chooser() as fc_info:
            self.page.get_by_text("📷 Choose Photo").click()
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)

    def save_changes(self):
        self.page.once("dialog", lambda dialog: dialog.dismiss())
        self.page.get_by_role("button", name="💾 Save Changes").click()
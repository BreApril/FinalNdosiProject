class ProfilePage:
    def __init__(self, page):
        self.page = page

    def click_edit_profile(self):
        self.page.get_by_role("button", name="✏️ Edit Profile").click()

    def upload_profile_picture(self, file_path):
        with self.page.expect_file_chooser() as fc_info:
            self.page.get_by_text("📷 Choose Photo").click()
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)
        # Give the app a moment to process/preview the selected file
        self.page.wait_for_timeout(1500)

    def save_changes(self):
        self.page.once("dialog", lambda dialog: dialog.dismiss())
        # Wait specifically for the image upload network call to complete
        with self.page.expect_response(
            lambda response: "/profile/image" in response.url and response.request.method == "POST",
            timeout=10000
        ) as response_info:
            self.page.get_by_role("button", name="💾 Save Changes").click()
        return response_info.value
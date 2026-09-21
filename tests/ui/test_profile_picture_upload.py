import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from pages.profile_page import ProfilePage

captured_requests = []


def log_request(request):
    captured_requests.append({
        "url": request.url,
        "method": request.method
    })


def test_upload_profile_picture(page, base_url, credentials):
    page.on("request", log_request)

    login_page = LoginPage(page)
    menu_page = MenuPage(page)
    profile_page = ProfilePage(page)

    os.makedirs("screenshots", exist_ok=True)

    login_page.goto(base_url)
    login_page.login(credentials["username"], credentials["password"])
    page.screenshot(path="screenshots/01_login.png")

    menu_page.open_menu()
    page.screenshot(path="screenshots/02_menu.png")

    menu_page.click_my_profile()
    page.screenshot(path="screenshots/03_my_profile.png")

    profile_page.click_edit_profile()
    page.screenshot(path="screenshots/04_edit_profile.png")

    profile_page.upload_profile_picture("test_data/sample_profile_pic.jpg")
    page.screenshot(path="screenshots/05_photo_selected.png")

    profile_page.save_changes()
    page.wait_for_timeout(1000)
    page.screenshot(path="screenshots/06_saved.png")

    # Save captured API calls for the API test suite
    os.makedirs("test_data", exist_ok=True)
    with open("test_data/captured_endpoints.json", "w") as f:
        json.dump(captured_requests, f, indent=2)

    assert len(captured_requests) > 0, "No network requests were captured during the flow"
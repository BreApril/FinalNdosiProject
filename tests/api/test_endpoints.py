import json
import os
import pytest

CAPTURED_FILE = os.path.join(os.path.dirname(__file__), "../../test_data/captured_endpoints.json")

# Endpoints we don't need to validate (static assets, unrelated third-party noise)
IGNORED_SUBSTRINGS = [
    "/static/",
    ".css",
    ".js",
    "Nta%20Logo",
    "/uploads/profile-images/"  # these are direct image GETs, not API responses
]

# Known issue: this endpoint currently returns 404 on the test environment.
# Documented here so the test suite reflects reality rather than silently failing.
KNOWN_ISSUES = {
    "https://www.ndosiautomation.co.za/APIDEV/student/today": 404
}


def load_captured_endpoints():
    with open(CAPTURED_FILE) as f:
        data = json.load(f)

    filtered = []
    seen = set()
    for entry in data:
        if any(s in entry["url"] for s in IGNORED_SUBSTRINGS):
            continue
        key = (entry["url"], entry["method"])
        if key in seen:
            continue
        seen.add(key)
        filtered.append(entry)
    return filtered


@pytest.mark.parametrize("entry", load_captured_endpoints(), ids=lambda e: f"{e['method']} {e['url']}")
def test_endpoint_status_code(entry):
    url = entry["url"]
    method = entry["method"]
    status = entry["status"]

    if url in KNOWN_ISSUES:
        expected = KNOWN_ISSUES[url]
        assert status == expected, (
            f"Known issue status changed for {method} {url}: "
            f"expected {expected}, got {status}. This may mean the issue was fixed "
            f"or a new problem was introduced — please investigate."
        )
        pytest.xfail(f"{url} is a known issue (returns {expected}) — tracked, not a new failure")

    assert 200 <= status < 300, (
        f"{method} {url} returned unexpected status {status} (expected 2xx)"
    )


def test_profile_image_upload_endpoint_specifically():
    """
    Explicit, named check for the core endpoint this assignment is about:
    the profile picture upload call.
    """
    data = load_captured_endpoints()
    upload_calls = [
        e for e in data
        if e["url"] == "https://www.ndosiautomation.co.za/APIDEV/profile/image"
        and e["method"] == "POST"
    ]
    assert len(upload_calls) > 0, "Profile image upload endpoint was never called during the UI flow"
    for call in upload_calls:
        assert call["status"] == 200, f"Upload endpoint returned {call['status']}, expected 200"
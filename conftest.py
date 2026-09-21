import os
import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("NDOSI_BASE_URL", "https://ndosi-test-site-url")

@pytest.fixture(scope="session")
def credentials():
    return {
        "username": os.getenv("NDOSI_USERNAME", ""),
        "password": os.getenv("NDOSI_PASSWORD", "")
    }
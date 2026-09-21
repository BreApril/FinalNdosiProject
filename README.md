# Ndosi Profile Picture Automation

Automated UI and API test suite for validating profile picture upload
functionality on the Ndosi test site, built with Python, Playwright, and pytest.

## Overview
This project automates:
- **UI flow**: Login → Menu → My Profile → Edit Profile → Upload Picture → Verify Update
- **API validation**: Captures and validates response codes for every endpoint
  hit during the UI flow

## Tech Stack
- Python 3.14
- Playwright (UI automation)
- pytest (test runner)
- requests (API testing)
- Allure (reporting)
- GitHub Actions (CI/CD, scheduled daily)

## Setup

\`\`\`bash
pip install -r requirements.txt
playwright install
\`\`\`

Create a `.env` file in the project root:
\`\`\`
NDOSI_BASE_URL=https://your-test-site-url
NDOSI_USERNAME=your_test_username
NDOSI_PASSWORD=your_test_password
\`\`\`

## Running Tests Locally

\`\`\`bash
pytest tests/ui
pytest tests/api
\`\`\`

## CI/CD
Tests run automatically every day at **00:00 SAST** via GitHub Actions
(see `.github/workflows/daily-tests.yml`), and can also be triggered manually.

## Reporting
Allure reports are generated after each run and uploaded as pipeline artifacts,
along with step-by-step screenshots.

## Project Structure
See folder layout in repo root: `pages/`, `tests/`, `utils/`, `config/`, etc.
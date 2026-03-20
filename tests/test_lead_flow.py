import time
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.create_lead_page import CreateLeadPage


def test_login_create_lead_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        login_page = LoginPage(page)
        dashboard_page = DashboardPage(page)
        create_lead_page = CreateLeadPage(page)

        # Dynamic test data
        timestamp = int(time.time())
        lead_name = f"Test User {timestamp}"
        lead_email = f"test{timestamp}@mail.com"
        lead_phone = "9999999999"

        # Step 1: Login
        login_page.goto()
        login_page.login("testuser@mail.com", "password123")

        # Step 2: Create Lead
        dashboard_page.click_create_lead()
        create_lead_page.create_lead(lead_name, lead_email, lead_phone)

        # Step 3: Verify Lead
        assert dashboard_page.is_lead_visible(lead_name)

        browser.close()

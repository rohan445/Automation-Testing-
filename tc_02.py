from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
import allure

@allure.title("Test Case 02: Negative Login Test")
@allure.description("This test verifies that a user cannot log in with invalid credentials and appropriate error messages are displayed.")
@allure.severity(allure.severity_level.NORMAL)

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://practice.qabrains.com/ecommerce/login")
    page.get_by_role("textbox", name="Email*").fill("test@qabrain.com")
    page.get_by_role("textbox", name="Password*").fill("Password123")

    page.get_by_role("button", name="Login").click()

    # ASSERTION 1: Still on login page
    expect(page).to_have_url("https://practice.qabrains.com/ecommerce/login")

    # ASSERTION 2: Error message visible
    expect(page.locator("text=Username is incorrect")).to_be_visible()

    # ASSERTION 3: Email field still contains entered value
    expect(page.get_by_role("textbox", name="Email*")).to_have_value("test@qabrain.com")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
import allure 


@allure.title("Test Case 01: Login Test")
@allure.description("This test verifies that a user can log in successfully with valid credentials.")
@allure.severity(allure.severity_level.MAJOR)
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practice.qabrains.com/ecommerce/login")
    page.get_by_role("textbox", name="Email*").fill("test@qabrains.com")
    page.get_by_role("textbox", name="Password*").fill("Password123")
    page.get_by_role("button", name="Login").click()

    # ASSERTION 1: URL should change (user logged in)
    expect(page).not_to_have_url("https://practice.qabrains.com/ecommerce/login")

    # ASSERTION 2: Login button should disappear (no longer on login page)
    expect(page.get_by_role("button", name="Login")).not_to_be_visible()

    # ASSERTION 3 (BEST): Check something from next page
    expect(page.locator("text=Products")).to_be_visible()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
import allure

@allure.title("Test Case 04: Negative Login Test - Empty Fields")
@allure.description("This test verifies that a user cannot log in without entering email and password, and appropriate error messages are displayed.")
@allure.severity(allure.severity_level.MINOR)

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practice.qabrains.com/ecommerce/login")
    page.get_by_role("button", name="Login").click()

    # ASSERTION 1: Still on login page
    expect(page).to_have_url("https://practice.qabrains.com/ecommerce/login")

    # ASSERTION 2: Email required error
    expect(page.locator("text=Email is a required field")).to_be_visible()

    # ASSERTION 3: Password required error
    expect(page.locator("text=Password is a required field")).to_be_visible()

    # ASSERTION 4: Fields are still empty
    expect(page.get_by_role("textbox", name="Email*")).to_have_value("")
    expect(page.get_by_role("textbox", name="Password*")).to_have_value("")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
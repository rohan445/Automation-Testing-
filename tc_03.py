from playwright.sync_api import expect ,sync_playwright,Playwright
import pytest
import allure

@allure.title("Test Case 03: Negative Login Test - Wrong Password")
@allure.description("This test verifies that a user cannot log in with a valid email but            invalid password, and appropriate error messages are displayed.")
@allure.severity()

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://practice.qabrains.com/ecommerce/login")
    page.get_by_role("textbox", name="Email*").fill("test@qabrains.com")
    page.get_by_role("textbox", name="Password*").fill("Password12")  # wrong password

    page.get_by_role("button", name="Login").click()

    # ASSERTION 1: Still on login page
    expect(page).to_have_url("https://practice.qabrains.com/ecommerce/login")

    # ASSERTION 2: Correct error message shown
    expect(page.locator("text=Password is incorrect.").first).to_be_visible()

    # ASSERTION 3: Email remains filled
    expect(page.get_by_role("textbox", name="Email*")).to_have_value("test@qabrains.com")

    # ASSERTION 4: Password field behavior (optional)
    expect(page.get_by_role("textbox", name="Password*")).to_have_value("Password12")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
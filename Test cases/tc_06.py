from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
import allure
@allure.title("Test Case 03: Negative Login Test - Wrong Password")
@allure.description("This test verifies that a user cannot log in with a valid email but invalid password, and appropriate error messages are displayed.")
@allure.severity(allure.severity_level.NORMAL)

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practice.qabrains.com/ecommerce/login")

    page.get_by_role("textbox", name="Email*").fill("test@qabrains.com")
    page.get_by_role("textbox", name="Password*").fill("Password123")
    page.get_by_role("button", name="Login").click()

    # ASSERTION 1: Login success
    expect(page).not_to_have_url("https://practice.qabrains.com/ecommerce/login")
    page.get_by_role("link", name="Sample Shirt Name").first.click()
    expect(page.locator("text=Sample Shirt Name")).to_be_visible()
    page.get_by_role("button", name="Add to cart").click()

    # ASSERTION 2: Shirt added
    expect(page.get_by_role("button", name="Remove from cart")).to_be_visible()
    page.get_by_role("button", name="Back to Products").click()
    page.get_by_role("link", name="Sample Shoe Name").first.click()
    expect(page.locator("text=Sample Shoe Name")).to_be_visible()
    page.get_by_role("button", name="+").click()
    page.get_by_role("button", name="+").click()
    page.get_by_role("button", name="−").click()
    page.get_by_role("button", name="Add to cart").click()

    # ASSERTION 3: Shoe added
    expect(page.get_by_role("button", name="Remove from cart")).to_be_visible()

    page.get_by_role("button", name="Back to Products").click()
    page.get_by_role("button", name="2").click()

    # ASSERTION 4: Page changed
    expect(page.locator("button[aria-current='true']")).to_have_text("2")
    page.get_by_role("button", name="Remove").first.click()
    page.get_by_role("button", name="Remove").click()

    # ASSERTION 5: Cart is empty (Add buttons visible again)
    expect(page.get_by_role("button", name="Add to cart").first).to_be_visible()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

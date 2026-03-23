from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
import allure

@allure.title("Test Case 05: Add to Cart Test")
@allure.description("This test verifies that a user can add a product to the cart and then remove it, ensuring the cart functionality works as expected.")
@allure.severity(allure.severity_level.NORMAL)


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practice.qabrains.com/ecommerce/login")
    page.get_by_role("textbox", name="Email*").fill("test@qabrains.com")
    page.get_by_role("textbox", name="Password*").fill("Password123")
    page.get_by_role("button", name="Login").click()

    # ASSERTION 1: Login successful (URL changed)
    expect(page).not_to_have_url("https://practice.qabrains.com/ecommerce/login")

    page.get_by_role("link", name="Sample Shirt Name").first.click()

    # ASSERTION 2: Product page opened
    expect(page.locator("text=Sample Shirt Name")).to_be_visible()

    page.get_by_role("button", name="+").click()
    page.get_by_role("button", name="+").click()
    page.get_by_role("button", name="−").click()
    page.get_by_role("button", name="Add to cart").click()

    # ASSERTION 3: Item added to cart
    expect(page.get_by_role("button", name="Remove from cart")).to_be_visible()

    # BACK TO PRODUCTS
    page.get_by_role("button", name="Back to Products").click()

    # ASSERTION 4: Back on product listing
    expect(page.locator("text=Sample Shirt Name")).to_be_visible()
    page.get_by_role("button", name="Remove from cart").click()

    # ASSERTION 5: Item removed from cart
    expect(page.get_by_role("button", name="Add to cart")).to_be_visible()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
from playwright.sync_api import Playwright, sync_playwright, expect
import re
import pytest
import allure 
@allure.title("Test Case 07: Product Interaction Test")
@allure.description("This test verifies that a user can interact with multiple products, add them to the cart, and navigate through pagination, ensuring the product listing and cart functionalities work as expected.")
@allure.severity(allure.severity_level.NORMAL)

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://practice.qabrains.com/ecommerce/login")

    page.get_by_role("textbox", name="Email*").fill("test@qabrains.com")
    page.get_by_role("textbox", name="Password*").fill("Password123")
    page.get_by_role("button", name="Login").click()

    # ASSERTION: Login successful
    expect(page).not_to_have_url("https://practice.qabrains.com/ecommerce/login")

    page.get_by_role("link", name="Sample Shirt Name").first.click()
    expect(page.locator("text=Sample Shirt Name")).to_be_visible()

    page.get_by_role("button", name="Add to cart").click()
    expect(page.get_by_role("button", name="Remove from cart")).to_be_visible()

    page.get_by_role("button", name="Back to Products").click()
    expect(page.locator("text=Sample Shirt Name")).to_be_visible()
    page.get_by_role("link", name="Sample Shoe Name").first.click()
    expect(page.locator("text=Sample Shoe Name")).to_be_visible()

    page.get_by_role("button", name="+").click()
    page.get_by_role("button", name="+").click()
    page.get_by_role("button", name="−").click()

    page.get_by_role("button", name="Add to cart").click()
    expect(page.get_by_role("button", name="Remove from cart")).to_be_visible()

    page.get_by_role("button", name="Back to Products").click()

    # Pagination
    page.get_by_role("button", name="2").click()
    expect(page.locator("button[aria-current='true']")).to_have_text("2")

    # Remove items
    page.get_by_role("button", name="Remove").first.click()
    page.get_by_role("button", name="Remove").click()
    expect(page.get_by_role("button", name="Add to cart").first).to_be_visible()

    # Add again
    page.get_by_role("button", name="Add to cart").first.click()
    expect(page.get_by_role("button", name="Remove from cart").first).to_be_visible()

    page.get_by_role("button", name="Add to cart").first.click()
    expect(page.get_by_role("button", name="Remove from cart").first).to_be_visible()

    
    page.get_by_role("link", name="Sample Shoe Name").first.click()
    expect(page.locator("text=Sample Shoe Name")).to_be_visible()
    page.get_by_role("button", name="+").click()
    page.get_by_role("button", name="Add to cart").click()
    expect(page.get_by_role("button", name="Remove from cart")).to_be_visible()
    page.get_by_role("button", name="Back to Products").click()
    page.get_by_role("button", name="Add to cart").first.click()
    page.get_by_role("button", name="Add to cart").nth(2).click()
    page.get_by_role("button", name="Add to cart").nth(2).click()
    page.get_by_role("button", name="Remove from cart").nth(3).click()
    expect(page.get_by_role("button", name="Add to cart").nth(3)).to_be_visible()
    page.get_by_role("link", name="Sample T-Shirt Name").nth(2).click()
    expect(page.locator("text=Sample T-Shirt Name")).to_be_visible()
    page.get_by_role("button", name="+").click()
    page.get_by_role("button", name="+").click()
    page.get_by_role("button", name="−").click()

    page.get_by_role("button", name="Add to cart").click()
    expect(page.get_by_role("button", name="Remove from cart")).to_be_visible()
    page.get_by_role("button", name="5").click()
    expect(page.locator("button[aria-current='true']")).to_have_text("5")
    page.get_by_role("button", name="-").nth(1).click()
    page.get_by_role("button", name="+").nth(2).click()
    page.get_by_role("button", name="Checkout").click()

    # FINAL ASSERTATION: navigated to checkout
    expect(page).to_have_url(re.compile(".*checkout"))

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
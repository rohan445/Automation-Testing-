import re
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
import allure
@allure.title("Test Case 08: End-to-End Purchase Flow Test")
@allure.description("This test verifies the complete end-to-end purchase flow, including login,product selection, cart management, checkout process, and logout, ensuring that all functionalities work together seamlessly.") 
@allure.severity(allure.severity_level.CRITICAL)


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practice.qabrains.com/ecommerce/login")

    page.get_by_role("textbox", name="Email*").fill("test@qabrains.com")
    password_box = page.get_by_role("textbox", name="Password*")
    password_box.fill("Password123")
    page.get_by_role("button", name="Login").click()

    # ASSERTION 1: URL should change (user logged in)
    expect(page).to_have_url(re.compile(".*products"))
    expect(page.get_by_text("Products")).to_be_visible()
    page.get_by_role("button", name="Add to cart").first.click()
    expect(page.locator(".cart-badge")).to_have_text("1")
    page.get_by_role("link", name="Sample Shoe Name").first.click()
    expect(page.get_by_text("Sample Shoe Name")).to_be_visible()
    page.get_by_role("button", name="+").click()
    page.get_by_role("button", name="Add to cart").click()
    expect(page.locator(".cart-badge")).to_have_text("2")
    page.get_by_role("button", name="Back to Products").click()
    page.get_by_role("link", name="Sample Jacket Name").first.click()

    # ASSERTION: Jacket page opened
    expect(page.get_by_text("Sample Jacket Name")).to_be_visible()

    page.get_by_role("button", name="+").click()
    page.get_by_role("button", name="−").click()
    page.get_by_role("button", name="Add to cart").click()
    expect(page.locator(".cart-badge")).to_have_text("3")
    page.get_by_role("button", name="Back to Products").click()
    page.get_by_role("button", name="3").click()  # Open cart
    page.get_by_role("button", name="Remove").nth(2).click()
    page.get_by_role("button", name="Remove").first.click()
    expect(page.locator(".cart-badge")).to_have_text("1")
    page.get_by_role("button", name="Checkout").click()
    expect(page.get_by_text("Checkout")).to_be_visible()
    page.get_by_role("textbox", name="Ex. John").fill("john")
    page.get_by_role("textbox", name="Ex. Doe").fill("doe")
    page.get_by_role("textbox").nth(3).fill("1207")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Finish").click()

    # ASSERTIONS: Order success
    expect(page.get_by_text("Thank you for your order!")).to_be_visible()
    expect(page.get_by_text("Your order has been dispatched")).to_be_visible()
    page.get_by_role("button", name="Continue Shopping").click()
    page.get_by_role("button", name="test@qabrains.com").click()
    page.get_by_role("button", name="Log out").click()
    page.get_by_role("button", name="Logout").click()

    # ASSERTATIONS: Back to login page
    expect(page).to_have_url(re.compile(".*login"))
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
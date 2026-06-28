import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"

STANDARD_USER = "standard_user"
LOCKED_OUT_USER = "locked_out_user"
VALID_PASSWORD = "secret_sauce"

def test_login_success(page: Page):
    page.goto(BASE_URL)

    page.get_by_placeholder("Username").fill(STANDARD_USER)
    page.get_by_placeholder("Password").fill(VALID_PASSWORD)
    page.get_by_text("Login", exact=True).click()

    expect(page).to_have_url(f"{BASE_URL}inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


def test_login_fail_locked_out_user(page: Page):
    page.goto(BASE_URL)

    page.get_by_placeholder("Username").fill(LOCKED_OUT_USER)
    page.get_by_placeholder("Password").fill(VALID_PASSWORD)
    page.get_by_text("Login", exact=True).click()

    expect(page.locator("[data-test='error']")).to_contain_text(
        "Sorry, this user has been locked out."
    )
    expect(page).to_have_url(BASE_URL)


def test_login_fail_wrong_password(page: Page):
    page.goto(BASE_URL)

    page.get_by_placeholder("Username").fill(STANDARD_USER)
    page.get_by_placeholder("Password").fill("wrong_password")
    page.get_by_text("Login", exact=True).click()

    expect(page.locator("[data-test='error']")).to_contain_text(
        "Username and password do not match any user in this service"
    )


def test_login_fail_empty_fields(page: Page):
    page.goto(BASE_URL)

    page.get_by_text("Login", exact=True).click()

    expect(page.locator("[data-test='error']")).to_contain_text(
        "Username is required"
    )

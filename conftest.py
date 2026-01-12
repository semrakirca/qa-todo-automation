import pytest
from playwright.sync_api import sync_playwright

from pages.todo_page import TodoPage


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
  # istersen False yapar, tarayıcıyı görürsün
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def todo_page(page):
    return TodoPage(page)

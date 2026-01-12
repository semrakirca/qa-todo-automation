import os
from datetime import datetime
import pytest
from playwright.sync_api import sync_playwright

from pages.todo_page import TodoPage

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("artifacts", exist_ok=True)
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = f"artifacts/{item.name}_{ts}.png"
            page.screenshot(path=path, full_page=True)
            print(f"\n📸 Screenshot saved: {path}")

@pytest.fixture(scope="session")
def browser():
    # CI'de ekran yok → headless şart
    # Lokal: PW_HEADLESS=0 yaparsan tarayıcı görünür
    headless_env = os.getenv("PW_HEADLESS", "1")
    headless = headless_env != "0"

    slow_mo = int(os.getenv("PW_SLOWMO", "0"))

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, slow_mo=slow_mo)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()

    page.set_default_timeout(60000)
    page.set_default_navigation_timeout(60000)

    yield page
    context.close()


@pytest.fixture
def todo_page(page):
    return TodoPage(page)
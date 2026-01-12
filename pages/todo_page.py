class TodoPage:
    BASE_URL = "https://todomvc.com/examples/react/dist/"

    def __init__(self, page):
        self.page = page
        self.task_input = "input.new-todo"

    def open(self):
        self.page.goto(self.BASE_URL, wait_until="domcontentloaded")
        self.page.wait_for_selector(self.task_input, timeout=60000)

    def add_task(self, text: str):
        self.page.fill(self.task_input, text)
        self.page.keyboard.press("Enter")

    def task_exists(self, text: str) -> bool:
        return self.page.locator(f"li:has-text('{text}')").is_visible()

    def toggle_task_complete(self, text: str):
        # ilgili li'yi bul, içindeki checkbox'ı tıkla
        item = self.page.locator("li", has_text=text)
        item.locator("input.toggle").click()

    def is_task_completed(self, text: str) -> bool:
        item = self.page.locator("li", has_text=text)
        return item.get_attribute("class") and "completed" in item.get_attribute("class")

    def delete_task(self, text: str):
        item = self.page.locator("li", has_text=text)
        item.hover()
        item.locator("button.destroy").click()

    def task_count(self) -> int:
        return self.page.locator("ul.todo-list li").count()

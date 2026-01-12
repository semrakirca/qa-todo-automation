import pytest


@pytest.mark.smoke
def test_user_can_add_task(todo_page):
    todo_page.open()
    todo_page.add_task("Buy milk")
    assert todo_page.task_exists("Buy milk")


@pytest.mark.regression
def test_user_can_add_multiple_tasks(todo_page):
    todo_page.open()
    todo_page.add_task("Task 1")
    todo_page.add_task("Task 2")
    assert todo_page.task_exists("Task 1")
    assert todo_page.task_exists("Task 2")

@pytest.mark.regression
def test_user_can_complete_task(todo_page):
    todo_page.open()
    todo_page.add_task("Complete me")
    todo_page.toggle_task_complete("Complete me")
    assert todo_page.is_task_completed("Complete me")


@pytest.mark.regression
def test_user_can_delete_task(todo_page):
    todo_page.open()
    todo_page.add_task("Delete me")
    assert todo_page.task_exists("Delete me")

    todo_page.delete_task("Delete me")
    assert not todo_page.task_exists("Delete me")


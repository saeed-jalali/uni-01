tasks = []

def add_task(title):
    tasks.append({"title": title, "done": False})
    print(f"Task '{title}' added.")

def show_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, 1):
        status = "✓" if t["done"] else " "
        print(f"{i}. [{status}] {t['title']}")

def complete_task(index):
    tasks[index - 1]["done"] = True

def delete_task(index):
    tasks.pop(index - 1)

def main():
    print("Task Manager")
    add_task("Learn Git")
    show_tasks()

if __name__ == "__main__":
    main()
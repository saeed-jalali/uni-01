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
    while True:
        print("\n1. Add  2. Show  3. Done  4. Delete  5. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_task(input("Title: "))
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            complete_task(int(input("Number: ")))
        elif choice == "4":
            delete_task(int(input("Number: ")))
        elif choice == "5":
            break

if __name__ == "__main__":
    main()
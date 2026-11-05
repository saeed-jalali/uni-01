tasks = []

def add_task(title):
    tasks.append({"title": title, "done": False})
    print(f"Task '{title}' added.")

def main():
    print("Task Manager")
    add_task("Learn Git")

if __name__ == "__main__":
    main()
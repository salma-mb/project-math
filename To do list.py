class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.description} ({status})"

class TodoList:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                tasks = []
                for line in file:
                    description, completed = line.strip().split(',')
                    tasks.append(Task(description, completed == 'True'))
                return tasks
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.description},{task.completed}\n")

    def add_task(self, description):
        self.tasks.append(Task(description))
        self.save_tasks()

    def remove_task(self, index):
        del self.tasks[index]
        self.save_tasks()

    def update_task(self, index, description):
        self.tasks[index].description = description
        self.save_tasks()

    def mark_task_as_completed(self, index):
        self.tasks[index].mark_as_completed()
        self.save_tasks()

    def view_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index+1}. {task}")

def main():
    todo_list = TodoList('tasks.txt')
    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. View Tasks")
        print("6. Quit")
        choice = input("Choose an option: ")
        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            index = int(input("Enter task index: ")) - 1
            todo_list.remove_task(index)
        elif choice == '3':
            index = int(input("Enter task index: ")) - 1
            description = input("Enter new task description: ")
            todo_list.update_task(index, description)
        elif choice == '4':
            index = int(input("Enter task index: ")) - 1
            todo_list.mark_task_as_completed(index)
        elif choice == '5':
            todo_list.view_tasks()
        elif choice == '6':
            break

if __name__ == "__main__":
    main()
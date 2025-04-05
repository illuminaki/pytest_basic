class TaskView:
    def show_tasks(self, tasks):      # Líneas 2-8
        if not tasks:
            print("No hay tareas.")
            return
        for task in tasks:
            status = "✓" if task["completed"] else "✗"
            print(f"[{status}] {task['id']}: {task['name']}")

    def show_message(self, message):  # Líneas 11
        print(message)
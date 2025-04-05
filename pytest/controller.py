class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_task(self, task_name):
        task = self.model.add_task(task_name)
        self.view.show_message(f"Tarea añadida: {task['name']}")

    def list_tasks(self):
        tasks = self.model.get_all_tasks()
        self.view.show_tasks(tasks)

    def complete_task(self, task_id):
        task = self.model.complete_task(task_id)
        if task:
            self.view.show_message(f"Tarea completada: {task['name']}")
        else:
            self.view.show_message("Tarea no encontrada")
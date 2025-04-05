class TaskModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        task = {"id": len(self.tasks) + 1, "name": task_name, "completed": False}
        self.tasks.append(task)
        return task

    def get_all_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return task
        return None
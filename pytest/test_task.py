import unittest
from model import TaskModel
from view import TaskView
from controller import TaskController

class TestTaskApp(unittest.TestCase):
    def setUp(self):
        self.model = TaskModel()
        self.view = TaskView()
        self.controller = TaskController(self.model, self.view)

    def test_add_task(self):
        task = self.model.add_task("Test task")
        self.assertEqual(task["name"], "Test task")
        self.assertFalse(task["completed"])
        self.assertEqual(len(self.model.tasks), 1)

    def test_complete_task(self):
        self.model.add_task("Test task")
        task = self.model.complete_task(1)
        self.assertTrue(task["completed"])
        result = self.model.complete_task(999)
        self.assertIsNone(result)

    def test_get_all_tasks(self):
        self.model.add_task("Task 1")
        self.model.add_task("Task 2")
        tasks = self.model.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]["name"], "Task 1")
        self.assertEqual(tasks[1]["name"], "Task 2")

    # Nuevas pruebas para el controlador
    def test_controller_add_task(self):
        self.controller.add_task("Controller task")
        tasks = self.model.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["name"], "Controller task")

    def test_controller_list_tasks(self):
        self.model.add_task("Task 1")
        self.controller.list_tasks()  # Solo llamamos al método, la salida va a la consola

    def test_controller_complete_task_success(self):
        self.controller.add_task("Complete task")
        self.controller.complete_task(1)
        tasks = self.model.get_all_tasks()
        self.assertTrue(tasks[0]["completed"])

    def test_controller_complete_task_not_found(self):
        self.controller.complete_task(999)  # Prueba el caso "else"

    # Nuevas pruebas para la vista
    def test_view_show_tasks_empty(self):
        self.view.show_tasks([])  # Prueba el caso de lista vacía

    def test_view_show_tasks_with_tasks(self):
        tasks = [{"id": 1, "name": "Task", "completed": False}]
        self.view.show_tasks(tasks)  # Prueba el bucle for

    def test_view_show_message(self):
        self.view.show_message("Test message")  # Prueba la salida de mensajes

if __name__ == "__main__":
    unittest.main()
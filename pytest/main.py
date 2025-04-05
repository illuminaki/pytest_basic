from model import TaskModel
from view import TaskView
from controller import TaskController

def main():
    model = TaskModel()
    view = TaskView()
    controller = TaskController(model, view)

    # Ejemplo de uso
    controller.add_task("Comprar leche")
    controller.add_task("Estudiar Python")
    controller.list_tasks()
    controller.complete_task(1)
    controller.list_tasks()

if __name__ == "__main__":
    main()
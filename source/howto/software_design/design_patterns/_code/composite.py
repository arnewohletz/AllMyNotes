from abc import ABC, abstractmethod

# Working, but not nice example of a HTML Generator for a To-Do list


# Component
class ToDoList(ABC):

    @abstractmethod
    def get_html(self):
        pass


# Leaf
class ToDoItem(ToDoList):

    def __init__(self, text):
        self.text = text

    def get_html(self):
        return f"<input type=\"checkbox\">{self.text}"


# Composite
class ToDoProject(ToDoList):

    def __init__(self, title, list_of_todos: list):
        self.title = title
        self.list_of_todos = list_of_todos

    def get_html(self):
        html = ""
        if len(self.list_of_todos) > 1:
            html += f"<h1>{self.title}</h1>"
        for item in self.list_of_todos:
            # If item is of type ToDoItem, then we will get the checkbox + text
            # but if it is of type ToDoProject, it will call itself on another
            # instance (-> recursion)
            html += "<li>"
            html += item.get_html()
            html += "</li>"
        return html


if __name__ == "__main__":

    to_do_A = ToDoProject("Do A", [ToDoItem("Doing A")])
    to_do_B = ToDoProject("Do B", [ToDoItem("Doing B")])

    to_do_C1_list = [ToDoItem("Doing C1.A"),
                     ToDoItem("Doing C1.B")]
    to_do_C1 = ToDoProject("Doing C1", to_do_C1_list)

    to_do_C_list = [
                    to_do_C1,
                    ToDoItem("Doing C2"),
                    ToDoItem("Doing C3")]
    to_do_C = ToDoProject("Doing C", to_do_C_list)

    print(to_do_A.get_html())
    print(to_do_B.get_html())
    print(to_do_C.get_html())

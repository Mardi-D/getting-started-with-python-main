
# Give the class a name
class PersonalAssistant:

    def __init__(self):  # init function, notice syntax
        self.contacts = {
            'Ann': 'Marketing Coordinator',
            'Chelsea': 'Software Developer',
            'Nichole': 'Sales Representative',
            'Max': 'Technical Writer'
        }
        self.todos = []

    def add_todo(self, new_item):
        self.todos.append(new_item)

    def remove_todo(self, todo_item):
        if todo_item in self.todos:
            # Get the todo_item index in list
            index = self.todos.index(todo_item)
            # pop the index for todo_item in todos list
            self.todos.pop(index)
        else:
            print("Todo is not in list!")

    def get_todos(self):  # Indented correctly
        return self.todos

    def get_birthday(self, name):
        if name == "James":
            print("Happy Birthday Jaybug, I love you so much! Today February is 26th!")
        elif name == "Camille":
            print("Happy Birthday SweetPea, today is August 5th!")
        elif name == "Dellie Doo":
            print("Happy Birthday Twinkie, today is Sept 30th")
        else:
            return "Can't find a birthday for this person"

    def get_contact(self, name):  # Indented correctly
        if name in self.contacts:
            return self.contacts[name]
        else:
            return 'There is no contact information for the name provided.'

# Code to test output of the class
assistant = PersonalAssistant()
assistant.add_todo('Pick up groceries')  # Call method without reassigning assistant
print(assistant.get_todos())  # Correct method call
print(assistant.get_birthday('James'))
print(assistant.get_contact("Chelsea"))  # Correct method call
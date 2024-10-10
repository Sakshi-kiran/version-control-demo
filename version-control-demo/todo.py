# todo.py

def main():
    todos = []
    
    while True:
        action = input("What would you like to do? (add/view/quit): ").strip().lower()
        
        if action == "add":
            todo = input("Enter a new to-do: ")
            todos.append(todo)
            print(f"'{todo}' has been added to your to-do list.")
        elif action == "view":
            print("Your To-Do List:")
            for i, todo in enumerate(todos, start=1):
                print(f"{i}. {todo}")
        elif action == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid action. Please choose add, view, or quit.")

if __name__ == "__main__":
    main()

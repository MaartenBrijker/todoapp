from app import db, Todo

first_todo = Todo(todo_text = "Learn Flask")
second_todo = Todo(todo_text = "Setup venv")
third_todo = Todo(todo_text = "Build a cool app")
db.session.add(first_todo)
db.session.add(second_todo)
db.session.add(third_todo)
db.session.commit()

# db.session.delete(Todo.query.all()[0])
# db.session.commit()

all_todos = Todo.query.all()
print(all_todos)
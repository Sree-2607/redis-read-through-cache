from fastapi import APIRouter, HTTPException
from .models import Todo


router = APIRouter()
todos: list[Todo] = []

@router.post("/todos", response_model=Todo, status_code=201)
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

@router.get("/todos", response_model=list[Todo])
def get_todos():
    return todos

@router.get("/todos/{todo_id}", response_model=Todo)
def get_todo_by_id(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@router.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            updated_todo.id = todo_id  # Ensure the ID remains the same
            todos[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

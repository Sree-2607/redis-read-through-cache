from fastapi import APIRouter, HTTPException
from .models import Todo
from .cache_service import get_todo, invalidate_todo
from .repository import (
    create_todo as create_todo_in_repo,
    get_all_todos,
    get_todo_by_id,
    update_todo,
    delete_todo
)

router = APIRouter()

# CREATE
@router.post("/todos", status_code=201)
def create_todo_route(todo: Todo):
    todo_data = todo.model_dump()
    create_todo_in_repo(todo_data)
    return todo_data

# READ ALL
@router.get("/todos")
def read_all_todos():
    return get_all_todos()

# READ ONE — THROUGH CACHE
@router.get("/todos/{todo_id}")
def read_todo(todo_id: int):
    todo = get_todo(todo_id)
    if todo is None:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )
    return todo

# UPDATE
@router.put("/todos/{todo_id}")
def update_todo_route(todo_id: int, todo: Todo):
    existing_todo = get_todo_by_id(todo_id)
    if existing_todo is None:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )
    updated_data = todo.model_dump()
    # ID should not change
    updated_data.pop("id", None)
    update_todo(
        todo_id,
        updated_data
    )
    invalidate_todo(todo_id)
    return get_todo_by_id(todo_id)

# DELETE
@router.delete("/todos/{todo_id}")
def delete_todo_route(todo_id: int):
    deleted_count = delete_todo(todo_id)
    if deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )
    invalidate_todo(todo_id)
    return {
        "message": "Todo deleted successfully"
    }
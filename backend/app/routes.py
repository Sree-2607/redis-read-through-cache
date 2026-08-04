from fastapi import APIRouter, HTTPException
from .models import Todo
from .cache_service import get_todo

router = APIRouter()

@router.get("/todos/{todo_id}")
def read_todo(todo_id:int):

    todo = get_todo(str(todo_id))

    if todo is None:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return todo

from fastapi import APIRouter
from .models import Todo


router = APIRouter()


@router.post("/todos")
def create_todo(todo: Todo):
    return todo
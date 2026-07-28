from fastapi import APIRouter
from .models import Todo


router = APIRouter()


@router.post("/todos",response_model=Todo)
def create_todo(todo: Todo):
    return todo
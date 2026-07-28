from pydantic import BaseModel


class Todo(BaseModel):
    title: str
    description: str
    completed: bool = False

todo = Todo(
    title="Learn Redis",
    description="Understand caching"
)

print(todo)
from .database import todos_collection

def get_all_todos():
    todos = list(
        todos_collection.find(
            {},
            {"_id": 0}
        )
    )
    return todos

def get_todo_by_id(todo_id: int):
    todo = todos_collection.find_one(
        {"id": todo_id},
        {"_id": 0}
    )
    return todo

def create_todo(todo_data: dict):
    result = todos_collection.insert_one(todo_data)
    return result.inserted_id

def update_todo(todo_id: int, updated_data: dict):
    result = todos_collection.update_one(
        {"id": todo_id},
        {"$set": updated_data}
    )
    return result.modified_count

def delete_todo(todo_id: int):
    result = todos_collection.delete_one(
        {"id": todo_id}
    )
    return result.deleted_count

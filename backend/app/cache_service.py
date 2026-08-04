from .redis_client import redis_client

fake_database = {
    "1": {
        "title": "Learn Redis",
        "description": "Understand caching",
        "completed": "false"
    }
}

def get_todo(todo_id):
    # 1. Check Redis first
    cached_todo = redis_client.hgetall(
        f"todo:{todo_id}"
    )
    if cached_todo:
        print("CACHE HIT")
        return cached_todo

    # 2. Cache miss
    print("CACHE MISS")
    todo = fake_database.get(todo_id)
    if todo:

        redis_client.hset(
            f"todo:{todo_id}",
            mapping=todo
        )
    return todo
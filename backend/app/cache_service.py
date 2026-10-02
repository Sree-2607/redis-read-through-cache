from .read_through_cache import ReadThroughCache
from .repository import get_todo_by_id

todo_cache = ReadThroughCache(ttl=60)

def get_todo(todo_id: int):
    cache_key = f"todo:{todo_id}"
    return todo_cache.get(
        key=cache_key,
        loader=lambda: get_todo_by_id(todo_id)
    )

def invalidate_todo(todo_id: int):
    cache_key = f"todo:{todo_id}"
    todo_cache.invalidate(cache_key)
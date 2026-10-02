import json
from typing import Callable, Optional, Dict, Any
from .redis_client import redis_client

class ReadThroughCache:

    def __init__(self, ttl: int = 60):
        self.ttl = ttl
    def get(
        self,
        key: str,
        loader: Callable[[], Optional[Dict[str, Any]]]
    ):
        # 1. Check Redis
        cached_data = redis_client.get(key)
        if cached_data:
            print("CACHE HIT")
            return json.loads(cached_data)
        # 2. Redis does not contain the key
        print("CACHE MISS")
        # 3. Load from backing database
        data = loader()
        if data is None:
            return None
        # 4. Python dictionary -> JSON string
        json_data = json.dumps(data)
        # 5. Save result in Redis with TTL
        redis_client.set(
            key,
            json_data,
            ex=self.ttl
        )
        # 6. Return database result
        return data
    
    def invalidate(self, key: str):
        redis_client.delete(key)
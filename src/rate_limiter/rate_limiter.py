from ..db import redis_client
import time

class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds

    async def is_rate_limited(self, user_id: str) -> bool:
        current_time = int(time.time())
        key = f"rate_limit:{user_id}"
        await redis_client.lpush(key, current_time)
        
        await redis_client.redis.expire(key, self.window_seconds)
        
        request_timestamps = await redis_client.redis.lrange(key, 0, -1)

        valid_requests = [int(ts) for ts in request_timestamps if current_time - int(ts) < self.window_seconds]

        await redis_client.redis.ltrim(key, 0, len(valid_requests) - 1)

        if len(valid_requests) > self.max_requests:
            return True
        
        return False
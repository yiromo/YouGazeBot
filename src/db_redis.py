import aioredis
from config import settings

class RedisClient:
    def __init__(self):
        self.redis = aioredis.from_url(settings.REDIS_HOST, decode_responses=True)

    async def set(self, key, value):
        await self.redis.set(key, value)

    async def get(self, key):
        return await self.redis.get(key)

    async def delete(self, key):
        await self.redis.delete(key)

    async def exists(self, key):
        return await self.redis.exists(key)

    async def hset(self, name, key, value):
        await self.redis.hset(name, key, value)

    async def hget(self, name, key):
        return await self.redis.hget(name, key)

    async def hdel(self, name, key):
        await self.redis.hdel(name, key)

    async def hmset(self, name, mapping):
        await self.redis.hmset_dict(name, mapping)

    async def hmget(self, name, keys):
        return await self.redis.hmget(name, keys)

    async def lpush(self, name, *values):
        await self.redis.lpush(name, *values)

    async def rpush(self, name, *values):
        await self.redis.rpush(name, *values)

    async def lpop(self, name):
        return await self.redis.lpop(name)

    async def rpop(self, name):
        return await self.redis.rpop(name)

    async def flushdb(self):
        await self.redis.flushdb()

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(RedisClient, cls).__new__(cls)
        return cls.instance

redis_client = RedisClient()

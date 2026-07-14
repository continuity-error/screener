import json
from redis import Redis
from app.core.config import get_settings

settings = get_settings()
redis_client = Redis.from_url(settings.redis_url, decode_responses=True)


def get_json(key: str):
    payload = redis_client.get(key)
    return json.loads(payload) if payload else None


def set_json(key: str, value, ttl: int):
    redis_client.setex(key, ttl, json.dumps(value, default=str))

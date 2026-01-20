import os
import psycopg2
import redis
from psycopg2.extras import RealDictCursor


def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        cursor_factory=RealDictCursor,
    )


redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    db=0
)


def redis_delete_cache(chat_id):
    for key in redis_client.scan_iter(f'notes:{chat_id}'):
        redis_client.delete(key)


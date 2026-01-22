import os
import psycopg2
import redis
from psycopg2.extras import RealDictCursor
from settings import Settings


settings = Settings()


def get_connection():
    return psycopg2.connect(
        dbname=settings.postgres_db,
        user=settings.postgres_user,
        password=settings.postgres_password,
        host=settings.postgres_host,
        port=settings.postgres_port,
        cursor_factory=RealDictCursor
    )


redis_client = redis.Redis(
    host=settings.redis_host,
    port=settings.redis_port,
    db=0
)


def redis_delete_cache(chat_id):
    for key in redis_client.scan_iter(f'notes:{chat_id}'):
        redis_client.delete(key)


import json
from db import get_connection
from db import redis_client, redis_delete_cache
from telegram import Update
from telegram.ext import ContextTypes
from producer import send_to_kafka


# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    context.chat_data[chat_id] = []
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


# /add
async def add(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = """
            INSERT INTO notes (chat_id, text)
            VALUES (%s, %s)
            RETURNING id;
        """
    chat_id = update.effective_chat.id
    note_text = " ".join(context.args)

    if not note_text:
        await update.message.reply_text("Пустая заметка, не добавлена")
        return

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (chat_id, note_text))
            conn.commit()
            await update.message.reply_text("Заметка добавлена")

    send_to_kafka(chat_id, note_text)
    redis_delete_cache(chat_id)


async def get_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = """
            SELECT text
            FROM notes
            WHERE chat_id = %s
            ORDER BY created_at DESC
            LIMIT 10;
        """
    chat_id = update.effective_chat.id
    cache_key = f'notes:{chat_id}'

    cached = redis_client.get(cache_key)
    if cached:
        notes = json.loads(cached)
        formatted_message = "\n".join(
            f"{note['text']}"
            for note in notes
        )
        await update.message.reply_text(f"Заметки из кэша:\n{formatted_message}")
        return

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (chat_id,))
            notes = cursor.fetchall()
            if not notes:
                await update.message.reply_text("Заметок не найдено")
                return

            formatted_message = "\n".join(
                    f"{note['text']}"
                    for note in notes
                )

        await update.message.reply_text(f'Последние 10 заметок: \n{formatted_message}')
        redis_client.set(cache_key, json.dumps(notes, default=str), ex=30)


async def clear_notes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = """
            DELETE FROM notes
            WHERE chat_id = %s
        """
    chat_id = update.effective_chat.id

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (chat_id,))
            conn.commit()
            await update.message.reply_text("Заметки очищены")

    redis_delete_cache(chat_id)


async def clear_cache(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    redis_delete_cache(chat_id)
    await update.message.reply_text("Кэш очищен")


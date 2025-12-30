import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv


# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    context.chat_data[chat_id] = []
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


# /add
async def add(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    args = " ".join(context.args)

    if not args:
        await update.message.reply_text("Пустая заметка")
        return

    if not context.chat_data[chat_id]:
        context.chat_data[chat_id] = []
    context.chat_data[chat_id].append(args)

    await update.message.reply_text("Заметка добавлена")
    return


async def get_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id

    if context.chat_data[chat_id]:
        messages = context.chat_data[chat_id][::-1]
        formatted_message = "\n".join(messages[:9])
        await update.message.reply_text(f'Последние заметки (максимум 10): \n{formatted_message}')

    else:
        await update.message.reply_text("Заметок не найдено")


async def clear_notes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    context.chat_data.get(chat_id, []).clear()
    await update.message.reply_text("Заметки очищены")
    return


def main():
    load_dotenv()
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

    app = ApplicationBuilder().token(bot_token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("list", get_list))
    app.add_handler(CommandHandler("clear", clear_notes))

    app.run_polling()


if __name__ == "__main__":
    main()

import threading
from bot import start, add, get_list, clear_cache, clear_notes
from telegram.ext import ApplicationBuilder, CommandHandler
from settings import Settings
from consumer import run_kafka_notes_consumer


def main():
    settings = Settings()
    app = ApplicationBuilder().token(settings.bot_token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("list", get_list))
    app.add_handler(CommandHandler("clear", clear_notes))
    app.add_handler(CommandHandler("clear_cache", clear_cache))

    consumer_thread = threading.Thread(
        target=run_kafka_notes_consumer,
        daemon=True
    )
    consumer_thread.start()

    app.run_polling()


if __name__ == "__main__":
    main()

import json
import logging
from kafka import KafkaConsumer

logger = logging.getLogger("notes_consumer")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

file_handler = logging.FileHandler("consumer.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def run_kafka_notes_consumer():
    consumer = KafkaConsumer(
        "notes",
        bootstrap_servers=["kafka:29092"],
        auto_offset_reset="earliest",
        group_id="notes_logger",
        value_deserializer=lambda m: json.loads(m.decode("utf-8"))
    )

    logger.info("Consumer started…")

    for msg in consumer:
        note = msg.value
        chat_id = note.get("chat_id")
        text = note.get("text")
        logger.info(f"New note from {chat_id}: {text}")

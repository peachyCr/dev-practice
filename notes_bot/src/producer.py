import json
from kafka import KafkaProducer


producer = KafkaProducer(
    bootstrap_servers=["broker:9092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)


def send_to_kafka(chat_id: int, text: str):
    data = {
        "chat_id": chat_id,
        "text": text
    }
    producer.send("notes", value=data)
    producer.flush()


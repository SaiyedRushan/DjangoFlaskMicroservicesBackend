import pika, json
from dotenv import load_dotenv
import os

load_dotenv()

params = pika.URLParameters(os.getenv("RABBITMQ_URL"))
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange="", routing_key="main", body=json.dumps(body), properties=properties
    )

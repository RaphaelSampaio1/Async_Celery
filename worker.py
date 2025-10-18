import os
import time
import random
from celery import Celery


app = Celery(
    'random_number', # Application name
    broker= os.getenv("CELERY_BROKER_URL"),
    backend= os.getenv("CELERY_BACKEND_URL")
)


@app.task
def generate_random_number(max_value: int):
    """Generate a random number between 1 and the max_value after a delay."""
    time.sleep(5) 
    return random.randint(1,max_value)


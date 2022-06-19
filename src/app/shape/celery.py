from celery import Celery
from src.config import ShapeConfig


app = Celery()
app.config_from_object(ShapeConfig)


if __name__ == '__main__':
    app.start()

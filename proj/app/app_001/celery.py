from celery import Celery
from proj.config import Config001


app = Celery()
app.config_from_object(Config001)


if __name__ == '__main__':
    app.start()

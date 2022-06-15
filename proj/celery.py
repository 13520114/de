from celery import Celery


app = Celery('proj',
             broker='amqp://de-broker-1',
             backend='redis://de-result_backend-1',
             include=['proj.tasks'])


app.conf.update(
  result_expires=3600,
)


if __name__ == '__main__':
  app.start()

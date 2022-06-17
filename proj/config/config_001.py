class Config001:
    broker_url = 'amqp://de-broker-1'
    result_backend = 'redis://de-result_backend-1'
    include = ['proj.module.module_001.tasks']

from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base


class Postgres:
    def __init__(self, db_user='kromlab', db_pass='kromlab',
                 db_host='kromlab_database', db_name='kromlab'):
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_host = db_host
        self.db_name = db_name
        self.engine = None
        self.base_model_class_dict = {}

    @staticmethod
    def _get_conn_str(db_user, db_pass, db_host, db_name):
        db_str = "postgresql+psycopg2://{db_user}:{db_pass}@{db_host}/{db_name}"
        return db_str.format(db_user=db_user, db_pass=db_pass,
                             db_host=db_host, db_name=db_name)

    def get_engine(self):
        if self.engine is None:
            db_str = self._get_conn_str(self.db_user, self.db_pass,
                                        self.db_host, self.db_name)
            self.engine = create_engine(db_str, echo=True)
        return self.engine

    def get_base_model_class(self, custom_base_model_class):
        base_model_class_name = custom_base_model_class.__tablename__
        base_model_class = self.base_model_class_dict.get(base_model_class_name)

        if base_model_class is None:
            base_model_class = declarative_base(cls=custom_base_model_class)
            self.base_model_class_dict[base_model_class_name] = base_model_class

        return self.base_model_class_dict[base_model_class_name]

    @contextmanager
    def get_session(self):
        with Session(self.engine) as session:
            yield session


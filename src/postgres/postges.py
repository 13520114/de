from sqlalchemy import create_engine, select
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_str = "postgresql+psycopg2://kromlab:kromlab@kromlab_database/kromlab"
db = create_engine(db_str)
base = declarative_base()

base.metadata.create_all(db)

Session = sessionmaker(db)
session = Session()

class Rectangle(base):
    __table_args__ = ({"schema": "shape"})
    __tablename__ = 'rectangle'
    rectangle_id = Column(Integer, primary_key=True)
    a = Column(Integer)
    b = Column(Integer)
    area = Column(Integer)
    perimeter = Column(Integer)


class Postgres:
    def __init__(self, host='kromlab_database', db_name='kromlab',
                 db_user='kromlab', db_pass='kromlab'):
        self.host = host
        self.db_name = db_name
        self.db_user = db_user
        self.db_pass = db_pass
        db_str = self._get_conn_str()
        self.engine = create_engine(db_str)

    def _get_conn_str(self):
        db_str = "postgresql+psycopg2://{username}:{password}@{host}/{db_name}"
        return db_str.format(username=self.db_user,
                             password=self.db_pass,
                             host=self.host,
                             db_name=self.db_name)

    def _exec_stmt(self, stmt):
        with self.engine.connect() as conn:
            conn.execute(statement=stmt)


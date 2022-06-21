from sqlalchemy import event, DDL
from sqlalchemy.schema import CreateSchema
from sqlalchemy.ext.declarative import declared_attr


class BaseModel:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    @classmethod
    def create_schema(cls):
        schema_name = cls.__table_args__.get('schema')
        event.listen(cls.metadata, 'before_create',
                     DDL(f'CREATE SCHEMA IF NOT EXISTS {schema_name}'))

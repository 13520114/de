from sqlalchemy.ext.declarative import declared_attr


class BaseModel:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

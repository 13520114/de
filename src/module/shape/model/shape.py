from sqlalchemy import select, update
from sqlalchemy import Column, Integer
from src.postgres import pg_handler, BaseModel


class Shape(BaseModel):
    __table_args__ = {'schema': 'shape'}
    area = Column(Integer)
    perimeter = Column(Integer)
    id = Column(Integer, primary_key=True)

    def calc_area(self):
        pass

    def calc_perimeter(self):
        pass

    @classmethod
    def find_by_id(cls, id):
        found = None
        with pg_handler.get_session() as session:
            found = session.query(cls).get(id)
        return found

    def update(self):
        with pg_handler.get_session() as session:
            session.add(self)
            session.commit()


Shape = pg_handler.get_base_model_class(Shape)

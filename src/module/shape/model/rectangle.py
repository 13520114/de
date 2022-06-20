from unicodedata import name
from sqlalchemy import select
from sqlalchemy import Column, Integer
from src.module.shape.model.shape import Shape


class Rectangle(Shape):
    a = Column(Integer)
    b = Column(Integer)
    area = Column(Integer)
    perimeter = Column(Integer)
    id = Column(Integer, name='rectangle_id', primary_key=True)

    def calc_area(self):
        self.area = self.a * self.b
        return self.area

    def calc_perimeter(self):
        self.perimeter = sum((self.a, self.b)) * 2
        return self.perimeter

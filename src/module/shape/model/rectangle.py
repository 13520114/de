from sqlalchemy import Column, Integer
from src.module.shape.model.shape import Shape
from src.module.shape.model.shape import InvalidInputException


class Rectangle(Shape):
    a = Column(Integer)
    b = Column(Integer)
    area = Column(Integer)
    perimeter = Column(Integer)
    id = Column(Integer, name='rectangle_id', primary_key=True)

    def _validate(self):
        if type(self.a) != int or type(self.b) != int or \
                self.a <= 0 or self.b <= 0:
            raise InvalidInputException

    def calc_area(self):
        self._validate()
        self.area = self.a * self.b
        return self.area

    def calc_perimeter(self):
        self._validate()
        self.perimeter = sum((self.a, self.b)) * 2
        return self.perimeter

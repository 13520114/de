from pytest import fail

from src.module.shape.model.rectangle import Rectangle
from src.module.shape.model.shape import InvalidInputException


class TestRectangle:
    def test_calc_area_with_valid_input(self):
        rectangle = Rectangle()
        rectangle.a = 3
        rectangle.b = 6
        area = rectangle.calc_area()
        assert area == 18

    def test_calc_area_with_invalid_input(self):
        exception_caught = False
        rectangle = Rectangle()
        rectangle.a = -1
        rectangle.b = 6
        try:
            rectangle.calc_area()
        except InvalidInputException:
            exception_caught = True

        if exception_caught is False:
            fail('Do not throw expected exception (InvalidInputException)')

    def test_calc_perimeter_with_valid_input(self):
        rectangle = Rectangle()
        rectangle.a = 3
        rectangle.b = 6
        perimeter = rectangle.calc_perimeter()
        assert perimeter == 18

    def test_calc_perimeter_with_invalid_input(self):
        exception_caught = False
        rectangle = Rectangle()
        rectangle.a = -1
        rectangle.b = 6
        try:
            rectangle.calc_perimeter()
        except InvalidInputException:
            exception_caught = True

        if exception_caught is False:
            fail('Do not throw expected exception (InvalidInputException)')

from src.app.shape import app
from src.module.shape.model import Rectangle


@app.task
def list_all():
    result = []
    all = Rectangle.list_all()
    for item in all:
        result.append({'id': item.id, 'a': item.a, 'b': item.b,
                       'area': item.area, 'perimeter': item.perimeter})
    return result


@app.task
def create(a, b):
    rectangle = Rectangle()
    rectangle.a = a
    rectangle.b = b
    rectangle_id = rectangle.update()
    return {'id': rectangle_id, 'a': a, 'b': b}


@app.task
def update(id):
    rectangle = Rectangle.find_by_id(id)
    if rectangle:
        area = rectangle.calc_area()
        perimeter = rectangle.calc_perimeter()
        rectangle.update()
        return {'status': 'OK', 'area': area, 'perimeter': perimeter}

    return {'status': 'NOK', 'message': 'Rectangle not found'}

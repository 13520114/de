from src.app.shape import app
from src.module.shape.model import Rectangle


@app.task
def update(id):
    rectangle = Rectangle.find_by_id(id)
    if rectangle:
        area = rectangle.calc_area()
        perimeter = rectangle.calc_perimeter()
        rectangle.update()
        return {'status': 'OK', 'area': area, 'perimeter': perimeter}

    return {'status': 'NOK', 'message': 'Rectangle not found'}

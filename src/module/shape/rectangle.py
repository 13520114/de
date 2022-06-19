from src.app.shape import app


class Rectangle:
    def __init__(self, id, a, b):
        self.id = None
        self.a = None
        self.b = None

    @staticmethod
    def find(id):
        database = {
            1: {'a': 1, 'b': 2},
            2: {'a': 3, 'b': 4},
            3: {'a': 5, 'b': 6},
            4: {'a': 7, 'b': 8}
        }

        res = database.get(id)
        return Rectangle(id=id, a=res['a'], b=res['b']) if res else None

    def calculate_area(self):
        return self.a * self.b

    def calculate_perimeter(self):
        return (self.a + self.b) * 2


@app.task
def update(id):
    res = Rectangle.find(id)
    return res

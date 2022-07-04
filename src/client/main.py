from flask import Flask, request, render_template
from src.module.shape.tasks.rectangle import list_all, create, update


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello world!</p>"


@app.route('/rectangle/', methods=['GET'])
def list_rectangle():
    result = list_all.delay()
    rectangles = result.get()
    return render_template('rectangle.html', rectangles=rectangles)


@app.route('/rectangle/create/', methods=['GET'])
def create_rectangle():
    args = request.args.to_dict()
    a = args.get('a')
    b = args.get('b')

    if not all([a, b]):
        return 'a or b is missing!'

    if not a.isdigit():
        return 'a is not digit!'

    if not b.isdigit():
        return 'b is not digit!'

    result = create.delay(int(a), int(b))
    new_rectangle = result.get()
    update.delay(new_rectangle['id'])
    return f'New rectangle a={a}, b={b} is created successfully!.' \
           f'\nCalculating area and perimeter asynchronously'

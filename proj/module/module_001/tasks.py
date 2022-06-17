from proj.app.app_001 import app

@app.task
def add(x, y): return x + y

@app.task
def mul(x, y): return x * y

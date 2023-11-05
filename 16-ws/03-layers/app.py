from flask import Flask, request, abort, render_template
import model

app = Flask(__name__)


@app.get("/tasks")
def read_tasks():
    return model.read_tasks()


@app.get("/tasks/<id>")
def read_task(id):
    task_id = int(id)

    try:
        return model.read_task(task_id)
    except FileNotFoundError:
        app.logger.warning('Task %d not found', task_id)
        abort(404)


@app.post("/tasks")
def create_task():
    new_task = request.json

    return model.create_task(new_task)


@app.put("/tasks/<id>")
def replace_task(id):
    task_id = int(id)
    new_task = request.json

    try:
        return model.replace_task(task_id, new_task)
    except FileNotFoundError:
        app.logger.warning('Task %d not found', task_id)
        abort(404)


@app.patch("/tasks/<id>")
def update_task(id):
    task_id = int(id)
    patch = request.json

    try:
        return model.update_task(task_id, patch)
    except FileNotFoundError:
        app.logger.warning('Task %d not found', task_id)
        abort(404)


@app.delete("/tasks/<id>")
def delete_task(id):
    task_id = int(id)

    try:
        return model.delete_task(task_id)
    except FileNotFoundError:
        app.logger.warning('Task %d not found', task_id)
        abort(404)

# Use a common template for all 404 errors


@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html'), 404  # send 404 instead of 200

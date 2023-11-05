from flask import Flask, request, abort, render_template

app = Flask(__name__)

tasks = [
    {'id': 1, 'text': 'Learn Python', 'completed': True},
    {'id': 2, 'text': 'Look for a job', 'completed': False},
    {'id': 3, 'text': 'Forget everything'},
]


@app.get("/tasks")
def read_tasks():
    return tasks


@app.get("/tasks/<id>")
def read_task(id):
    task_id = int(id)

    try:
        return next(task for task in tasks if task['id'] == task_id)
    except StopIteration:
        app.logger.warning('Task %d not found', task_id)
        abort(404)


@app.post("/tasks")
def create_task():
    new_task = request.json
    max_id = tasks[len(tasks)-1]['id'] if len(tasks) else 0
    new_task['id'] = max_id + 1
    tasks.append(new_task)
    return new_task


@app.put("/tasks/<id>")
def replace_task(id):
    task_id = int(id)
    new_task = request.json

    try:
        index = next(index for index, task in enumerate(
            tasks) if task['id'] == task_id)
        new_task['id'] = task_id
        tasks[index] = new_task
        return new_task
    except StopIteration:
        app.logger.warning('Task %d not found', task_id)
        abort(404)


@app.patch("/tasks/<id>")
def update_task(id):
    task_id = int(id)
    patch = request.json

    try:
        index = next(index for index, task in enumerate(
            tasks) if task['id'] == task_id)
        tasks[index].update(patch)
        return tasks[index]
    except StopIteration:
        app.logger.warning('Task %d not found', task_id)
        abort(404)


@app.delete("/tasks/<id>")
def delete_task(id):
    task_id = int(id)

    try:
        index = next(index for index, task in enumerate(
            tasks) if task['id'] == task_id)
        deleted_task = tasks[index]
        tasks.remove(deleted_task)
        return deleted_task
    except StopIteration:
        app.logger.warning('Task %d not found', task_id)
        abort(404)

# Use a common template for all 404 errors


@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html'), 404  # send 404 instead of 200

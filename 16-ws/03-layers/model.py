tasks = [
    {'id': 1, 'text': 'Learn Python', 'completed': True},
    {'id': 2, 'text': 'Look for a job', 'completed': False},
    {'id': 3, 'text': 'Forget everything'},
]


def read_tasks():
    return tasks


def read_task(task_id):
    try:
        return next(task for task in tasks if task['id'] == task_id)
    except StopIteration:
        raise FileNotFoundError(task_id)


def create_task(new_task):
    max_id = tasks[len(tasks)-1]['id'] if len(tasks) else 0
    new_task['id'] = max_id + 1
    tasks.append(new_task)
    return new_task


def replace_task(task_id, new_task):
    try:
        index = next(index for index, task in enumerate(
            tasks) if task['id'] == task_id)
        new_task['id'] = task_id
        tasks[index] = new_task
        return new_task
    except StopIteration:
        raise FileNotFoundError(task_id)


def update_task(task_id, patch):
    try:
        index = next(index for index, task in enumerate(
            tasks) if task['id'] == task_id)
        tasks[index].update(patch)
        return tasks[index]
    except StopIteration:
        raise FileNotFoundError(task_id)


def delete_task(task_id):
    try:
        index = next(index for index, task in enumerate(
            tasks) if task['id'] == task_id)
        deleted_task = tasks[index]
        tasks.remove(deleted_task)
        return deleted_task
    except StopIteration:
        raise FileNotFoundError(task_id)

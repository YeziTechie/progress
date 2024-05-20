from tasks.models.task import Task


def total_tasks_done():
    result = 0
    tasks = Task.objects.all()

    for task in tasks:
        if task.is_done is True:
            result += 1

    return result

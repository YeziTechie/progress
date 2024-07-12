from tasks.models.normal_task import NormalTask


def total_tasks_done():
    result = 0
    tasks = NormalTask.objects.all()

    for task in tasks:
        if task.is_done is True:
            result += 1

    return result

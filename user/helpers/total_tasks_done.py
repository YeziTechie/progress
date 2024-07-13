from tasks.models.classic_task import ClassicTask


def total_tasks_done():
    result = 0
    classic_tasks = ClassicTask.objects.all()

    for task in classic_tasks:
        if task.is_done is True:
            result += 1

    return result

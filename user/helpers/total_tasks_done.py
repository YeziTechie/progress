from tasks.models.classic import Classic


def total_tasks_done():
    result = 0
    tasks = Classic.objects.all()

    for task in tasks:
        if task.is_done is True:
            result += 1

    return result

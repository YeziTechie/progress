from tasks.models.task import Task
from abilities.models.outcome import Outcome


def total_xp():
    abilities = Outcome.objects.all()
    result = 0

    for ability in abilities:
        result += ability.total_xp

    tasks = Task.objects.all()

    for task in tasks:
        if task.is_done is True and task.is_added is False and task.ability is False:
            result += task.xp

    return result

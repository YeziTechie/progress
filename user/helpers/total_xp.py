from tasks.models.task import Task
from abilities.models.outcome import Outcome


def total_xp():
    outcomes = Outcome.objects.all()
    result = 0

    for outcome in outcomes:
        result += outcome.total_xp

    tasks = Task.objects.all()

    for task in tasks:
        if task.is_done is True and task.is_added is False and task.outcome is False:
            result += task.xp

    return result

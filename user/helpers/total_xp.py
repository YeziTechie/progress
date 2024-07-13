from tasks.models.classic_task import ClassicTask
from abilities.models.outcome import Outcome


def total_xp():
    outcomes = Outcome.objects.all()
    result = 0

    for outcome in outcomes:
        result += outcome.total_xp

    classic_tasks = ClassicTask.objects.all()

    for task in classic_tasks:
        if task.is_done is True and task.is_added is False and task.outcome is False:
            result += task.xp

    return result

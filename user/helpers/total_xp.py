from tasks.models.classic import Classic
from abilities.models.outcome import Outcome


def total_xp():
    outcomes = Outcome.objects.all()
    tasks = Classic.objects.all()
    result = 0

    for outcome in outcomes:
        result += outcome.total_xp
    for task in tasks:
        if task.is_done is True and task.is_added is False and task.outcome is False:
            result += task.xp
    return result

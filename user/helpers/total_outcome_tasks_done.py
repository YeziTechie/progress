from tasks.models.classic_task import ClassicTask
from abilities.models.outcome import Outcome


def outcome_total_tasks_done(pk):
    outcome = Outcome.objects.get(pk=pk)
    classic_tasks = ClassicTask.objects.filter(outcome=outcome)
    result = 0

    for task in classic_tasks:
        if task.is_done is True:
            result += 1

    return result

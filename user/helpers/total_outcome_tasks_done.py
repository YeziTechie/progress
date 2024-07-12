from tasks.models.normal_task import NormalTask
from abilities.models.outcome import Outcome


def outcome_total_tasks_done(pk):
    outcome = Outcome.objects.get(pk=pk)
    tasks = NormalTask.objects.filter(outcome=outcome)

    result = 0

    for task in tasks:
        if task.is_done is True:
            result += 1

    return result

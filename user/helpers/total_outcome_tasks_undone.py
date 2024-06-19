from tasks.models.task import Task
from outcomes.models.outcome import Outcome


def outcome_total_tasks_undone(pk):
    outcome = Outcome.objects.get(pk=pk)
    tasks = Task.objects.filter(outcome=outcome)

    result = 0

    for task in tasks:
        if task.is_done is False:
            result += 1

    return result

from tasks.models.classic import Classic
from abilities.models.outcome import Outcome


def outcome_total_tasks_done(pk):
    outcome = Outcome.objects.get(pk=pk)
    tasks = Classic.objects.filter(outcome=outcome)
    result = 0

    for task in tasks:
        if task.is_done is True:
            result += 1

    return result

from tasks.models.task import Task
from abilities.models.ability import Ability


def outcome_total_tasks_done(pk):
    ability = Ability.objects.get(pk=pk)
    tasks = Task.objects.filter(ability=ability)

    result = 0

    for task in tasks:
        if task.is_done is True:
            result += 1

    return result

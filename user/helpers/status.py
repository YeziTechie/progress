from tasks.models.classic import Classic
from tasks.models.deadline import Deadline
from tasks.models.time import Time
from tasks.models.count import Count

from abilities.models.outcome import Outcome


def outcome_active_tasks(pk):
    outcome = Outcome.objects.get(pk=pk)

    classics = Classic.objects.filter(outcome=outcome)
    deadlines = Deadline.objects.filter(outcome=outcome)
    counts = Count.objects.filter(outcome=outcome)
    times = Time.objects.filter(outcome=outcome)

    result = 0
    result += len(times) + len(counts)

    for classic in classics:
        if classic.is_done is False:
            result += 1

    for deadline in deadlines:
        if deadline.is_done is False:
            result += 1

    return result


def total_tasks_done():
    result = 0
    tasks = Classic.objects.all()

    for task in tasks:
        if task.is_done is True:
            result += 1

    return result


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


def time_spent():
    tasks = Time.objects.all()
    total_time = 0
    for task in tasks:
        total_time += task.total_time

    return total_time


def count_scored():
    tasks = Count.objects.all()
    total_count = 0
    for task in tasks:
        total_count += task.total_count

    return total_count


def total_xp_lost():
    tasks = Deadline.objects.all()
    xp_lost = 0
    for task in tasks:
        xp_lost += task.penalty_xp

    return xp_lost

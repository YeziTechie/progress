from tasks.models.classic import Classic
from tasks.models.deadline import Deadline
from tasks.models.time import Time
from tasks.models.count import Count


def outcome_active_tasks(pk):
    from abilities.models.outcome import Outcome
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


def total_xp():
    from abilities.models.outcome import Outcome
    level = 0
    for i in Outcome.objects.all():
        level += i.level()
    return level


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

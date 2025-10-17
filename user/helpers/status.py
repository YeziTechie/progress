from tasks.models.deadline import Deadline
from tasks.models.time import Time
from tasks.models.count import Count


def total_xp(user):
    from outcomes.models.outcome import Outcome
    xp = 0
    for i in Outcome.objects.filter(owner=user):
        xp += i.total_xp()
    return xp


def time_spent(user):
    tasks = Time.objects.filter(owner=user)
    total_time = 0
    for task in tasks:
        total_time += task.total_time

    return total_time


def count_scored(user):
    tasks = Count.objects.filter(owner=user)
    total_count = 0
    for task in tasks:
        total_count += task.total_count

    return total_count


def total_xp_lost(user):
    tasks = Deadline.objects.filter(owner=user)
    xp_lost = 0
    for task in tasks:
        xp_lost += task.penalty_xp

    return xp_lost

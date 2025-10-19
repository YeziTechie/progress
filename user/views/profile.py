from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from user.helpers.status import total_xp_lost, time_spent, count_scored, total_xp

from user.helpers.generate_level import calculate_level, calculate_xp_for_level

from outcomes.models.outcome import Outcome
from tasks.models.classic import Classic
from tasks.models.deadline import Deadline


@login_required(login_url='login')
def UserProfileView(request):
    user = request.user

    # --- XP and level calculation ---
    user_total_xp = total_xp(user)  # ensure total_xp() accepts user if needed
    level = calculate_level(user_total_xp)
    next_level_xp = calculate_xp_for_level(level + 1) - calculate_xp_for_level(level)
    xp = user_total_xp - calculate_xp_for_level(level)

    per1 = f'{round((xp / next_level_xp) * 100)}%' if next_level_xp != 0 else '0%'
    per2 = f'{round(((next_level_xp - xp) / next_level_xp) * 100)}%' if next_level_xp != 0 else '100%'

    # --- Highest XP task ---
    classic_high = Classic.objects.filter(owner=user, is_done=True).order_by('-xp').first()
    deadline_high = Deadline.objects.filter(owner=user, is_done=True).order_by('-xp').first()

    highest_xp = max(
        [t.xp for t in [classic_high, deadline_high] if t is not None],
        default=0
    )

    # --- Last task done ---
    classic_done = Classic.objects.filter(owner=user, is_done=True).order_by('-done_at').first()
    deadline_done = Deadline.objects.filter(owner=user, is_done=True).order_by('-deadline_date').first()

    last_task_done = None
    if classic_done and deadline_done:
        last_task_done = max(classic_done.done_at, deadline_done.deadline_date)
    elif classic_done:
        last_task_done = classic_done.done_at
    elif deadline_done:
        last_task_done = deadline_done.deadline_date
    else:
        last_task_done = 'None'

    # --- User-specific outcomes and tasks ---
    outcomes = Outcome.objects.filter(owner=user)
    deadlines = Deadline.objects.filter(owner=user, is_done=False)
    classics = Classic.objects.filter(owner=user, is_done=False)

    now = timezone.now().date()

    for deadline in deadlines:
        days = (deadline.deadline_date.date() - now).days
        if days < 0:
            deadline.deadline_date = f'{abs(days)} days passed'
        else:
            deadline.deadline_date = f'{days} days left'

    for classic in classics:
        classic.created_at = (classic.created_at.date() - now).days * -1

    # --- Context ---
    context = {
        'total_xp': xp,
        'level': level,
        'next_level_xp': next_level_xp,
        'filled': per1,
        'remaining': per2,
        'deadlines': deadlines,
        'classics': classics,
        'classic_done': Classic.objects.filter(owner=user, is_done=True).count(),
        'deadline_done': Deadline.objects.filter(owner=user, is_done=True).count(),
        'count_scored': count_scored(user),  # update helper functions to accept user
        'time_spent': time_spent(user),      # update helper functions to accept user
        'outcomes': outcomes,
        'total_outcomes': outcomes.count(),
        'last_outcome_created': outcomes.order_by('-created_at').first(),
        'last_outcome_achieved': outcomes.order_by('-achieved_at').first(),
        'highest_xp_by_single_task': highest_xp,
        'last_task_done': last_task_done,
        'total_xp_lost': total_xp_lost(user),  # update helper functions to accept user
    }

    return render(request, 'profile.html', context)

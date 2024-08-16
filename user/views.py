from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.views import View

from .helpers.status import *
from .helpers.generate_level import calculate_level, calculate_xp_for_level

from outcomes.models.outcome import Outcome

from tasks.models.classic import Classic

class UserProfileView(View):
    def get(self, request, *args, **kwargs):

        # xp and level, next level and current xp and stuff

        level = calculate_level(total_xp())
        next_level_xp = calculate_xp_for_level(level + 1) - calculate_xp_for_level(level)
        xp = total_xp() - calculate_xp_for_level(level)

        # Percentage for width of the design of xp bar element in front-end

        per1 = f'{round((xp / next_level_xp) * 100)}%'
        per2 = f'{round(((next_level_xp - xp) / next_level_xp) * 100)}%'

        # highest xp
        classic_high = Classic.objects.filter(is_done=True).order_by('-xp').first()
        deadline_high = Deadline.objects.filter(is_done=True).order_by('-xp').first()

        highest_xp = 0

        if classic_high and deadline_high:
            if classic_high.xp > deadline_high.xp:
                highest_xp = classic_high.xp
            else:
                highest_xp = deadline_high.xp
        elif classic_high:
            highest_xp = classic_high.xp
        elif deadline_high:
            highest_xp = deadline_high.xp

        # last task done
        classic_done = Classic.objects.filter(is_done=True).order_by('-done_at').first()
        deadline_done = Deadline.objects.filter(is_done=True).order_by('-deadline_date').first()

        last_task_done = 'None'

        if classic_done and deadline_done:
            if deadline_done.deadline_date < classic_done.done_at:
                last_task_done = classic_done.done_at
            else:
                last_task_done = deadline_done.deadline_date
        elif classic_done:
            last_task_done = classic_done.done_at
        elif deadline_done:
            last_task_done = deadline_done.deadline_date

        # outcomes
        outcomes = Outcome.objects.all()

        # tasks
        deadlines = Deadline.objects.filter(is_done=False)
        classics = Classic.objects.filter(is_done=False)
        now = timezone.now().date()

        for deadline in deadlines:
            days = (deadline.deadline_date.date() - now).days

            if days < 0:
                deadline.deadline_date = f'{abs((deadline.deadline_date.date() - now).days)} days passed'
            else:
                deadline.deadline_date = f'{abs((deadline.deadline_date.date() - now).days)} days left'

        for classic in classics:
            classic.created_at = (classic.created_at.date() - now).days * -1

        # finally, context
        context = {
            'total_xp': xp,
            'level': level,
            'next_level_xp': next_level_xp,

            'filled': per1,
            'remaining': per2,

            'deadlines': deadlines,
            'classics': classics,

            'classic_done': len(Classic.objects.filter(is_done=True)),
            'deadline_done': len(Deadline.objects.filter(is_done=True)),
            'count_scored': count_scored(),
            'time_spent': time_spent(),

            'outcomes': outcomes,
            'total_outcomes': len(Outcome.objects.all()),
            'last_outcome_created': Outcome.objects.order_by('-created_at').first(),
            'last_outcome_achieved': Outcome.objects.order_by('-achieved_at').first(),

            'highest_xp_by_single_task': highest_xp,
            'last_task_done': last_task_done,
            'total_xp_lost': total_xp_lost(),
        }

        return render(request, 'profile.html', context)

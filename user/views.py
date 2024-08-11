from datetime import timedelta

from django.utils import timezone
from django.shortcuts import render
from django.views import View

from .helpers.status import *
from .helpers.generate_level import calculate_level, calculate_xp_for_level


class UserProfileView(View):

    def get(self, request, *args, **kwargs):

        # xp and level, next level and current xp and stuff
        xp = total_xp()
        level = calculate_level(xp=xp)
        next_level_xp = calculate_xp_for_level(calculate_level(xp=xp) + 1)
        xp = xp - calculate_xp_for_level(level)
        next_level_xp = next_level_xp - calculate_xp_for_level(level)

        # Percentage for width of the design of xp bar element in front-end
        num1 = xp
        num2 = next_level_xp - xp
        per1 = round((num1 / next_level_xp) * 100)
        per2 = round((num2 / next_level_xp) * 100)

        # highest xp
        classic_high = Classic.objects.order_by('-xp').first()
        deadline_high = Deadline.objects.order_by('-xp').first()

        if deadline_high.xp < classic_high.xp:
            highest_xp = classic_high.xp
        else:
            highest_xp = deadline_high.xp

        # last task done
        classic_done = Classic.objects.order_by('-done_at').first()
        deadline_done = Deadline.objects.order_by('-deadline_date').first()

        if deadline_done.deadline_date < classic_done.done_at:
            last_task_done = deadline_done.deadline_date
        else:
            last_task_done = classic_done.done_at

        outcomes = Outcome.objects.all()
        res = []

        # outcome information
        for outcome in outcomes:
            output = {
                "pk": outcome.pk,
                "name": outcome.name,
                "active_tasks": outcome_active_tasks(outcome.pk),
            }

            res.append(output)

        # tasks
        deadlines = Deadline.objects.filter(is_done=False)
        classics = Classic.objects.filter(is_done=False)
        now = timezone.now().date()

        for deadline in deadlines:
            days = (deadline.deadline_date.date() - now).days

            if days < 0:
                deadline.deadline_date = f'{abs((deadline.deadline_date.date() - now).days)} day passed'
            else:
                deadline.deadline_date = f'{abs((deadline.deadline_date.date() - now).days)} day left'

        for classic in classics:
            classic.created_at = (classic.created_at.date() - now).days * -1


        # finally, context
        context = {
            'total_xp': xp,
            'level': calculate_level(xp=total_xp()),
            'next_level_xp': next_level_xp,

            'filled': per1,
            'remaining': per2,

            'deadlines': deadlines,
            'classics': classics,

            'classic_done': len(Classic.objects.filter(is_done=True)),
            'deadline_done': len(Deadline.objects.filter(is_done=True)),
            'count_scored': count_scored(),
            'time_spent': time_spent(),

            'outcomes': res,
            'total_outcomes': len(Outcome.objects.all()),
            'last_outcome_created': Outcome.objects.order_by('-created_at').first(),
            'last_outcome_achieved': Outcome.objects.order_by('-achieved_at', 'is_achieved').first(),

            'highest_xp_by_single_task': highest_xp,
            'last_task_done': last_task_done,
            'total_xp_lost': total_xp_lost(),
        }

        return render(request, 'profile.html', context)
